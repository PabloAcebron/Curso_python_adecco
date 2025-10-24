# importamos fastapi

from fastapi import FastAPI


# creamos la instacia, solo se hace una vez

app = FastAPI()

# creamos la ruta raiz

@app.get("/")
def leer_raiz():
    return {"mensaje" : "Hola desde la ruta raiz"}

@app.get("/inicio")
def obtener_informacion():
    return {"mensaje" : "Esto es el inicio de la web", "Autor" : "Pablo Acebrón"}