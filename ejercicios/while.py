while True:
    print("""
        Welcome.
        Elige una opción:
        1 - Mostrar productos
        2 - Mostrar un producto
        salir - salir del programa
        """)
    opcion = input("Introduce una opción: ")
    print(f"Has elegido la opcion {opcion}")
    if opcion == "salir":
        print("Hasta la proxima")
        break


print ("Fuera del bucle")