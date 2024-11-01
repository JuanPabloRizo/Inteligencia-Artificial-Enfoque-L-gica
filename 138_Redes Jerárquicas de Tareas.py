class HTNPlanner:
    def __init__(self):
        # Definir la lista de métodos y el plan final que el robot debe ejecutar
        self.metodos = {}
        self.plan = []

    def agregar_metodo(self, tarea, metodo):
        """Registra un método para descomponer una tarea."""
        if tarea not in self.metodos:
            self.metodos[tarea] = []
        self.metodos[tarea].append(metodo)

    def planificar(self, tarea, contexto):
        """
        Planifica una tarea usando los métodos apropiados.
        :param tarea: La tarea inicial a planificar.
        :param contexto: El contexto actual (e.g., estado de la sala).
        :return: El plan de acciones a ejecutar.
        """
        if tarea in self.metodos:
            for metodo in self.metodos[tarea]:
                sub_tareas = metodo(contexto)
                if sub_tareas:
                    for sub_tarea in sub_tareas:
                        if not self.planificar(sub_tarea, contexto):
                            return False
                    return True
        elif self.es_primtiva(tarea):
            print(f"Ejecutando tarea: {tarea}")
            self.plan.append(tarea)
            return True
        return False

    def es_primtiva(self, tarea):
        """Verifica si una tarea es primitiva y, por lo tanto, ejecutable directamente."""
        primitivas = ["barrer", "limpiar_mesas", "organizar_objetos", "revisar_inventario"]
        return tarea in primitivas

# Métodos para descomposición de tareas complejas

def metodo_limpiar_sala(contexto):
    """Descompone la tarea 'limpiar_sala' en sub-tareas si la sala está sucia."""
    if contexto.get("sala_sucia", False):
        return ["barrer", "limpiar_mesas"]
    return []

def metodo_organizar_sala(contexto):
    """Descompone la tarea 'organizar_sala' en sub-tareas de organización."""
    if contexto.get("objetos_desorganizados", False):
        return ["organizar_objetos", "revisar_inventario"]
    return []

# Configuración y uso del planificador HTN
if __name__ == "__main__":
    # Crear un planificador HTN
    planificador = HTNPlanner()

    # Registrar métodos para tareas compuestas
    planificador.agregar_metodo("limpiar_sala", metodo_limpiar_sala)
    planificador.agregar_metodo("organizar_sala", metodo_organizar_sala)

    # Definir el contexto inicial del entorno
    contexto = {
        "sala_sucia": True,
        "objetos_desorganizados": True
    }

    # Planificar las tareas principales
    tareas_principales = ["limpiar_sala", "organizar_sala"]
    for tarea in tareas_principales:
        if planificador.planificar(tarea, contexto):
            print(f"Tarea '{tarea}' planificada exitosamente.")
        else:
            print(f"No se pudo planificar la tarea '{tarea}'.")

    # Mostrar el plan generado
    print("\nPlan final generado:")
    for accion in planificador.plan:
        print(accion)
"""
Clase HTNPlanner:

Contiene métodos para agregar descomposiciones de tareas (métodos) y para ejecutar la planificación recursiva.
El método planificar realiza la descomposición de tareas usando los métodos registrados para cada tarea. Si la tarea es primitiva, se añade directamente al plan.
Métodos de Tareas Compuestas:

Los métodos metodo_limpiar_sala y metodo_organizar_sala descomponen las tareas complejas en sub-tareas en función del contexto.
Cada método verifica si el contexto permite que las sub-tareas sean necesarias (por ejemplo, si la sala está sucia o si los objetos están desorganizados).
Ejecución de la Planificación:

Se define un contexto inicial, contexto, que indica el estado de la sala.
Las tareas principales son descompuestas hasta que se obtiene un plan ejecutable compuesto solo de tareas primitivas.
"""