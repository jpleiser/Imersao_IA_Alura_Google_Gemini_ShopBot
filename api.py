import uuid
import uvicorn
from pydantic import BaseModel
from typing import Dict
from fastapi import FastAPI, HTTPException, Response, Request
from fastapi.responses import HTMLResponse, JSONResponse 
from fastapi.middleware.cors import CORSMiddleware  

from shop.bot.create_database import CreateDatabase
from shop.bot.shop_bot import ShopBot
  
app = FastAPI()

app.add_middleware(  
    CORSMiddleware,  
    allow_origins=["*"],  
    allow_credentials=True,  
    allow_methods=["*"],  
    allow_headers=["*"],  
    expose_headers=["user-session"]  
)  

sessions:Dict[str, ShopBot] = {} 

def build_application(app):
    uvicorn.run(
        app, host="127.0.0.1", port=8081, timeout_keep_alive=200
    )

def open_file_utf8(filename):  
    with open(filename, 'r', encoding='utf-8') as file:  
        content = file.read()  
    return content  

@app.get("/", response_class=HTMLResponse)  
def read_root(request: Request, response: Response):
    try:
        # Para retornar uma informação no cabeçalho
        CreateDatabase() # supondo que esta função exista
        return HTMLResponse(content=open_file_utf8("./resource/index.html"))  
    except HTTPException as err:  
        raise HTTPException(status_code=400, detail=str(err))


@app.get("/api/welcome", response_class=HTMLResponse)    
def read_root(request: Request, response: Response):  
    try:  
        response = None
        shop_bot:ShopBot = None  
        # Verificando se o usuário já possui uma sessão ativa      
        session_id = request.headers.get('user-session', None)      
        if session_id is None:   
            session_id = str(uuid.uuid4())    
            shop_bot = ShopBot()    
            sessions[session_id] = shop_bot  
            response = shop_bot.welcome()    
        else:    
            shop_bot = sessions.get(session_id, None)      
        if shop_bot is None:  
            raise HTTPException(status_code=400, detail="Invalid session id")  
  
        return JSONResponse(  
            content={
                "question": "WELCOME",
                "response": response,
                "status": 200  
            },  
            headers={"user-session": session_id}  
        )  
              
    except HTTPException as err:    
        raise HTTPException(status_code=400, detail=str(err))  
    except Exception as e:  
        raise HTTPException(status_code=500, detail=str(e))  


class Message(BaseModel):  
    message: str  
  
@app.post("/api/send-message")    
async def send_message(request: Request, message: Message):    
    try:    
        session_id = request.headers.get('user-session', None)    
        if session_id is not None:    
            shop_bot = sessions.get(session_id, None)    
            if shop_bot is not None: 
                response = shop_bot.send_message(message.message)    
                return JSONResponse(content=response)    
            else:    
                raise HTTPException(status_code=400, detail="Sessão não encontrada")    
        else:    
            raise HTTPException(status_code=400, detail="Id de sessão não encontrado")    
    
    except HTTPException as err:    
        raise HTTPException(status_code=400, detail=str(err))    
 

if __name__ == "__main__":
    build_application(app)
    