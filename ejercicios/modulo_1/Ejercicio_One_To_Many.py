print("=== EJERCICIO: RELACIÓN CARPETA-ARCHIVOS ===\n")


class Carpeta:
    def __init__(self, id, nombre, fecha_creacion):
        self.id = id
        self.nombre = nombre
        self.fecha_creacion = fecha_creacion
        self.archivos = []
        


class Archivo:
    def __init__(self, id, nombre, extension, tamanyo, carpeta_id):
        self.id = id
        self.nombre = nombre
        self.extension = extension
        self.tamanyo = tamanyo
        self.carpeta_id = carpeta_id
        

print("=== CREANDO OBJETOS ===")



carpeta1 = Carpeta(1,"Proyecto Aviberico","2025-01-15")




archivo1 = Archivo(1,"main","py",1024,1)
archivo2 = Archivo(2,"config","json",512,1)
archivo3 = Archivo(3,"readme","pmd",256,1)

print("=== ESTABLECIENDO RELACIÓN ===")



carpeta1.archivos.append(archivo1)
carpeta1.archivos.append(archivo2)
carpeta1.archivos.append(archivo3)





print(f"Nombre de la carpeta: {carpeta1.nombre}")

print(f"Número total de archivos: {len(carpeta1.archivos)}")


for archivo in carpeta1.archivos: 
    print(f"ID: {archivo.id}, Nombre: {archivo.nombre}, Extensión: {archivo.extension}, Tamaño: {archivo.tamanyo}")



print("\n=== RESULTADO FINAL ===")

print(f"La lista de archivos es {len(carpeta1.archivos)}")