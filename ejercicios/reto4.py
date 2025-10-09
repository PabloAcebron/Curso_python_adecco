
edad = input("Dime la edad del usuario")

edad = int(edad)

if edad < 13:
    print("Eres un niño")
elif edad >= 13 and  edad <= 17:
    print("Eres un adolescente")
elif edad >= 18 and edad <= 64:
    print("Eres un adulto")
elif edad >=65:
    print("Eres un adulto mayor")
else:
    print("Error en la edad")