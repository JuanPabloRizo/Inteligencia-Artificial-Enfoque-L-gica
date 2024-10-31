# Definimos una clase para representar un conjunto de números
class ConjuntoNumeros:
    def __init__(self, numeros):
        # Inicializamos el conjunto de números
        self.numeros = numeros

    def cuantificador_universal(self, propiedad):
        # Evaluamos una propiedad para todos los números en el conjunto
        for numero in self.numeros:
            # Si alguna de las propiedades no se cumple, devolvemos False
            if not propiedad(numero):
                return False
        # Si todas las propiedades se cumplen, devolvemos True
        return True

    def cuantificador_existencial(self, propiedad):
        # Evaluamos si hay al menos un número en el conjunto que cumple la propiedad
        for numero in self.numeros:
            # Si encontramos un número que cumple la propiedad, devolvemos True
            if propiedad(numero):
                return True
        # Si no encontramos ningún número que cumpla la propiedad, devolvemos False
        return False

# Definimos una propiedad para los ejemplos
def es_par(x):
    # Verifica si un número es par
    return x % 2 == 0

def es_mayor_que_tres(x):
    # Verifica si un número es mayor que tres
    return x > 3

# Creamos un conjunto de números
conjunto = ConjuntoNumeros([1, 2, 3, 4, 5])

# Usamos el cuantificador universal para verificar si todos los números son pares
todos_pares = conjunto.cuantificador_universal(es_par)
print(f"¿Todos los números son pares? {todos_pares}")

# Usamos el cuantificador existencial para verificar si existe un número mayor que 3
existe_mayor_que_tres = conjunto.cuantificador_existencial(es_mayor_que_tres)
print(f"¿Hay algún número mayor que tres? {existe_mayor_que_tres}")
"""
Definición de la Clase ConjuntoNumeros:

Se crea una clase llamada ConjuntoNumeros que acepta una lista de números durante la inicialización.
self.numeros almacena los números en el objeto.
Método cuantificador_universal:

Este método toma una función propiedad como argumento, que se aplicará a cada número en el conjunto.
Recorre cada número en self.numeros y evalúa si cumple con la propiedad.
Si encuentra un número que no cumple la propiedad, devuelve False.
Si todos los números cumplen la propiedad, devuelve True.
Método cuantificador_existencial:

Similar al método anterior, pero en este caso busca al menos un número que cumpla con la propiedad.
Si encuentra al menos un número que cumple la propiedad, devuelve True.
Si no encuentra ninguno, devuelve False.
Funciones es_par y es_mayor_que_tres:

Estas funciones representan propiedades que se pueden evaluar en el conjunto de números.
es_par verifica si un número es par.
es_mayor_que_tres verifica si un número es mayor que tres.
Creación del Conjunto y Evaluación de Propiedades:

Se crea una instancia de ConjuntoNumeros con una lista de números del 1 al 5.
Se utiliza el cuantificador universal para verificar si todos los números son pares y se imprime el resultado.
Se utiliza el cuantificador existencial para verificar si existe algún número mayor que tres y se imprime el resultado.
"""