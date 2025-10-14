class Libro:

    def __init__(self,titulo,autor,numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.abierto = False
     
     
    def abrir(self):
        self.abierto = True
        print(f"Se ha abierto: {self.titulo}")
        
    def cerrar(self):
        self.abierto = False
        print(f"Se ha cerrado: {self.titulo}")
        
libro1 = Libro("El hobbit", "Tolkien", 1500)
libro2 = Libro("El juego de Ender","Orson Scott Card",376)


class Producto:
    
    def __init__(self,nombre,precio,stock=0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

laptop = Producto("Portatil",200,20)

# crear clase Rectangulo
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.area = ancho * alto
        self.perimetro = 2 * (ancho + alto)

# crear objeto rectángulo
rectangulo = Rectangulo(5, 3)
print(rectangulo.area)
print(rectangulo.perimetro)

# clase Cuenta bancaria
class Cuenta:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo_inicial = saldo_inicial

# validación para que el saldo inicial sea como mínimo 0 (que no sea negativo)
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo")

        self.saldo = saldo_inicial

# crear objetos cuenta
cuenta_ana = Cuenta("Ana", 1000)

# esto lanzará un ValueError
try:
    cuenta_problematica = Cuenta("Juan", -500)
except ValueError as e:
    print(f"ERROR: {e}")
