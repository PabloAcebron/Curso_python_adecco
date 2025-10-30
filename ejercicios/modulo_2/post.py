from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# modelo básico
class Usuario(BaseModel):
    nombre: str
    edad: int
    activo: bool

# modelo con campos opcionales y valores por defecto
class Producto(BaseModel):
    nombre: str
    precio: float
    categoria: str
    descripcion: Optional[str] = None
    disponible: bool = True


@app.post("/productos")
def crear_producto(producto: Producto):
    return {
    "Mensaje":f"Producto {producto.nombre} registrado con éxito con precio {producto.precio}€"
    }