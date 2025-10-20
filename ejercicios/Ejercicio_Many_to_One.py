print("=== EJERCICIO: RELACIÓN HABITACIONES-HOTEL ===\n")

# 1. Crear la clase Hotel con los atributos: id, nombre, direccion, estrellas
# El atributo 'habitaciones' debe inicializarse como una lista vacía
class Hotel:
    def __init__(self, id, nombre, direccion, estrellas):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.estrellas = estrellas
    

# 2. Crear la clase Habitacion con los atributos: id, numero, tipo, precio, hotel
class Habitacion:
    def __init__(self, id, numero, tipo, precio,hotel):
        self.id = id
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.hotel = hotel
        

print("=== CREANDO OBJETOS ===")

# 3. Crear un hotel con id: 1, nombre: Hotel Carbonero, dirección: Plaza Parus Mayor 123, estrellas: 4

hotel1 = Hotel( 1,"Hotel Carbonero","Plaza Parus Mayor 123",4)

# 4. Crear tres habitaciones:
# - id: 1, número: 101, tipo: Individual, precio: 80, id de hotel: 1
# - id: 2, número: 102, tipo: Doble, precio: 120, id de hotel: 1
# - id: 3, número: 103, tipo: Suite, precio: 200, id de hotel: 1

habitacion1 = Habitacion(1,101,"Individual",80,hotel1.nombre)
habitacion2 = Habitacion(2,102,"Doble",120,hotel1.nombre)
habitacion3 = Habitacion(3,103,"Suite",200,hotel1.nombre)






print("=== VERIFICANDO RELACIÓN ===")

# 6. Imprimir información del hotel y sus habitaciones
# Hay que mostrar:
# - Nombre del hotel y sus estrellas
# - Número total de habitaciones
# - Lista de habitaciones con sus detalles
# - Verificar que la relación es bidireccional

print(f"El hotel es: {hotel1.nombre} y las estrellas son: {hotel1.estrellas}")

print("\n=== RESULTADO FINAL ===")
# 7. Mostrar un mensaje confirmando la relación many-to-one

print(f"La habitacion es: {habitacion1.numero} al hotel: {hotel1.nombre}")