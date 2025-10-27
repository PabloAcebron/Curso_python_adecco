from fastapi import FastAPI

# Crear la instancia de la aplicación

app = FastAPI()
# Escribe aquí tu código para los endpoints GET

@app.get("/animales")
def obtener_animales():
    return {
    "Animales": ["Tigre",
    "León",
    "Mapache",
    "Elefante"]
    }
    
@app.get("/zoologico")
def obtener_zoloogico():
    return {
    "Nombre": "Zoo de Pablo",
    "Cantidad_animales": 4,
    "Abierto": True,
    "Horario": "L-D 9:00-18:00"
    }
@app.get("/estadisticas")
def leer_estadisticas():

    return {
    "Informacion_general": {
    "Nombre": "Zoo de Pablo",
    "Ubicación": "Brazatortas"
    },
    "Datos_animales": {
    "Total_especies": 4,
    "Animales_populares": ["Mapache", "Elefante"]
    },
    "Estado_operacional": {
    "Abierto": True,
    "Empleados_presentes": 3
    }
    }