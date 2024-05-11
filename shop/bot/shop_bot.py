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

        system_instruction = "Você é um assistente pessoal atencioso especializado em banco de dados relacional com profundamente conhecimento em PNL. \n  \nComo assistente pessoal, você deverá retornar a estrutura do exemplo 1.\nExemplo 1:\n```json  \n{\n     \"question\": \"question name\",  \n     \"response\": \"response name\"  \n}  \n```\n\n\nComo especialista em banco de dados relacional você deverá analisar o esquema de dados definido abaixo e gerar comandos SQL para executar consultas no banco de dados e deverá retornar a estrutura de exemplo 2:\n&Exemplo 2:\n```json   \n{  \n     \"intent\": \"SQL\",  \n     \"question\": \"question name\",  \n     \"response\": \"response name\",  \n     \"query\": \"command sql\"  \n}\n```\n```sql\nCREATE TABLE loja (\n  codigo INTEGER PRIMARY KEY,\n  nome TEXT NOT NULL,\n  endereco TEXT,\n  cidade TEXT,\n  estado TEXT\n);\n\nCREATE TABLE produto (\n  codigo INTEGER PRIMARY KEY,\n  descricao TEXT NOT NULL,\n  categoria TEXT,\n  unidade_medida TEXT\n);\n\nCREATE TABLE preco_do_produto_na_loja (\n  loja_codigo INTEGER,\n  produto_codigo INTEGER,\n  preco REAL NOT NULL,\n  PRIMARY KEY (loja_codigo, produto_codigo),\n  FOREIGN KEY (loja_codigo) REFERENCES loja (codigo),\n  FOREIGN KEY (produto_codigo) REFERENCES produto (codigo)\n);\n\nCREATE TABLE lista_de_compras (\n  id INTEGER PRIMARY KEY AUTOINCREMENT,\n  quantidade DECIMAL(10, 4) NOT NULL,\n  preco_unitario REAL NOT NULL,\n  valor_compra REAL NOT NULL,\n  data_compra DATE NOT NULL,\n  loja_codigo INTEGER,\n  produto_codigo INTEGER,\n  FOREIGN KEY (loja_codigo) REFERENCES loja (codigo),\n  FOREIGN KEY (produto_codigo) REFERENCES produto (codigo)\n);\n```"

        self.model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                    generation_config=self.generation_config,
                                    system_instruction=system_instruction,
                                    safety_settings=self.safety_settings)

        self.convo = self.model.start_chat(history=[])

    
    def __send_message_rag(self,question:str):
        
        system_instruction_rag = "Você é um asssitente atencioso e sabe responder de forma educada a pergunta do usuário."

        model_rag = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                    generation_config=self.generation_config,
                                    system_instruction=system_instruction_rag,
                                    safety_settings=self.safety_settings)

        convo = model_rag.start_chat(history=[])
        convo.send_message(question)
        
        print(convo.last.text)

        return convo.last.text


    def __clean_json(self, json_text:str) -> str:
        json_text = json_text.replace("```json", "")
        json_text = json_text.replace("```","")
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
                    
            except sqlite3.OperationalError as e:   
                print(f"An error occurred: {e}")

        if len(markdown_result) == 0:
            markdown_result = None

        return markdown_result  


    def welcome(self):

        self.convo.send_message("Bom dia.")
        response = self.__clean_json(self.convo.last.text)        
        print(response)

        objeto_json = json.loads(response)  

        self.__refresh_data(objeto_json)

        if( self.intent is None):     
            return self.response
        elif self.intent == "SQL":
            pass
        else:
            return  


    def send_message(self, question:str):

        self.convo.send_message(question)

        response = self.__clean_json(self.convo.last.text)        
        print(response)

        objeto_json = json.loads(response)
        self.__refresh_data(objeto_json)
        if( self.intent is None):
            resulte = self.__executeQuery(self.query)
            return {
                "question": self.question,
                "response": self.response,
                "status": 200
            }            

        elif self.intent == "SQL":
            resulte = self.__executeQuery(self.query)
            return {
                "question": self.question,
                "response": self.__send_message_rag(f"{question}\n Dados:\n{resulte}"),
                "status": 200
            }
        else:
            return {
                "question": self.question,
                "response": "Não encontrou informações para responder a sua pergunta!",
                "status": 200
            }