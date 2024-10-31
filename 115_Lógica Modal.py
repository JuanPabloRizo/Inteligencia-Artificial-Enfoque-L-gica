# Clase para representar un Mundo Posible
class MundoPosible:
    def __init__(self, nombre, proposiciones):
        self.nombre = nombre
        # Conjunto de proposiciones que son verdaderas en este mundo
        self.proposiciones = proposiciones

# Clase para representar un Modelo de Kripke
class ModeloKripke:
    def __init__(self):
        self.mundos = {}  # Diccionario de mundos posibles
        self.accesibilidad = {}  # Relación de accesibilidad entre mundos

    def agregar_mundo(self, mundo):
        # Agregar un mundo posible al modelo
        self.mundos[mundo.nombre] = mundo
        self.accesibilidad[mundo.nombre] = set()

    def agregar_accesibilidad(self, desde, hacia):
        # Definir que desde un mundo se puede acceder a otro
        self.accesibilidad[desde].add(hacia)

    def es_necesario(self, mundo, proposicion):
        # Evaluar si una proposición es necesaria (verdadera en todos los mundos accesibles)
        for accesible in self.accesibilidad[mundo]:
            if proposicion not in self.mundos[accesible].proposiciones:
                return False
        return True

    def es_posible(self, mundo, proposicion):
        # Evaluar si una proposición es posible (verdadera en al menos un mundo accesible)
        for accesible in self.accesibilidad[mundo]:
            if proposicion in self.mundos[accesible].proposiciones:
                return True
        return False

# Crear el modelo de Kripke
modelo = ModeloKripke()

# Definir mundos posibles con proposiciones verdaderas en ellos
mundo1 = MundoPosible("Mundo1", {"P"})  # En Mundo1, P es verdadero
mundo2 = MundoPosible("Mundo2", {"Q"})  # En Mundo2, Q es verdadero

# Agregar los mundos al modelo
modelo.agregar_mundo(mundo1)
modelo.agregar_mundo(mundo2)

# Definir accesibilidad entre los mundos
modelo.agregar_accesibilidad("Mundo1", "Mundo2")  # Desde Mundo1, se puede acceder a Mundo2

# Evaluar la necesidad y posibilidad de proposiciones
print(f"Es necesario que 'P' en Mundo1: {modelo.es_necesario('Mundo1', 'P')}")
print(f"Es posible que 'Q' en Mundo1: {modelo.es_posible('Mundo1', 'Q')}")
"""
Clase MundoPosible:

Representa un mundo posible en el sistema de lógica modal.
Cada mundo tiene un nombre y un conjunto de proposiciones que son verdaderas en ese mundo.
Clase ModeloKripke:

Esta clase representa el modelo de Kripke que contiene un conjunto de mundos y las relaciones de accesibilidad entre ellos.
Se utilizan dos métodos principales para evaluar la lógica modal:
es_necesario: Evalúa si una proposición es verdadera en todos los mundos accesibles desde un mundo dado (necesidad).
es_posible: Evalúa si una proposición es verdadera en al menos un mundo accesible desde un mundo dado (posibilidad).
Creación del Modelo de Kripke:

Se crean dos mundos posibles: Mundo1 donde P es verdadero y Mundo2 donde Q es verdadero.
Se define una relación de accesibilidad desde Mundo1 a Mundo2, lo que permite que en Mundo1 se pueda evaluar la posibilidad de Q en función de Mundo2.
Evaluación de Necesidad y Posibilidad:

El código evalúa si P es necesario en Mundo1 (es verdadero en todos los mundos accesibles desde Mundo1) y si Q es posible en Mundo1 (es verdadero en al menos un mundo accesible desde Mundo1).
"""