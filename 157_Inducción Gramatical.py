import random

class InduccionGramatical:
    def __init__(self):
        # Almacena las reglas gramaticales aprendidas
        self.gramatica = {}

    def aprender(self, ejemplos):
        """Aprender reglas gramaticales a partir de ejemplos."""
        for ejemplo in ejemplos:
            palabras = ejemplo.split()  # Separar las palabras del ejemplo
            for i in range(len(palabras) - 1):
                # Crear una regla que conecta palabras adyacentes
                if palabras[i] not in self.gramatica:
                    self.gramatica[palabras[i]] = []
                self.gramatica[palabras[i]].append(palabras[i + 1])

    def generar(self, palabra_inicial, longitud=5):
        """Generar una cadena de texto a partir de la gramática aprendida."""
        if palabra_inicial not in self.gramatica:
            return "Palabra inicial no encontrada en la gramática."
        
        cadena = [palabra_inicial]
        for _ in range(longitud - 1):
            # Verificar si la última palabra de la cadena tiene continuaciones
            if cadena[-1] in self.gramatica:
                siguiente_palabra = random.choice(self.gramatica[cadena[-1]])  # Elegir una palabra siguiente al azar
                cadena.append(siguiente_palabra)
            else:
                break  # Salir si no hay más palabras que añadir

        return ' '.join(cadena)

# Ejemplo de uso
if __name__ == "__main__":
    ejemplos = [
        "el gato come pescado",
        "el perro ladra",
        "la vaca da leche",
        "el gato juega",
        "el perro corre rápido"
    ]
    
    # Crear una instancia de la clase
    inductora = InduccionGramatical()
    
    # Aprender de los ejemplos
    inductora.aprender(ejemplos)
    
    # Generar una nueva cadena a partir de una palabra inicial
    palabra_inicial = "el"
    nueva_cadena = inductora.generar(palabra_inicial)
    print(f"Cadenas generadas a partir de la palabra '{palabra_inicial}':")
    print(nueva_cadena)

"""
Clase InduccionGramatical: Define una clase para manejar la inducción gramatical.

Método __init__: Inicializa la estructura que almacenará las reglas gramaticales.

Método aprender:

Toma ejemplos de cadenas de texto.
Separa cada ejemplo en palabras.
Crea reglas que conectan palabras adyacentes, almacenando en un diccionario.
Método generar:

Genera una nueva cadena de texto comenzando desde una palabra inicial.
Utiliza las reglas aprendidas para elegir aleatoriamente la siguiente palabra.
Ejemplo de uso:

Se proporcionan ejemplos de frases para aprender.
Se genera una nueva cadena a partir de una palabra inicial.
"""