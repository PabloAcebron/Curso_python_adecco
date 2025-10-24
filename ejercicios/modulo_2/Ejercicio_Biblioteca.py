from fastapi import FastAPI

# Crear la instancia de la aplicación
app = FastAPI()

# Escribe aquí tu código para los endpoints GET

@app.get("/libros")
def obtener_libros():
    return {"libro1" : "El juego de Ender","libro2":"El Hobbit","libro3":"El señor de los anillos"}

@app.get("/biblioteca")
def obtener_biblioteca():
    return {"nombre" : "Rafael Alberti","total_libros": 300,"abierta": True}