from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Optional, List

# Crear la instancia de la aplicación
app = FastAPI()

# Escribe aquí tu código para los modelos Pydantic y los endpoints

class Contacto(BaseModel):
    telefono: str
    email: Optional[str] = None
    activo: bool

# modelo con campos opcionales y valores por defecto
class Paciente(BaseModel):
    nombre: str
    apellido: str
    edad: int
    contacto: Contacto
    alergias: List[str] = []
    activo: bool = True
   
   

pacientes_db: List[Paciente] = [
    Paciente(nombre="Pablo", apellido="Acebron",edad=34,contacto="913647362",alergias=["Algas","Example1@mail.com",True],activo=True),
    Paciente(nombre="Pedro", apellido="Ropero",edad= 34,contacto="916454362",alergias=["Manzanas","Example2@mail.com",False],activo=True),
    Paciente(nombre="Ana", apellido="Herranz",edad= 35,contacto="913297362",alergias=["Queso","Example3@mail.com",True],activo=False)   
  ] 
 
pacientes_count = 0  
  
@app.post("/pacientes", response_model=Paciente, status_code=201)
def crear_paciente(paciente: Paciente):
    pacientes_db.append(paciente)
    return paciente

@app.get("/pacientes", response_model=List[Paciente])
def listar_pacientes():
    return pacientes_db

@app.get("/pacientes/{pacientes_id}", response_model=Paciente)
def obtener_paciente(pacientes_id: int):
    for p in pacientes_db:
        if p.id == pacientes_id:
            return p
    raise HTTPException(status_code=404, detail="Paciente no encontrado")

@app.get("/pacientes/activos", response_model=Paciente)
def obtener_paciente_activos(pacientes_id: int):
    for p in pacientes_db:
        if p.activo == pacientes_id:
            return p
    raise HTTPException(status_code=404, detail="Paciente no encontrado")