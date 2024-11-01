import random

class Grammar:
    def __init__(self, rules):
        """Inicializa la gramática con un conjunto de reglas.
        
        Args:
            rules (dict): Un diccionario donde las claves son no terminales
                          y los valores son listas de producciones.
        """
        self.rules = rules

    def generate(self, start_symbol):
        """Genera una cadena a partir del símbolo inicial.
        
        Args:
            start_symbol (str): El símbolo inicial de la gramática.
        
        Returns:
            str: La cadena generada.
        """
        # Inicializa la cadena con el símbolo inicial
        result = start_symbol
        # Mientras haya no terminales en la cadena, seguir generando
        while any(symbol in self.rules for symbol in result):
            # Selecciona un símbolo no terminal
            for i, symbol in enumerate(result):
                if symbol in self.rules:
                    # Selecciona una producción aleatoria
                    production = random.choice(self.rules[symbol])
                    # Reemplaza el símbolo no terminal con la producción
                    result = result[:i] + production + result[i + 1:]
                    break  # Salir del bucle después de reemplazar uno
        return result

# Definición de una gramática libre de contexto simple
rules = {
    'S': ['AB', 'aS', 'b'],
    'A': ['a'],
    'B': ['b']
}

# Crear una instancia de Grammar
grammar = Grammar(rules)

# Generar cadenas a partir del símbolo inicial 'S'
for _ in range(5):
    generated_string = grammar.generate('S')
    print(f"Cadena generada: {generated_string}")
"""
Clase Grammar:

__init__: Inicializa la gramática con un diccionario de reglas. Cada clave es un símbolo no terminal y cada valor es una lista de producciones posibles.
generate: Método para generar una cadena a partir de un símbolo inicial:
Comienza con el símbolo inicial.
Mientras haya no terminales en la cadena, busca uno y lo reemplaza con una producción aleatoria de las reglas correspondientes.
El proceso continúa hasta que la cadena está compuesta solo de símbolos terminales.
Definición de la Gramática:

Se define una gramática libre de contexto simple con el símbolo inicial 'S', que puede expandirse a 'AB', 'aS', o 'b'.
'A' se expande a 'a' y 'B' se expande a 'b'.
Generación de Cadenas:

Se generan cinco cadenas aleatorias a partir del símbolo inicial 'S' y se imprimen.
"""