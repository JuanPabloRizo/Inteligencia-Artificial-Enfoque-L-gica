import random
import numpy as np

def calcular_distancia(ruta, distancias):
    # Calcula la distancia total de la ruta dada
    distancia_total = 0
    for i in range(len(ruta) - 1):
        distancia_total += distancias[ruta[i]][ruta[i + 1]]
    # Añadir la distancia de vuelta al punto de partida
    distancia_total += distancias[ruta[-1]][ruta[0]]
    return distancia_total

def generar_vecino(ruta):
    # Genera un vecino intercambiando dos ciudades en la ruta
    vecino = ruta.copy()
    i, j = random.sample(range(len(vecino)), 2)  # Escoger dos índices aleatorios
    vecino[i], vecino[j] = vecino[j], vecino[i]  # Intercambiar las ciudades
    return vecino

def busqueda_local(distancias, max_iter=1000):
    # Inicializa una ruta aleatoria
    num_ciudades = len(distancias)
    ruta_actual = list(range(num_ciudades))
    random.shuffle(ruta_actual)
    
    mejor_distancia = calcular_distancia(ruta_actual, distancias)
    
    for _ in range(max_iter):
        vecino = generar_vecino(ruta_actual)
        distancia_vecino = calcular_distancia(vecino, distancias)
        
        # Si el vecino es mejor, se actualiza la ruta actual
        if distancia_vecino < mejor_distancia:
            ruta_actual = vecino
            mejor_distancia = distancia_vecino
            
    return ruta_actual, mejor_distancia

if __name__ == "__main__":
    # Ejemplo de matriz de distancias entre ciudades
    distancias = np.array([[0, 10, 15, 20],
                           [10, 0, 35, 25],
                           [15, 35, 0, 30],
                           [20, 25, 30, 0]])
    
    ruta_optima, distancia_total = busqueda_local(distancias)
    
    print("Ruta óptima encontrada:", ruta_optima)
    print("Distancia total:", distancia_total)
    """
    Imports:

import random: Se importa para generar números aleatorios.
import numpy as np: Se importa para trabajar con matrices de distancias.
Función calcular_distancia:

Esta función toma una ruta (lista de ciudades) y una matriz de distancias.
Calcula la distancia total de la ruta sumando las distancias entre ciudades adyacentes.
Al final, también suma la distancia de regreso al punto de partida.
Función generar_vecino:

Genera un "vecino" de la ruta actual intercambiando dos ciudades.
Usa random.sample para seleccionar dos índices aleatorios de la lista de ciudades y las intercambia.
Función busqueda_local:

Inicializa una ruta aleatoria y calcula su distancia.
En un bucle que se ejecuta max_iter veces:
Genera un vecino de la ruta actual.
Calcula la distancia del vecino.
Si el vecino es mejor (menor distancia), actualiza la ruta actual y la mejor distancia encontrada.
Bloque if __name__ == "__main__":

Define una matriz de distancias entre cuatro ciudades.
Llama a la función busqueda_local para encontrar la ruta óptima.
Imprime la ruta óptima y la distancia total.
    """