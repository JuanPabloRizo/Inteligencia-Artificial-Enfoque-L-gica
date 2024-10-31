from sympy import symbols, ForAll, Function, Implies

# Definimos variables
x, y = symbols('x y')

# Definimos un predicado F (que es una función de orden superior)
F = Function('F')

# Expresamos una fórmula de orden superior: Para todo F, F(x) implica F(y)
formula = ForAll(F(x), Implies(F(x), F(y)))

# Mostramos la fórmula
print("Fórmula de lógica de orden superior:")
print(formula)
"""
Importación de sympy:

sympy es una biblioteca de Python que permite trabajar con álgebra simbólica, incluyendo la lógica proposicional y de predicados.
Importamos los componentes necesarios como symbols (para definir variables), ForAll (cuantificador universal) y Function (para definir funciones de orden superior).
Definición de variables:

x y y son individuos en el dominio del discurso, y se definen usando symbols.
Definición de un predicado:

F es una función de orden superior. Esto significa que F es un predicado que puede ser aplicado a diferentes argumentos, en este caso, x y y.
Construcción de la fórmula:

Usamos ForAll(F(x), ...) para expresar que la fórmula aplica para todos los predicados F.
La fórmula en este caso expresa que si F(x) es verdadero, entonces F(y) también lo es (Implies(F(x), F(y))).
Impresión de la fórmula:

Finalmente, imprimimos la fórmula construida para mostrar cómo se vería en un lenguaje simbólico.
Explicación:
Este código genera una fórmula de lógica de orden superior que establece que para cualquier predicado F, si F(x) es verdadero, 
entonces F(y) también lo es. Esto es un ejemplo de cómo la lógica de orden superior permite cuantificar sobre predicados, algo que no es 
posible en la lógica de primer orden.
"""