import pycosat

# Representamos nuestras proposiciones usando números enteros
# Para este ejemplo, asignamos lo siguiente:
# P(x) se representa como 1
# Q(y) se representa como 2

# Función para Skolemizar una fórmula
def skolemizacion():
    # Cláusula original antes de skolemización:
    # ∃x ∀y (P(x) ∨ ¬Q(y))
    
    # Paso 1: Eliminamos el cuantificador existencial (Skolemización)
    # P(x) se convierte en P(c), siendo c una constante de Skolem
    # Fórmula después de skolemización: P(c) ∨ ¬Q(y)
    
    # Paso 2: Eliminamos los cuantificadores universales
    # Ya está en forma normal conjuntiva (P(c) ∨ ¬Q(y))
    
    # Representamos esto en forma numérica para pycosat
    # P(c) se representa como 1 (positivo)
    # ¬Q(y) se representa como -2 (negativo)
    return [[1, -2]]  # P(c) o no Q(y)

# Función que usa el solucionador SAT para verificar la satisfacibilidad
def resolver():
    # Obtenemos la fórmula skolemizada
    clausulas = skolemizacion()
    
    # Usamos pycosat para verificar la satisfacibilidad de las cláusulas
    solucion = pycosat.solve(clausulas)
    
    # Si la solución es "UNSAT", no es satisfacible, de lo contrario lo es
    if solucion == 'UNSAT':
        print("La fórmula es insatisfacible (UNSAT).")
    else:
        print(f"La fórmula es satisfacible: {solucion}")

# Ejecutar la resolución
resolver()
"""
pycosat es una librería de Python que nos permite trabajar con problemas de Satisfacibilidad Booleana (SAT), donde podemos verificar si un conjunto de cláusulas en FNC es satisfacible o no.
Aquí skolemizamos la fórmula original. El valor 1 representa la proposición P(c), y -2 representa la negación de Q(y), que es ¬Q(y).
Las fórmulas se representan como una lista de listas de enteros, donde los números positivos indican variables y los negativos indican negaciones de variables.
pycosat.solve() recibe como entrada una lista de cláusulas en FNC y devuelve UNSAT si la fórmula es insatisfacible, o una solución si es satisfacible.
En nuestro caso, imprimimos si la fórmula es satisfacible o no.
Ejecución:
El código verifica si la fórmula es satisfacible o no utilizando la técnica de resolución con la fórmula skolemizada.
"""
