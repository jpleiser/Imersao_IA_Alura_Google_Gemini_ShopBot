import sqlite3  
import os  

def CreateDatabase():
    # Verifique se o arquivo de controle existe  
    if not os.path.exists('ShopBotInit.txt'):  
    
        # Conecte-se ao banco de dados SQLite (ou crie se não existir)  
        conn = sqlite3.connect('ShopBot.db')  
        c = conn.cursor()  
    
        # Abra o arquivo SQL e leia-o  
        with open('ShopBot.sql', 'r') as sql_file:  
            sql_commands = sql_file.read()  
    
        # Divida o arquivo em comandos individuais  
        sql_commands = sql_commands.split(';')  
    
        # Execute cada comando  
        for command in sql_commands:  
            try:  
                c.execute(command)  
            except sqlite3.OperationalError as e:  
                print('Comando pulado: ', e)  
    
        # Faça commit das mudanças  
        conn.commit()  
    
        # Feche a conexão  
        conn.close()  
    
        # Crie o arquivo de controle  
        with open('ShopBotInit.txt', 'w') as control_file:  
            control_file.write('Banco de dados carregado com sucesso')  
    
    else:  
        print('O banco de dados já foi carregado anteriormente')  
