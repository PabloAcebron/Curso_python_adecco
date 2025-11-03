from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define aquí el modelo Libro

class Libro(BaseModel):
    titulo:str
    autor:str
    paginas:int

# Define aquí el endpoint POST

@app.post("/libros")
async def crear_libro(libro:Libro):
    descripcion = {
        "Titulo": libro.titulo,
        "Autor":libro.autor,
        "paginas":libro.paginas
    }
    return f"Has creado el libro {descripcion}"