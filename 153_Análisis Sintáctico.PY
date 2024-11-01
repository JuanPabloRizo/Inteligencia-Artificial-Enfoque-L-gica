class Token:
    """Clase que representa un token en el análisis léxico."""
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

    def __repr__(self):
        return f"Token({self.tipo}, {repr(self.valor)})"


class Lexer:
    """Clase que implementa el analizador léxico para las expresiones aritméticas."""
    def __init__(self, texto):
        self.texto = texto
        self.pos = 0  # Posición actual en el texto
        self.caracter_actual = self.texto[self.pos] if self.texto else None

    def error(self):
        """Lanza un error si se encuentra un carácter no válido."""
        raise Exception(f'Error de análisis: carácter no válido {self.caracter_actual}')

    def avanzar(self):
        """Avanza a la siguiente posición en el texto y actualiza el carácter actual."""
        self.pos += 1
        if self.pos > len(self.texto) - 1:
            self.caracter_actual = None  # Fin del texto
        else:
            self.caracter_actual = self.texto[self.pos]

    def ignorar_espacios(self):
        """Ignora los espacios en blanco en el texto."""
        while self.caracter_actual is not None and self.caracter_actual.isspace():
            self.avanzar()

    def identificar_token(self):
        """Identifica el siguiente token en el texto."""
        while self.caracter_actual is not None:
            if self.caracter_actual.isspace():
                self.ignorar_espacios()
                continue

            if self.caracter_actual.isdigit():  # Números
                inicio = self.pos
                while self.caracter_actual is not None and self.caracter_actual.isdigit():
                    self.avanzar()
                return Token('NUMERO', int(self.texto[inicio:self.pos]))

            if self.caracter_actual == '+':
                self.avanzar()
                return Token('SUMA', '+')
            if self.caracter_actual == '-':
                self.avanzar()
                return Token('RESTA', '-')
            if self.caracter_actual == '*':
                self.avanzar()
                return Token('MULTIPLICACION', '*')
            if self.caracter_actual == '/':
                self.avanzar()
                return Token('DIVISION', '/')
            if self.caracter_actual == '(':
                self.avanzar()
                return Token('PAR_IZQUIERDO', '(')
            if self.caracter_actual == ')':
                self.avanzar()
                return Token('PAR_DERECHO', ')')

            self.error()  # Carácter no válido

        return Token('EOF', None)  # Fin del archivo

    def analizar(self):
        """Analiza el texto y devuelve la lista de tokens generados."""
        tokens = []
        while self.caracter_actual is not None:
            token = self.identificar_token()
            tokens.append(token)
        return tokens


class Nodo:
    """Clase que representa un nodo en el árbol de sintaxis abstracta (AST)."""
    def __init__(self, tipo, valor=None, izquierda=None, derecha=None):
        self.tipo = tipo
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

    def __repr__(self):
        if self.tipo == 'NUMERO':
            return f'Nodo(NUMERO, {self.valor})'
        return f'Nodo({self.tipo}, {self.izquierda}, {self.derecha})'


class Parser:
    """Clase que implementa el analizador sintáctico para las expresiones aritméticas."""
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.token_actual = self.tokens[self.pos]

    def error(self):
        """Lanza un error si se encuentra un token inesperado."""
        raise Exception(f'Error de análisis sintáctico: token inesperado {self.token_actual}')

    def avanzar(self):
        """Avanza al siguiente token en la lista de tokens."""
        self.pos += 1
        if self.pos > len(self.tokens) - 1:
            self.token_actual = Token('EOF', None)  # Fin de los tokens
        else:
            self.token_current = self.tokens[self.pos]

    def factor(self):
        """Analiza un factor: número o paréntesis."""
        token = self.token_actual
        if token.tipo == 'NUMERO':
            self.avanzar()
            return Nodo('NUMERO', token.valor)
        elif token.tipo == 'PAR_IZQUIERDO':
            self.avanzar()
            nodo = self.expresion()
            if self.token_actual.tipo != 'PAR_DERECHO':
                self.error()
            self.avanzar()
            return nodo
        self.error()

    def termino(self):
        """Analiza un término: factor seguido de multiplicación o división."""
        nodo = self.factor()
        while self.token_actual.tipo in ('MULTIPLICACION', 'DIVISION'):
            token = self.token_actual
            self.avanzar()
            nodo = Nodo(token.tipo, izquierda=nodo, derecha=self.factor())
        return nodo

    def expresion(self):
        """Analiza una expresión: término seguido de suma o resta."""
        nodo = self.termino()
        while self.token_actual.tipo in ('SUMA', 'RESTA'):
            token = self.token_actual
            self.avanzar()
            nodo = Nodo(token.tipo, izquierda=nodo, derecha=self.termino())
        return nodo

    def parsear(self):
        """Inicia el análisis sintáctico y retorna el nodo raíz del AST."""
        return self.expresion()


# Ejemplo de uso del analizador léxico y sintáctico
if __name__ == "__main__":
    texto = "3 + 5 * ( 2 - 8 )"
    lexer = Lexer(texto)
    tokens = lexer.analizar()

    print("Tokens generados:")
    for token in tokens:
        print(token)

    parser = Parser(tokens)
    arbol_sintaxis = parser.parsear()

    print("\nÁrbol de Sintaxis Abstracta (AST):")
    print(arbol_sintaxis)
"""
Clase Token:

Representa un token con un tipo y un valor.
Clase Lexer:

Implementa el analizador léxico que convierte un texto en una lista de tokens.
Identifica números, operadores y paréntesis.
Ignora espacios y maneja errores de caracteres no válidos.
Clase Nodo:

Representa un nodo en el árbol de sintaxis abstracta (AST).
Cada nodo puede ser un número o un operador, y puede tener nodos hijos (izquierdo y derecho).
Clase Parser:

Implementa el analizador sintáctico que construye el AST a partir de la lista de tokens.
Usa una gramática sencilla para definir la jerarquía de operaciones: primero los factores (números o expresiones entre paréntesis), luego los términos (factores multiplicados o divididos) y finalmente las expresiones (términos sumados o restados).
Ejemplo de Uso:

Se analiza la expresión aritmética "3 + 5 * ( 2 - 8 )".
Se generan tokens y se construye un árbol de sintaxis abstracta que representa la estructura de la expresión.
"""