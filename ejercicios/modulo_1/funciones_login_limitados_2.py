import sys

VALID_EMAIL = "user@gmail.com"
VALID_PASSWORD = "pass1234"

def login():
    # bucle for para máximo 3 intentos fallidos
    for intento in range(1,4):
        user_email = input("Introduce tu mail: ")
        user_pass = input("Introduce tu contraseña: ")

        if user_email == VALID_EMAIL and user_pass == VALID_PASSWORD:
            return True
        else:
            print(f"Datos incorrectos llevas {intento} /3 ")


    print("Has excedido los intentos, saliedo...")
    sys.exit(1) # para salir del

login()