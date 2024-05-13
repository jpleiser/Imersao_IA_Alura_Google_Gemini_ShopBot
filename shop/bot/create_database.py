import sqlite3  
import os  
import logging  

def CreateDatabase():
    # Verifique se o arquivo de controle existe  
    if not os.path.exists('./database/ShopBotInit.txt'):  
    
        # Conecte-se ao banco de dados SQLite (ou crie se não existir)  
        conn = sqlite3.connect('./database/ShopBot.db')  
        c = conn.cursor()  
    
        # Abra o arquivo SQL e leia-o  
        with open('./scripts/ShopBot.sql', 'r', encoding='utf-8') as sql_file:  
            sql_commands = sql_file.read()  
    
        # Divida o arquivo em comandos individuais  
        sql_commands = sql_commands.split(';')  

        # Configura o arquivo de log  
        logging.basicConfig(filename='start-database.log', level=logging.INFO)  
        
        # Execute cada comando    
        for command in sql_commands:    
            try:  
                # Grava o comando no log antes da execução  
                logging.info('Executando comando: %s' % command)  
                c.execute(command)    
            except sqlite3.OperationalError as e:    
                # Grava o erro no log se houver algum  
                logging.error('Erro ao executar comando: %s' % e)  
                print('Comando pulado: ', e)    

    
        # Faça commit das mudanças  
        conn.commit()  
    
        # Feche a conexão  
        conn.close()  
    
        # Crie o arquivo de controle  
        with open('./database/ShopBotInit.txt', 'w') as control_file:  
            control_file.write('Banco de dados carregado com sucesso')  
    
    else:  
        print('O banco de dados já foi carregado anteriormente')  
