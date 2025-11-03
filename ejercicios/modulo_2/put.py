from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

usuarios_db = [
    {"id": 1, "nombre": "Grajilla", "email": "grajilla@aves.com"},
    {"id": 2, "nombre": "Rabilargo", "email": "rabilargo@aves.com"}
]

class Usuario(BaseModel):
    nombre: str
    email: str
    edad: int
    
class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[str] = None
    edad: Optional[int] = None

@app.get("/usuarios")
def obtener_usuarios():
    return usuarios_db