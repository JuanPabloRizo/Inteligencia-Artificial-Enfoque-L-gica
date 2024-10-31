from collections import defaultdict

class GraphPlan:
    def __init__(self, acciones, estado_inicial, estado_objetivo):
        """
        Inicializa el planificador GRAPHPLAN.
        :param acciones: Diccionario de acciones con precondiciones y efectos.
        :param estado_inicial: Conjunto de condiciones iniciales.
        :param estado_objetivo: Conjunto de condiciones objetivo.
        """
        self.acciones = acciones  # Acciones disponibles
        self.estado_inicial = estado_inicial  # Estado inicial
        self.estado_objetivo = estado_objetivo  # Estado objetivo
        self.grafo = defaultdict(list)  # Grafo de planificación
        self.niveles = []  # Lista para almacenar niveles del grafo

    def generar_grafo(self):
        """
        Genera el grafo de planificación utilizando las acciones y estados.
        """
        # Inicializa el primer nivel con el estado inicial
        self.niveles.append(self.estado_inicial)

        # Genera niveles hasta que se alcance el objetivo o no haya más acciones
        while True:
            nuevo_nivel = set()  # Nuevo nivel de efectos
            for accion, (precondiciones, efectos) in self.acciones.items():
                # Verifica si se pueden ejecutar las precondiciones en el nivel actual
                if precondiciones.issubset(self.niveles[-1]):
                    nuevo_nivel.update(efectos)  # Añade los efectos al nuevo nivel
                    self.grafo[self.niveles[-1]].append(efectos)  # Añade el efecto al grafo

            if not nuevo_nivel:  # Si no se han añadido nuevos efectos, detener el bucle
                break
            self.niveles.append(nuevo_nivel)  # Añadir el nuevo nivel al grafo

    def planificar(self):
        """
        Genera un plan utilizando el grafo de planificación.
        """
        self.generar_grafo()  # Genera el grafo de planificación
        plan = []  # Lista de acciones a realizar

        # Verifica si se puede alcanzar el estado objetivo
        for estado in reversed(self.niveles):
            if self.estado_objetivo.issubset(estado):  # Si el estado objetivo está en el nivel
                for efecto in estado:
                    for accion, (precondiciones, efectos) in self.acciones.items():
                        if efectos == efecto:  # Si la acción produce el efecto
                            plan.append(accion)  # Añadir la acción al plan

        plan.reverse()  # Invertir el plan para tener el orden correcto
        return plan

# Ejemplo de uso
if __name__ == "__main__":
    # Definición de acciones y sus precondiciones y efectos
    acciones = {
        "Preparar Ingredientes": ({"Ingredientes Listos"}, {"Ingredientes Preparados"}),
        "Cocinar": ({"Ingredientes Preparados"}, {"Comida Cocinada"}),
        "Servir": ({"Comida Cocinada"}, {"Comida Servida"})
    }

    estado_inicial = {"Ingredientes Listos"}  # Estado inicial del sistema
    estado_objetivo = {"Comida Servida"}  # Estado objetivo deseado

    # Crear un planificador
    graph_plan = GraphPlan(acciones, estado_inicial, estado_objetivo)

    # Generar plan
    plan = graph_plan.planificar()  # Genera el plan para alcanzar el estado objetivo

    # Mostrar el plan final
    if plan:
        print("Plan de acciones a seguir:")
        for accion in plan:
            print("-", accion)  # Imprime cada acción en el plan
    else:
        print("No se pudo encontrar un plan para alcanzar el estado objetivo.")  # Mensaje si no se encuentra un plan


"""
Clase GraphPlan:

__init__: Inicializa el planificador con acciones, estado inicial y estado objetivo.
generar_grafo: Crea el grafo de planificación, generando niveles de estados a partir de las acciones disponibles. Si las precondiciones de una acción están en el nivel actual, se añade su efecto al nuevo nivel.
planificar: Utiliza el grafo generado para crear un plan de acciones. Comprueba si el estado objetivo se encuentra en alguno de los niveles generados y, si es así, construye el plan correspondiente.
Ejemplo de Uso:

Se definen acciones junto con sus precondiciones y efectos.
Se especifican el estado inicial y el objetivo.
Se crea una instancia de GraphPlan y se genera el plan.
Se imprime el plan de acciones a seguir.
"""