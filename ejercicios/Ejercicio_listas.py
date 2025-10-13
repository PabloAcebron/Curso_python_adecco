def filtrar_mayores(lista, umbral):
    """
    Filtra los números de una lista que son mayores que un valor umbral dado.
    
    Args:
        lista (list): Lista de números enteros a filtrar.
        umbral (int): Valor umbral para la comparación.
        
        
        
    Returns:
        list: Nueva lista con los números mayores que el umbral.
    """
    
    lista = list(lista)
    
    umbral = int(umbral)
    
    resultado = []
    
    # TODO: haz aquí el código de la función:
    
    for num in lista:
        if num > umbral:
            resultado.append(num)
    return resultado

# Ejemplos de uso
if __name__ == "__main__":
    print(filtrar_mayores([5, 10, 15, 20], 12))  # Debe devolver [15, 20]
    print(filtrar_mayores([1, 2, 3], 5))         # Debe devolver [] (lista vacía)