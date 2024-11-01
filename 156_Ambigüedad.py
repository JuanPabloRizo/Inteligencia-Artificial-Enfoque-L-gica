class Ambiguedad:
    def __init__(self):
        self.frases = {
            "banco": ["entidad financiera", "lugar para sentarse"],
            "cerca": ["proximidad", "valla"],
            "vela": ["objeto que arde", "unidad de medida de la luz"],
        }

    def interpretar(self, palabra):
        """Interpreta una palabra ambigua y muestra sus significados."""
        if palabra in self.frases:
            print(f"La palabra '{palabra}' tiene los siguientes significados:")
            for significado in self.frases[palabra]:
                print(f"- {significado}")
        else:
            print(f"No se encontró ambigüedad para la palabra '{palabra}'.")

# Ejemplo de uso
amb = Ambiguedad()
palabras = ["banco", "cerca", "vela"]

for palabra in palabras:
    amb.interpretar(palabra)
"""
Manejo de la Ambigüedad
Para manejar la ambigüedad en sistemas de procesamiento de lenguaje natural y en inteligencia artificial, se pueden utilizar varias estrategias:

Desambiguación Léxica: Utilizar contexto adicional para determinar qué significado de una palabra es el correcto.

Gramáticas de Dependencia: Estas gramáticas ayudan a establecer relaciones claras entre las palabras en una oración, lo que puede reducir la ambigüedad sintáctica.

Modelos de Aprendizaje Automático: Entrenar modelos que puedan reconocer patrones y contextos para resolver ambigüedades de forma automática.
"""