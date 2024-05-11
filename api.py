import uvicorn
from fastapi.responses import HTMLResponse  
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException
from create_database import CreateDatabase

app = FastAPI()

def build_application(app):
    uvicorn.run(
        app, host="127.0.0.1", port=8081, timeout_keep_alive=200
    )

@app.get("/", response_class=HTMLResponse)  
def read_root():
    try:
        CreateDatabase()
        return """  
        <html>  
            <head>  
                <title>ShopBot</title>  
            </head>  
            <body>  
                <h1>Olá como posso ajudar?</h1>  
            </body>  
        </html>  
        """  
    except HTTPException as err:
        raise HTTPException(status_code=400, detail=str(err))


if __name__ == "__main__":
    build_application(app)