from fastapi import FastAPI
from pydantic import BaseModel 

app = FastAPI()

@app.get("/users")
async def users():
    return [{"name": "Brais", "surname":"Moure", "url":"https://moure.dev"},
            {"name": "Saul", "surname":"Bigboss", "url":"https://moure.com"},
            {"name": "Cahnchito", "surname":"Feliz", "url":"https://chanchito.com"}]