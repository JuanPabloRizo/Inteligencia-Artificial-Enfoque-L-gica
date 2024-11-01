import re

class Lexer:
    def __init__(self, texto):
        """Inicializa el analizador léxico con el texto de entrada.
        
        Args:
            texto (str): La cadena de texto que se va a analizar.
        """
        self.texto = texto
        self.pos = 0  # Posición actual en el texto
        self.caracter_actual = self.texto[self.pos] if self.texto else None

    def error(self):
        """Lanza un error si se encuentra un carácter no válido."""
        raise Exception(f'Error de análisis: carácter no válido {self.caracter_actual} en posición {self.pos}')

    def avanzar(self):
        """Avanza a la siguiente posición en el texto y actualiza el carácter actual."""
        self.pos += 1
        if self.pos > len(self.texto) - 1:
            self.caracter_actual = None  # Fin del texto
        else:
            self.caracter_actual = self.texto[self.pos]

    def ignorar_espacios(self):
        """Ignora los espacios en blanco y los saltos de línea en el texto."""
        while self.caracter_actual is not None and self.caracter_actual.isspace():
            self.avanzar()

    def ignorar_comentarios(self):
        """Ignora los comentarios que comienzan con '#'."""
        while self.caracter_actual is not None and self.caracter_actual == '#':
            while self.caracter_actual is not None and self.caracter_actual != '\n':
                self.avanzar()
            self.avanzar()  # Avanzar al siguiente carácter después del comentario

    def identificar_token(self):
        """Identifica el siguiente token en el texto."""
        while self.caracter_actual is not None:
            if self.caracter_actual.isspace():
                self.ignorar_espacios()
                continue
            
            if self.caracter_actual == '#':
                self.ignorar_comentarios()
                continue
            
            if self.caracter_actual.isalpha():  # Identificadores (letras)
                inicio = self.pos
                while self.caracter_actual is not None and self.caracter_actual.isalnum():
                    self.avanzar()
                lexema = self.texto[inicio:self.pos]
                return ('IDENTIFICADOR', lexema)
            
            if self.caracter_actual.isdigit():  # Números
                inicio = self.pos
                while self.caracter_actual is not None and self.caracter_actual.isdigit():
                    self.avanzar()
                lexema = self.texto[inicio:self.pos]
                return ('NUMERO', lexema)
            
            if self.caracter_actual == '=':  # Operador de asignación
                self.avanzar()
                return ('ASIGNACION', '=')
            if self.caracter_actual == '+':  # Operador suma
                self.avanzar()
                return ('SUMA', '+')
            if self.caracter_actual == '-':  # Operador resta
                self.avanzar()
                return ('RESTA', '-')
            if self.caracter_actual == '*':  # Operador multiplicación
                self.avanzar()
                return ('MULTIPLICACION', '*')
            if self.caracter_actual == '/':  # Operador división
                self.avanzar()
                return ('DIVISION', '/')
            if self.caracter_actual == '"':  # Cadena de texto
                self.avanzar()  # Avanzar para pasar la comilla de apertura
                inicio = self.pos
                while self.caracter_actual is not None and self.caracter_actual != '"':
                    self.avanzar()
                lexema = self.texto[inicio:self.pos]
                self.avanzar()  # Avanzar para pasar la comilla de cierre
                return ('CADENA', lexema)

            # Si llega aquí, el carácter no es válido
            self.error()  # Carácter no válido

        return ('EOF', None)  # Fin del archivo

    def analizar(self):
        """Analiza el texto y devuelve la lista de tokens generados."""
        tokens = []
        while self.caracter_actual is not None:
            token = self.identificar_token()
            tokens.append(token)
        return tokens

# Ejemplo de uso del analizador léxico
if __name__ == "__main__":
    texto = """
    x = 10 + 20
    y = x - 5  # Restar 5 de x
    z = "Hola, mundo"  # Saludo
    resultado = y * 2
    """
    lexer = Lexer(texto)
    try:
        tokens = lexer.analizar()
        print("Tokens generados:")
        for token in tokens:
            print(token)
    except Exception as e:
        print(e)
"""
Clase Lexer:

__init__: Inicializa el analizador léxico con el texto de entrada, establece la posición actual y el carácter actual.
error: Lanza un error si se encuentra un carácter no válido.
avanzar: Mueve la posición actual al siguiente carácter en el texto y actualiza el carácter actual.
ignorar_espacios: Ignora los espacios en blanco y los saltos de línea.
ignorar_comentarios: Ignora las líneas de comentarios que comienzan con #.
identificar_token: Identifica el siguiente token en el texto. Puede reconocer identificadores, números, operadores y cadenas de texto.
Usa bucles para recorrer los caracteres y clasificar los tokens.
analizar: Analiza el texto completo y devuelve una lista de tokens generados.
Ejemplo de Uso:

Se crea una instancia de Lexer con una cadena de texto que contiene una expresión simple con comentarios y cadenas.
Se analizan los tokens y se imprimen.
"""