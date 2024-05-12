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

            - Como especialista em banco de dados relacional você deverá analisar o esquema de dados definido abaixo e gerar comandos SQL para executar consultas no banco de dados e deverá retornar a estrutura de exemplo 2:
            **&Exemplo 2:**
            ```json
            {
                "intent": "SQL",
                "question": "question name",
                "response": "response name", 
                "query": "command sql"
            }
            ```

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

        self.convo.send_message("Bom dia.")
        response = self.__clean_json(self.convo.last.text)        
        print(response)

        objeto_json = json.loads(response)  

        self.__refresh_data(objeto_json)

        return self.response


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
            result = self.__executeQuery(self.query)
            response = f"{self.response}\n```markdown\n{result}\n```"
            print(response)
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