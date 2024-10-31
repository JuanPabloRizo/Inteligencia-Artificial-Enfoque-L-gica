class Tarea:
    def __init__(self, nombre, precondiciones):
        """
        Inicializa una tarea con su nombre y las precondiciones necesarias.
        :param nombre: Nombre de la tarea.
        :param precondiciones: Lista de precondiciones que deben cumplirse antes de realizar la tarea.
        """
        self.nombre = nombre  # Nombre de la tarea
        self.precondiciones = precondiciones  # Precondiciones para ejecutar la tarea

class PlanificadorOrdenParcial:
    def __init__(self, tareas):
        """
        Inicializa el planificador con una lista de tareas.
        :param tareas: Lista de tareas a planificar.
        """
        self.tareas = tareas  # Lista de tareas
        self.estado = set()  # Estado inicial vacío
        self.plan = []  # Plan final a construir

    def puede_ejecutar(self, tarea):
        """
        Verifica si una tarea se puede ejecutar según las precondiciones.
        :param tarea: La tarea a verificar.
        :return: True si la tarea se puede ejecutar, False en caso contrario.
        """
        return all(precondicion in self.estado for precondicion in tarea.precondiciones)

    def ejecutar_tarea(self, tarea):
        """
        Ejecuta una tarea y actualiza el estado actual.
        :param tarea: La tarea a ejecutar.
        """
        print(f"Ejecutando tarea: {tarea.nombre}")  # Imprime la tarea que se está ejecutando
        self.plan.append(tarea.nombre)  # Añade la tarea al plan
        self.estado.add(tarea.nombre)  # Actualiza el estado con la tarea completada

    def planificar(self):
        """
        Genera un plan para completar todas las tareas respetando las precondiciones.
        """
        while self.tareas:  # Mientras haya tareas por realizar
            ejecutado = False  # Controla si se ha ejecutado alguna tarea en el ciclo
            for tarea in self.tareas:  # Iterar sobre las tareas disponibles
                if self.puede_ejecutar(tarea):  # Verifica si se puede ejecutar la tarea
                    self.ejecutar_tarea(tarea)  # Ejecutar la tarea
                    self.tareas.remove(tarea)  # Remover la tarea de la lista de tareas
                    ejecutado = True  # Se ejecutó una tarea
                    break  # Rompe el bucle para reiniciar la búsqueda

            if not ejecutado:  # Si no se ejecutó ninguna tarea en este ciclo
                print("No se puede ejecutar más tareas. Verifica las precondiciones.")  # Mensaje de error
                break  # Salir del ciclo

# Ejemplo de uso
if __name__ == "__main__":
    # Definición de tareas con sus precondiciones
    tareas = [
        Tarea("Preparar ingredientes", []),  # Puede realizarse en cualquier momento
        Tarea("Cocinar", ["Preparar ingredientes"]),  # Necesita que los ingredientes estén preparados
        Tarea("Servir", ["Cocinar"]),  # Necesita que la comida esté cocinada
    ]

    # Crear un planificador
    planificador = PlanificadorOrdenParcial(tareas)

    # Planificar
    planificador.planificar()  # Genera el plan para completar todas las tareas

    # Mostrar el plan final
    print("Plan final:", planificador.plan)  # Imprime el plan final de tareas ejecutadas
"""
Clase Tarea: Define cada tarea que el agente puede realizar. Cada tarea tiene un nombre y una lista de precondiciones que deben cumplirse antes de que se pueda ejecutar.

Clase PlanificadorOrdenParcial:

__init__: Inicializa el planificador con una lista de tareas y un estado vacío.
puede_ejecutar: Verifica si la tarea se puede ejecutar, asegurándose de que todas sus precondiciones estén en el estado actual.
ejecutar_tarea: Ejecuta la tarea, imprime el nombre de la tarea y actualiza el estado y el plan.
planificar: Genera un plan para completar todas las tareas. Continúa ejecutando tareas hasta que se completen o no se puedan ejecutar más.
Ejemplo de Uso:

Se definen tres tareas: preparar ingredientes, cocinar y servir, con sus respectivas precondiciones.
Se crea una instancia del planificador y se llama al método planificar.
Finalmente, se imprime el plan generado que muestra las tareas en el orden en que se ejecutaron.
"""