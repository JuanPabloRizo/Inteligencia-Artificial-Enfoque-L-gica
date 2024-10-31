def unificar(expr1, expr2):
    """
    Función para unificar dos expresiones lógicas.
    :param expr1: Primer término (cadena de texto).
    :param expr2: Segundo término (cadena de texto).
    :return: Diccionario de unificación o None si no se puede unificar.
    """
    # Si ambas expresiones son iguales, no hay necesidad de unificación.
    if expr1 == expr2:
        return {}

    # Si uno de los términos es una variable, la unificación es posible.
    elif es_variable(expr1):
        return {expr1: expr2}
    elif es_variable(expr2):
        return {expr2: expr1}

    # Si ambas expresiones son compuestas (contienen funciones).
    elif es_compuesto(expr1) and es_compuesto(expr2):
        # Separamos la función y sus argumentos.
        func1, args1 = separar(expr1)
        func2, args2 = separar(expr2)

        # Si las funciones son diferentes, no se puede unificar.
        if func1 != func2:
            return None

        # Intentamos unificar los argumentos recursivamente.
        unificaciones = {}
        for arg1, arg2 in zip(args1, args2):
            resultado = unificar(arg1, arg2)
            if resultado is None:
                return None
            unificaciones.update(resultado)

        return unificaciones

    # En cualquier otro caso, no se puede unificar.
    return None

def es_variable(expr):
    """
    Verifica si la expresión es una variable (una sola letra en este caso).
    :param expr: Expresión a verificar.
    :return: True si es una variable, False en caso contrario.
    """
    return isinstance(expr, str) and len(expr) == 1 and expr.isalpha()

def es_compuesto(expr):
    """
    Verifica si la expresión es compuesta (contiene una función).
    :param expr: Expresión a verificar.
    :return: True si es compuesta, False en caso contrario.
    """
    return isinstance(expr, str) and '(' in expr and ')' in expr

def separar(expr):
    """
    Separa una expresión compuesta en su función y argumentos.
    :param expr: Expresión compuesta.
    :return: Tupla (función, lista de argumentos).
    """
    func = expr[:expr.index('(')]  # Nombre de la función
    args = expr[expr.index('(') + 1:-1].split(',')  # Argumentos
    return func, args

# Ejemplo de uso
expr1 = 'f(X, g(Y))'
expr2 = 'f(a, g(b))'

resultado = unificar(expr1, expr2)

if resultado is not None:
    print("Unificación exitosa:", resultado)
else:
    print("No se puede unificar.")
"""
Función unificar(expr1, expr2): Esta es la función principal que intenta unificar dos expresiones.

Caso 1: Si expr1 y expr2 son iguales, simplemente devuelve un diccionario vacío.
Caso 2: Si uno de los términos es una variable, devuelve una sustitución que mapea la variable al otro término.
Caso 3: Si ambos términos son compuestos, separa la función y sus argumentos, y verifica si las funciones coinciden. Luego intenta unificar los argumentos recursivamente.
Caso 4: Si ninguna de las condiciones anteriores se cumple, devuelve None, indicando que no se puede unificar.
Funciones auxiliares:

es_variable(expr): Comprueba si expr es una variable (una letra).
es_compuesto(expr): Comprueba si expr es una expresión compuesta.
separar(expr): Separa una expresión compuesta en su función y sus argumentos.
Ejemplo de uso: Se definen dos expresiones y se intenta unificarlas. Si la unificación es exitosa, se imprime el resultado; de lo contrario, se indica que no se puede unificar.
"""