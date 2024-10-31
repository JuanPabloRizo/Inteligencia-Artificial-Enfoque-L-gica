def es_seguro(tablero, fila, col):
    # Comprobar si es seguro colocar una reina en la posición (fila, col).
    
    # Comprobar la fila en la parte izquierda
    for i in range(col):
        if tablero[fila][i] == 1:  # Si hay una reina en esta fila, retornar False
            return False
    
    # Comprobar la diagonal superior izquierda
    for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
        if tablero[i][j] == 1:  # Si hay una reina en esta diagonal, retornar False
            return False
    
    # Comprobar la diagonal inferior izquierda
    for i, j in zip(range(fila, len(tablero)), range(col, -1, -1)):
        if tablero[i][j] == 1:  # Si hay una reina en esta diagonal, retornar False
            return False
    
    return True  # Si no hay conflictos, es seguro colocar la reina


def resolver_n_reinas(tablero, col):
    # Función recursiva para resolver el problema de N-Reinas.
    
    if col >= len(tablero):  # Si todas las reinas están colocadas, retornar True
        return True

    for i in range(len(tablero)):  # Intentar colocar una reina en cada fila
        if es_seguro(tablero, i, col):  # Verificar si es seguro colocar en (i, col)
            tablero[i][col] = 1  # Colocar la reina

            # Recursivamente intentar colocar reinas en la siguiente columna
            if resolver_n_reinas(tablero, col + 1):
                return True  # Si se logra, retornar True

            # Si no se logra, quitar la reina (Backtracking)
            tablero[i][col] = 0  # Deshacer la colocación

    return False  # Si no se puede colocar una reina en esta columna, retornar False


def imprimir_tablero(tablero):
    # Función para imprimir el tablero.
    
    for fila in tablero:
        print(" ".join("Q" if x else "." for x in fila))  # Imprimir reinas y espacios vacíos
    print()  # Espacio en blanco entre soluciones


def resolver(n):
    # Función principal para resolver el problema de N-Reinas.
    
    tablero = [[0] * n for _ in range(n)]  # Crear un tablero vacío

    if not resolver_n_reinas(tablero, 0):  # Intentar resolver
        print("No se puede encontrar una solución para N =", n)
        return

    imprimir_tablero(tablero)  # Imprimir la solución encontrada


# Ejecutar la función para resolver el problema de N-Reinas
resolver(4)  # Cambiar el número aquí para resolver diferentes tamaños
"""
Función es_seguro(tablero, fila, col):

Esta función verifica si es seguro colocar una reina en la posición dada del tablero.
Comprueba las filas y las diagonales para asegurarse de que no haya otras reinas que puedan atacar a la nueva reina.
Función resolver_n_reinas(tablero, col):

Esta función es el núcleo del algoritmo de Backtracking.
Intenta colocar una reina en cada fila de la columna actual.
Si es seguro colocar una reina, la coloca y hace una llamada recursiva para la siguiente columna.
Si no se puede encontrar una solución, quita la reina (Backtracking) y prueba la siguiente fila.
Función imprimir_tablero(tablero):

Esta función se encarga de imprimir el tablero de forma legible.
Muestra "Q" para las posiciones con reinas y "." para los espacios vacíos.
Función resolver(n):

Esta es la función principal que inicializa el tablero y llama a la función de resolución.
Si no se puede encontrar una solución, informa al usuario.
Ejecutar resolver(4):

Aquí es donde se inicia el proceso. Se puede cambiar el número para resolver diferentes tamaños de tableros.
"""