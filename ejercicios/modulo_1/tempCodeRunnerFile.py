print("=== PROGRAMA: GENERADOR DE PATRÓN TRIANGULAR ===\n")

# Solicitar al usuario la altura del triángulo
# Escribe aquí tu código para pedir el número al usuario
altura = input("dime la altura del triangulo: ")

# Convertir la entrada a número entero
# Escribe aquí tu código para la conversión
altura = int(altura)

print(f"\nGenerando patrón triangular de altura {altura}:")
print("-" * 30)

# Generar el patrón usando bucles for anidados
# Bucle externo: para cada fila (desde 1 hasta la altura)
# Escribe aquí tu código para el bucle externo

for i in range (1,altura + 1):

    # Bucle interno: para cada número en la fila actual (desde 1 hasta el número de fila)
    # Escribe aquí tu código para el bucle interno
    for j in range (i,altura):
        # Imprimir cada número seguido de un espacio (sin salto de línea)
        # Escribe aquí tu código para imprimir el número
        print(range(1,j))
        

    # Después de completar una fila, hacer un salto de línea
    # Escribe aquí tu código para el salto de línea
    print()

print("-" * 30)
print("Patrón completado!")