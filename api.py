import uuid
import uvicorn
from typing import Dict
from fastapi import FastAPI, HTTPException, Response, Request
from fastapi.responses import HTMLResponse  

from shop.bot.create_database import CreateDatabase
from shop.bot.shop_bot import ShopBot

app = FastAPI()

sessions:Dict[str, ShopBot] = {} 

def build_application(app):
    uvicorn.run(
        app, host="127.0.0.1", port=8081, timeout_keep_alive=200
    )

@app.get("/", response_class=HTMLResponse)  
def read_root(request: Request, response: Response):  
    try:
        # Verificando se o usuário já possui uma sessão ativa  
        header_value = request.headers.get('user-session')  
        if header_value is None:
            session_id = uuid.uuid4()
            shop_bot = ShopBot()
            sessions[session_id] = shop_bot
        else:
            # Para retornar uma informação no cabeçalho  
            response.headers['Custom-Header'] = 'Some value'        
            CreateDatabase() # supondo que esta função exista  
            return """
            <html>
                <head> 
                    <title>ShopBot</title> 
                </head> 
                <body>  
                    <h1>Olá como posso ajudar?</h1>   
                </body>    
            </html>"""    
    except HTTPException as err:
        raise HTTPException(status_code=400, detail=str(err))


if __name__ == "__main__":
    build_application(app)