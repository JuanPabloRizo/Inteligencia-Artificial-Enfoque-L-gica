import itertools

# Función para imprimir la tabla de verdad de la expresión lógica ¬(P ∧ Q) → (P ∨ ¬Q)
def tabla_de_verdad():
    # Variables proposicionales P y Q
    variables = ['P', 'Q']
    
    # Generamos todas las combinaciones posibles de valores de verdad para P y Q
    combinaciones = list(itertools.product([True, False], repeat=2))
    
    # Encabezado de la tabla, utilizando símbolos lógicos correctos
    print(f"{'P':<6} {'Q':<6} {'P ∧ Q':<8} {'¬(P ∧ Q)':<12} {'¬Q':<6} {'P ∨ ¬Q':<10} {'¬(P ∧ Q) → (P ∨ ¬Q)':<25}")
    
    # Iteramos sobre cada combinación y calculamos los valores de las expresiones
    for P, Q in combinaciones:
        conjuncion = P and Q          # P ∧ Q (AND lógico)
        negacion_conjuncion = not conjuncion  # ¬(P ∧ Q)
        negacion_Q = not Q            # ¬Q
        disyuncion = P or negacion_Q  # P ∨ ¬Q (OR lógico)
        implicacion = negacion_conjuncion <= disyuncion  # ¬(P ∧ Q) → (P ∨ ¬Q)
        
        # Imprimimos los resultados en la tabla de manera alineada
        print(f"{str(P):<6} {str(Q):<6} {str(conjuncion):<8} {str(negacion_conjuncion):<12} {str(negacion_Q):<6} {str(disyuncion):<10} {str(implicacion):<25}")

# Ejecutamos la función para ver la tabla de verdad
tabla_de_verdad()
"""
P ∧ Q representa la conjunción lógica (AND).
P ∨ ¬Q representa la disyunción lógica (OR con la negación de Q).
¬ se utiliza para la negación.
Librería itertools: Nos permite generar las combinaciones de valores de verdad para las variables P y Q (en este caso, True y False).

Encabezado de la tabla: Creamos una fila inicial con los nombres de las proposiciones y las operaciones que estamos evaluando.

Cálculo de las expresiones:

P ∧ Q: Calcula la conjunción lógica de P y Q.
¬(P ∧ Q): Calcula la negación de la conjunción.
¬Q: Calcula la negación de Q.
P ∨ ¬Q: Calcula la disyunción entre P y ¬Q.
¬(P ∧ Q) → (P ∨ ¬Q): Evalúa la implicación lógica entre ¬(P ∧ Q) y P ∨ ¬Q.
"""
