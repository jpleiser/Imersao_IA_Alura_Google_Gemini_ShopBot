import os
import sqlite3
import google.generativeai as genai
import json
from typing import List

class ShopBot:

    STEP_WELCOME:str = "WELCOME"
    STEP_CHATBOT = "CHATBOT"
    STEP_FINISH= "FINISH"

    def __init__(self):

        self.intent = None
        self.question = None
        self.response = None
        self.query = None

        self.history = []

        genai.configure(api_key=os.getenv("GEMINI_TOKEN_KEY"))

        self.step:str = ShopBot.STEP_WELCOME

        # Set up the model
        self.generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 0,
            "max_output_tokens": 8192,
        }

        self.safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_NONE"
        },
        ]

        system_instruction = """
            Você é um assistente pessoal atencioso especializado em banco de dados relacional com profundamente conhecimento em PNL.

            - Como assistente pessoal, você deverá retornar a estrutura do exemplo 1.
            **Exemplo 1:** 
            ```json  
            {
                "question": "question name",
                "response\": "response name" 
            }  
            ```

            - Como especialista em banco de dados relacional você deverá analisar o esquema de dados definido abaixo e 
              dever gerar comandos SQL na sintaxe correta sem incluir os ids no resultado da consulta de forma que eu possa
              executar em um banco de dados sql-lite. Voce deverá retornar o resultado conforme estrutura de exemplo 2:

            **&Exemplo 2:**
            ```json
            {
                "intent": "SQL",
                "question": "question name",
                "response": "response name", 
                "query": "command sql"
            }
            ```

            Aqui estão alguns exemplos de perguntas que o usuário constuma fazer durante a interação com o chatbot:
            exemplos de consulta na lista de compras:
            - Usuario: [
                - liste as minhas compras deste mês
                - qual foi a minha primeira compra 
                - Liste todas as minhas compras
                - Quais foram as lojas que eu comprei neste mês
                - Quais produtos eu pagugei mais barato e em que loja
            ]    
            - Exemplo de reposta:[
                SELECT   
                    loja.nome AS 'Nome da Loja',  
                    loja.endereco AS 'Endereço da Loja',  
                    loja.cidade AS 'Cidade da Loja',  
                    loja.estado AS 'Estado da Loja',  
                    produto.descricao AS 'Descrição do Produto',  
                    produto.categoria AS 'Categoria do Produto',  
                    produto.unidade_medida AS 'Unidade de Medida do Produto',  
                    lista_de_compras.quantidade AS 'Quantidade Comprada',  
                    lista_de_compras.preco_unitario AS 'Preço Unitário',  
                    lista_de_compras.valor_compra AS 'Valor da Compra',  
                    lista_de_compras.data_compra AS 'Data da Compra'  
                FROM   
                    lista_de_compras  
                INNER JOIN   
                    loja ON lista_de_compras.loja_codigo = loja.codigo  
                INNER JOIN   
                    produto ON lista_de_compras.produto_codigo = produto.codigo;  
            
            ]

            
            Exemplos de consulta de preços produto loja:
            - Usuario: [
                - Qual loja possui o menor preço do produto arroz
                - Liste os produtos e as lojas que possuem o menor preço
                - liste as 2 lojas que possuem o menor preço para o produto feijão
            ]
            - Exemplo de reposta:[
                SELECT   
                        loja.nome AS Loja,   
                        loja.endereco AS Endereco,   
                        loja.cidade AS Cidade,   
                        loja.estado AS Estado,   
                        produto.descricao AS Produto,   
                        produto.categoria AS Categoria,   
                        produto.unidade_medida AS Unidade,   
                        loja_produto_preco.preco AS Preco  
                FROM   
                        loja_produto_preco 
                        INNER JOIN   
                                loja ON loja_produto_preco.loja_codigo = loja.codigo  
                        INNER JOIN   
                                produto ON loja_produto_preco.produto_codigo = produto.codigo;              

            ]

            
            Exemplos de consulta de menor, maior, média de preços produto loja:
            - Usuario: [
                - Em que loja eu posso fazer compras e pagar o menor preço para o arroz, feijão e papel higiênico
            ]
            - Exemplo de reposta:[
                SELECT   
                        loja.nome AS Loja,   
                        loja.endereco AS Endereco,   
                        loja.cidade AS Cidade,   
                        loja.estado AS Estado,   
                        produto.descricao AS Produto,   
                        produto.categoria AS Categoria,   
                        produto.unidade_medida AS Unidade,   
                        loja_produto_preco.preco AS Preco  
                FROM   
                        loja_produto_preco 
                        INNER JOIN   
                                loja ON loja_produto_preco.loja_codigo = loja.codigo  
                        INNER JOIN   
                                produto ON loja_produto_preco.produto_codigo = produto.codigo;              

            ]

            - **Esquema de dados**
            ```json   
            {  
                "intent": "SQL",  
                "question": "question name",  
                "response": "response name",  
                "query": "command sql"  
            }
            ```
            ```sql
                CREATE TABLE loja (
                codigo INTEGER PRIMARY KEY,
                nome TEXT,
                endereco TEXT,
                cidade TEXT,
                estado TEXT
                );

                CREATE TABLE produto (
                codigo INTEGER PRIMARY KEY,
                descricao TEXT,
                categoria TEXT,
                unidade_medida TEXT
                );

                CREATE TABLE loja_produto_preco (
                loja_codigo INTEGER,
                produto_codigo INTEGER,
                preco REAL,
                PRIMARY KEY (loja_codigo, produto_codigo),
                FOREIGN KEY (loja_codigo) REFERENCES loja(codigo),
                FOREIGN KEY (produto_codigo) REFERENCES produto(codigo)
                );

                CREATE TABLE lista_compras (
                id INTEGER PRIMARY KEY,
                quantidade DECIMAL(10,4),
                preco_unitario REAL,
                valor_compra REAL,
                data_compra DATE,
                loja_produto_preco_loja_codigo INTEGER,
                loja_produto_preco_produto_codigo INTEGER,
                FOREIGN KEY (loja_produto_preco_loja_codigo, loja_produto_preco_produto_codigo) REFERENCES loja_produto_preco(loja_codigo, produto_codigo)
                );
            ````
        """

        self.model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                    generation_config=self.generation_config,
                                    system_instruction=system_instruction,
                                    safety_settings=self.safety_settings)

        self.convo = self.model.start_chat(history=self.history)

    
    def __send_message_rag(self,question:str):
        
        system_instruction_rag = "você é um web-design com profundo conhecimento em html, css3 e botstrap, quero que Analise os dados fornecido pelo usuário e converta os dados para um formato html para uma melhor visualização."

        model_rag = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                    generation_config=self.generation_config,
                                    system_instruction=system_instruction_rag,
                                    safety_settings=self.safety_settings)

        convo = model_rag.start_chat(history=[])
        convo.send_message(question)
        
        print(convo.last.text)

        return convo.last.text


    def __clean_json(self, json_text:str) -> str:
        startIndex:int = json_text.find("```json")
        if startIndex >= 0:
            json_text= json_text[startIndex+len("```json"):]
            endIndex:int = json_text.find("```")
            if endIndex > startIndex:
                return json_text[0: endIndex]
        return json_text


    def __refresh_data(self, jsonObject):    
        self.intent     = jsonObject.get("intent", None)
        self.question   = jsonObject.get("question", None)
        self.response   = jsonObject.get("response", None)
        self.query      = jsonObject.get("query", None)


    def __executeQuery(self, query:str) -> str:  
        markdown_result = "" 

        # Conecte-se ao banco de dados SQLite (ou crie se não existir)    
        with sqlite3.connect('ShopBot.db') as connection:    
            cursor = connection.cursor()    
            try:                 
                # Executar uma consulta SQL    
                cursor.execute(query)    
                
                # Obter os nomes das colunas    
                column_names = [description[0] for description in cursor.description]    
                
                # Adicionar nomes de colunas ao resultado markdown  
                markdown_result += " | ".join(column_names) + "\n"  
                
                # Adicionar linha de separação  
                markdown_result += " | ".join(["---"]*len(column_names)) + "\n"  
                
                # Obter dados da consulta  
                data = cursor.fetchall()  
                
                # Adicionar dados ao resultado markdown  
                for row in data:  
                    markdown_result += " | ".join(str(item) for item in row) + "\n"                  
                # self.__send_message_rag(f"dados do usuário para renderização:\n{self.response}\n{markdown_result}")

            except sqlite3.OperationalError as e:   
                print(f"An error occurred: {e}")

        if len(markdown_result) == 0:
            markdown_result = None
        else:
            print(markdown_result)

        return markdown_result  


    def welcome(self):

        # Eu monitoro as flutuações de preços e posso até prever o melhor momento para você comprar um produto específico 📈.  

        welcome:str = """
            
            👋 Olá seja bem-vindo ao <b>ShopBot</b>! 🤖 seu assistente pessoal para compras inteligentes e econômicas. 
            Estou aqui para ajudá-lo a encontrar as melhores ofertas 🛍️, comparar preços 💰 e analisar seu histórico 
            de compras 📊 para que você possa tomar decisões de compra mais acertivas.  
            <br/>
            Meu objetivo é tornar suas compras mais eficientes e econômicas.
            Quer saber onde encontrar o melhor preço para um produto? 
            <br/>
            É só perguntar! Eu posso comparar preços em várias lojas, permitindo que você economize tempo ⏳ 
            e dinheiro 💵.  
            <br/>
            Além disso, posso analisar seus padrões de gastos 💳 e ajudá-lo a identificar áreas onde você pode economizar. 
            <hr/>

            Aqui estão alguns exemplos de perguntas que você pode fazer:  
            
            <li> Liste os preços da loja atacadão.  
            <li> Liste a loja onde o café é mais barato.  
            <li> Liste as minhas compras deste mês 📅.  
            <li> Qual foi a minha primeira compra?  
            <li> Liste todas as minhas compras.  
            <li> Sumarize minhas compras por mês e ano 🗓️.  
            <li> Quais foram as lojas que eu comprei neste mês?  
            <li> Quais produtos eu paguei mais barato e em que loja 💲🏬?  
            <li> Qual loja possui o menor preço do produto arroz?  
            <li> Liste os produtos e as lojas que possuem o menor preço.  
            <li> Liste 2 lojas que possuem o menor preço para o produto feijão.  
            <br>
            <br>
            Estou aqui para ajudá-lo a fazer compras inteligentes. Vamos começar? 🚀
        """
        # self.convo.send_message("Bom dia.")
        # response = self.__clean_json(self.convo.last.text)        
        # print(response)

        # objeto_json = json.loads(response)  

        # self.__refresh_data(objeto_json)

        # return self.response
        return welcome

    def send_message(self, question:str):

        self.convo.send_message(question)

        response = self.__clean_json(self.convo.last.text)        
        print(response)

        objeto_json = json.loads(response)
        self.__refresh_data(objeto_json)
        if( self.intent is None):
            return {
                "question": self.question,
                "response": self.response,
                "status": 200
            }            

        elif self.intent == "SQL":
            print(self.question)            
            if self.query is None or len(self.query) == 0:
                return {
                    "question": self.question,
                    "response": self.response,
                    "status": 200
                }
            print( self.question)

            result = self.__executeQuery(self.query)
            response = f"{self.response}\n```markdown\n{result}\n```"
            return {
                "question": self.question,
                "response": response,
                "status": 200
            }
        else:
            return {
                "question": self.question,
                "response": "Não encontrou informações para responder a sua pergunta!",
                "status": 200
            }