class EstadoNReinas:
    def __init__(self, tamaño, reinas=None):
        """
        Inicializa un estado del problema N-reinas.
        :param tamaño: Tamaño del tablero (NxN).
        :param reinas: Lista de posiciones de las reinas en el tablero.
        """
        self.tamaño = tamaño
        self.reinas = reinas if reinas is not None else []

    def es_valido(self):
        """
        Verifica si el estado actual es válido (no hay reinas que se ataquen entre sí).
        :return: True si es válido, False en caso contrario.
        """
        for i in range(len(self.reinas)):
            for j in range(i + 1, len(self.reinas)):
                # Verificar si dos reinas están en la misma fila o diagonal
                if self.reinas[i] == self.reinas[j] or abs(self.reinas[i] - self.reinas[j]) == j - i:
                    return False
        return True

    def generar_sucesores(self):
        """
        Genera todos los sucesores del estado actual.
        :return: Lista de estados sucesores.
        """
        sucesores = []
        for columna in range(self.tamaño):
            nuevo_estado = EstadoNReinas(self.tamaño, self.reinas + [columna])
            if nuevo_estado.es_valido():
                sucesores.append(nuevo_estado)
        return sucesores

def buscar_solucion(tamaño):
    """
    Busca una solución para el problema de N-reinas utilizando búsqueda en el espacio de estados.
    :param tamaño: Tamaño del tablero (NxN).
    :return: Estado que representa la solución o None si no hay solución.
    """
    estado_inicial = EstadoNReinas(tamaño)
    pila = [estado_inicial]  # Usamos una pila para la búsqueda en profundidad

    while pila:
        estado_actual = pila.pop()
        if len(estado_actual.reinas) == tamaño:  # Se ha colocado N reinas
            return estado_actual
        sucesores = estado_actual.generar_sucesores()
        for sucesor in sucesores:
            pila.append(sucesor)

    return None  # No se encontró solución

# Ejemplo de uso
if __name__ == "__main__":
    tamaño = 4  # Problema de 4 reinas
    solucion = buscar_solucion(tamaño)

    if solucion:
        print("Solución encontrada:")
        for i, reina in enumerate(solucion.reinas):
            print(f"Reina en fila {i}, columna {reina}")
    else:
        print("No se encontró solución.")
"""
Clase EstadoNReinas:

Esta clase representa un estado del problema de N-reinas.
Método __init__: Inicializa el tamaño del tablero y la lista de posiciones de las reinas.
Método es_valido: Verifica si el estado actual es válido. Asegura que ninguna de las reinas se ataque entre sí.
Método generar_sucesores: Crea nuevos estados al intentar colocar una nueva reina en cada columna del tablero, y agrega el nuevo estado a la lista de sucesores si es válido.
Función buscar_solucion:

Esta función utiliza búsqueda en profundidad para encontrar una solución al problema de N-reinas.
Estado inicial: Crea un estado inicial vacío y lo coloca en una pila.
Bucle de búsqueda: Mientras haya estados en la pila, extrae uno y verifica si se han colocado todas las reinas.
Generación de sucesores: Genera todos los sucesores válidos del estado actual y los añade a la pila para ser procesados.
Ejemplo de uso:

Se establece un tamaño para el tablero (en este caso, 4).
Se llama a buscar_solucion para encontrar una solución y se imprimen las posiciones de las reinas si se encuentra.
"""