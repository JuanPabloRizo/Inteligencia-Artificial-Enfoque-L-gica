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
            self.token_actual = self.tokens[self.pos]

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


class SemanticAnalyzer:
    """Clase que implementa el análisis semántico para las expresiones aritméticas."""
    def __init__(self, ast):
        self.ast = ast

    def analizar(self):
        """Realiza el análisis semántico sobre el AST."""
        self.verificar_nodos(self.ast)

    def verificar_nodos(self, nodo):
        """Verifica los nodos del AST para validar la semántica."""
        if nodo.tipo == 'NUMERO':
            return  # Un número es semánticamente válido

        if nodo.tipo in ('SUMA', 'RESTA', 'MULTIPLICACION', 'DIVISION'):
            # Verifica que ambos hijos sean números
            if nodo.izquierda.tipo == 'NUMERO' and nodo.derecha.tipo == 'NUMERO':
                # Verifica operaciones específicas, como la división por cero
                if nodo.tipo == 'DIVISION' and nodo.derecha.valor == 0:
                    raise Exception('Error semántico: División por cero')
            else:
                raise Exception(f'Error semántico: Operación {nodo.tipo} no válida entre {nodo.izquierda} y {nodo.derecha}')

            # Recursivamente verifica los hijos
            self.verificar_nodos(nodo.izquierda)
            self.verificar_nodos(nodo.derecha)


# Ejemplo de uso del analizador léxico, sintáctico y semántico
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

    # Análisis semántico
    analyzer = SemanticAnalyzer(arbol_sintaxis)
    try:
        analyzer.analizar()
        print("\nAnálisis semántico: No se encontraron errores.")
    except Exception as e:
        print(f"\nError durante el análisis semántico: {e}")
"""
Clase SemanticAnalyzer:

Se encarga de verificar el árbol de sintaxis abstracta (AST) para asegurarse de que las operaciones son semánticamente válidas.
Incluye métodos para verificar que las operaciones se realizan entre tipos compatibles y para detectar errores como la división por cero.
Método verificar_nodos:

Recorre el AST recursivamente, verificando cada nodo.
Si encuentra un operador, verifica que ambos hijos sean números.
Realiza validaciones específicas según el tipo de operación.
Ejemplo de Uso:

Al final del código, se realiza el análisis léxico y sintáctico, seguido del análisis semántico.
Se imprime un mensaje si se encuentran errores durante el análisis semántico.
"""