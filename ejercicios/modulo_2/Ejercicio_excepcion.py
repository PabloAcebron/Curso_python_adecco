from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

libros_db = [
    {"id": 1, "titulo": "El juego de ender", "autor": "Orson Scoot Card"},
    {"id": 2, "titulo": "el señor de los anillos", "autor": "Tolkien"}
]

@app.get("/libros/{libro_id}")
def obtener_libro(libro_id: int):
    for libro in libros_db:
        if libro["id"] == libro_id:
            return libro
    raise HTTPException(status_code=404, detail="404 - Libro no encontrado")