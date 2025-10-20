
# Relacion One to One

class Ciudadano:
    def __init__(self,id,nombre,apellido,edad):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = None



class DNI:
    def __init__(self,id,dni):
        self.id = id
        self.dni = dni

        
ciudadano1 = Ciudadano (345,"Pablo","Acebron",34)

dni1 = DNI ("45654324-J")


ciudadano1.dni = dni1


ciudadano2 = Ciudadano (564,"Asunción","Acebron",40)

dni2 = DNI ("45387972-Y")


ciudadano2.dni = dni2

# Relacion Many to One

class Departamento:
    def __init__(self,id,nombre,documentacion):
        self.id = id
        self.nombre = nombre
        self.documentacion = documentacion
        
class Profesor:
    def __init__(self,id,nombre,especialidad,departamento):
        self.id = id
        self.nombre = nombre
        self.especialidad = especialidad
        self.departamento = departamento


departamento1 = Departamento(1,"Matematicas","Edificioa1")


profesor1 = Profesor(1,"Antonio","Topologia",departamento1)

profesor2 = Profesor(2,"Pepito","Cálculo",departamento1)


# Relacion One to Many

class Categoria:
    def __init__(self,id,nombre,descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.productos = []

class Producto:
    def __init__(self,id,nombre,precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        
        
categoria1 = Categoria(463,"Lácteos","Productos derivados de la leche")

categoria2 = Categoria(635, "Frutas","Productos frescos")

producto1 = Producto(1,"Leche",1.00)
producto2 = Producto(1,"Queso",3.00)
producto3 = Producto(1,"Yogurt",2.00)

producto4 = Producto(4,"Naranja",0.75)

categoria1.productos.append(producto1)
categoria1.productos.append(producto2)
categoria1.productos.append(producto3)

categoria2.productos.append(producto4)


# Many to Many

class Estudiante:
    def __init__(self,id,nombre,edad):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.asignaturas = []
        
class Asignatura:
    def __init__(self,id,nombre,creditos):
        self.id = id
        self.nombre = nombre
        self.creditos = creditos
        self.estudiantes = []

class EstudianteAsigantura:
    def __init__(self, estudiante_id,asignatura_id,nota):
        self.estudiante_id = estudiante_id
        self.asignatura_id = asignatura_id
        self.nota = nota
        
        
estudiante1 = Estudiante(1,"Ana",22)
estudiante2 = Estudiante(2,"Pepe",24)

asignatura1 = Asignatura(1,"Matematicas",6)
asignatura2 = Asignatura(2,"Psicologia",7)

estudiante1.asignaturas = [asignatura1,asignatura2]
estudiante2.asignaturas = [asignatura1]

asignatura1.estudiantes = [estudiante1,estudiante2]
asignatura1.estudiantes = [estudiante1,]

relaciones = [ 
      
      EstudianteAsigantura(1,1,8.5),
      EstudianteAsigantura(1,2,6.0),
      EstudianteAsigantura(2,1,7.5),
               
              
              ]