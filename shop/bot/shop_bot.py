import os
import google.generativeai as genai

from typing import List

class ShopBot:

    STEP_WELCOME:str = "WELCOME"
    STEP_CHATBOT = "CHATBOT"
    STEP_FINISH= "FINISH"

    def __init__(self):

        genai.configure(api_key=os.getenv("GEMINI_TOKEN_KEY"))

        self.step:str = ShopBot.STEP_WELCOME 

        # Set up the model
        generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 0,
        "max_output_tokens": 8192,
        }

        safety_settings = [
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
                                    generation_config=generation_config,
                                    system_instruction=system_instruction,
                                    safety_settings=safety_settings)

        self.convo = self.model.start_chat(history=[])


    def welcome(self):

        self.convo.send_message("Bom dia.")
        print(self.convo.last.text)

