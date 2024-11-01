import pycosat

# Función que codifica un problema de planificación usando SATPLAN
def satplan(estado_inicial, estado_objetivo, acciones, num_pasos):
    """
    Genera una representación SAT para un problema de planificación.
    :param estado_inicial: Lista de hechos iniciales.
    :param estado_objetivo: Lista de hechos de estado objetivo.
    :param acciones: Lista de diccionarios que definen las acciones disponibles.
    :param num_pasos: Número de pasos de tiempo para intentar alcanzar la meta.
    :return: Resultado de la ejecución de SATPLAN.
    """
    # Representar hechos como variables booleanas con notación (paso, hecho)
    var_dict = {}
    num_var = 1

    # Función para obtener o crear una variable de hecho en un paso determinado
    def get_var(hecho, paso):
        if (hecho, paso) not in var_dict:
            var_dict[(hecho, paso)] = num_var
            nonlocal num_var
            num_var += 1
        return var_dict[(hecho, paso)]

    # Crear cláusulas de SAT para el problema
    clausulas = []

    # 1. Codificar el estado inicial
    for hecho in estado_inicial:
        clausulas.append([get_var(hecho, 0)])

    # 2. Codificar las acciones y efectos en cada paso
    for paso in range(num_pasos):
        for accion in acciones:
            precondiciones_vars = [get_var(precondicion, paso) for precondicion in accion["precondiciones"]]
            efectos_vars = [get_var(efecto, paso + 1) for efecto in accion["efectos"]]
            
            # Agregar precondiciones de la acción
            clausulas.append([-get_var(accion["nombre"], paso)] + precondiciones_vars)

            # Si se ejecuta la acción, se deben cumplir los efectos en el siguiente paso
            for efecto_var in efectos_vars:
                clausulas.append([-get_var(accion["nombre"], paso), efecto_var])

    # 3. Codificar la meta (estado objetivo)
    meta_vars = [get_var(hecho, num_pasos) for hecho in estado_objetivo]
    clausulas.append(meta_vars)

    # Resolver el problema SAT con pycosat
    solucion = pycosat.solve(clausulas)

    # Interpretar y retornar la solución
    if solucion == "UNSAT":
        print("No se encontró una solución.")
        return None
    else:
        plan = []
        for paso in range(num_pasos + 1):
            acciones_en_paso = [accion["nombre"] for accion in acciones if get_var(accion["nombre"], paso) in solucion]
            plan.append((paso, acciones_en_paso))
        return plan

# Ejemplo de uso de SATPLAN
if __name__ == "__main__":
    # Definir el estado inicial y objetivo
    estado_inicial = ["robot_en_sala1"]
    estado_objetivo = ["robot_en_sala2"]

    # Definir las acciones disponibles
    acciones = [
        {
            "nombre": "mover_a_sala2",
            "precondiciones": ["robot_en_sala1"],
            "efectos": ["robot_en_sala2"]
        },
        {
            "nombre": "mover_a_sala1",
            "precondiciones": ["robot_en_sala2"],
            "efectos": ["robot_en_sala1"]
        }
    ]

    # Intentar encontrar un plan en 1 paso de tiempo
    plan = satplan(estado_inicial, estado_objetivo, acciones, num_pasos=1)

    # Mostrar el resultado
    if plan:
        for paso, acciones in plan:
            print(f"Paso {paso}: {', '.join(acciones)}")
    else:
        print("No se encontró un plan.")
"""
Definición de Variables Booleanas (get_var):

Cada hecho y acción se representa como una variable booleana. La función get_var asigna un número único a cada combinación de hecho y paso de tiempo.
Codificación del Estado Inicial:

Se asegura que los hechos en estado_inicial son ciertos en el paso 0.
Codificación de Acciones y Efectos:

En cada paso de tiempo, para cada acción, se establecen las precondiciones y efectos. La lógica asegura que si la acción se ejecuta, entonces los efectos se cumplen en el siguiente paso.
Las precondiciones de cada acción deben cumplirse en el paso en que la acción se ejecuta, y los efectos se aplican en el siguiente paso.
Codificación del Estado Objetivo:

Las cláusulas para el estado objetivo aseguran que los hechos deseados estén presentes al final de los pasos permitidos (num_pasos).
Resolver con SAT y Extraer el Plan:

Se utiliza pycosat.solve para resolver las cláusulas SAT.
Si el problema es UNSAT, no se encontró una solución en el número de pasos especificado.
Si hay solución, se interpreta para mostrar las acciones a realizar en cada paso.
"""