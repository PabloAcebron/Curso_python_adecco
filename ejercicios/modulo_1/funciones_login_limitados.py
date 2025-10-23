import sys
VALID_EMAIL="admin@empresa.com"
VALID_PASS="admin"
MAX_INTENTOS = 3

def login():
    
    for intento in range(1,MAX_INTENTOS +1):
        email = input("introduce email: ").strip()
        password = input("introduce password: ").strip()
        
        if email == VALID_EMAIL and password == VALID_PASS:
            return True
        intentos_restantes = MAX_INTENTOS - intento 
        if intentos_restantes > 0:
            print(f"Te quedan: {intentos_restantes} intentos")
        else:
            print(f"Te has quedado sin intentos")
            sys.exit(1)
    


def elegir_opcion():
    print("")
    input()
    return opcion
    
if login():
    while True:
        print("Bienvenido a la aplicación, Opciones disponibles : 1 - Ver productos, 2 - Crear producto, 3 - Salir ")
        opcion = input("Introduce la opcion ")
        print(f"Has elegido la opción: {opcion}")
        if opcion == "1":
            print("Puedes ver productos")
        elif opcion == "2":
            print("Puedes crear productos")
        elif opcion == "3":
            print("Has salido de la app")
            break
        else:
            print("opcion incorrecta")