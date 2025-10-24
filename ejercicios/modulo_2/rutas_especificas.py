from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def leer_ruta_raiz():
    return {"mensaje" : "Esto es la raiz"}

@app.get("/productos")
def obtener_productos():
    return {"productos" : ["leche","queso","manzana"]}

@app.get("/usuarios")
def leer_usuarios():
    return {"usuarios" : ["Pablo","Paco","Pedro"]}