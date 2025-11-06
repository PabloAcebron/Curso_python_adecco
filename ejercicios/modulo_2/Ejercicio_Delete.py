from fastapi import FastAPI, HTTPException

app = FastAPI()

# Define aquí la lista de libros

libros = [
       {"id": 1, "titulo": "El Quijote", "autor": "Cervantes"},
       {"id": 2, "titulo": "Cien años de soledad", "autor": "García Márquez"},
       {"id": 3, "titulo": "1984", "autor": "Orwell"}
   ]



# Implementa aquí el endpoint DELETE

@app.delete("/libros/{libro_id}")
def eliminar_libros(libro_id: int):
    for i, libro in enumerate(libros):
        if libro["id"] == libro_id:
            libro_eliminado = libros.pop(i)
            return {"mensaje": f"Libro eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Libro no encontrado")