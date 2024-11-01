# Clase que representa una acción en ADL
class AccionADL:
    def __init__(self, nombre, precondiciones, efectos):
        """
        Inicializa una acción en el modelo ADL.
        :param nombre: Nombre de la acción.
        :param precondiciones: Lista de precondiciones necesarias para la acción (incluyen predicados negativos).
        :param efectos: Efectos de la acción después de ejecutarse.
        """
        self.nombre = nombre
        self.precondiciones = precondiciones  # Precondiciones complejas con predicados negativos
        self.efectos = efectos                # Efectos que incluye la acción

    def es_ejecutable(self, estado):
        """
        Verifica si la acción puede ejecutarse en el estado actual.
        :param estado: Estado actual.
        :return: Verdadero si todas las precondiciones se cumplen en el estado.
        """
        for precondicion in self.precondiciones:
            if precondicion.startswith("no "):
                hecho_negativo = precondicion[3:]  # Elimina "no " para el predicado
                if hecho_negativo in estado:
                    return False
            elif precondicion not in estado:
                return False
        return True

# Clase para manejar el problema de planificación ADL
class ProblemaADL:
    def __init__(self, estado_inicial, meta):
        """
        Inicializa el problema de planificación ADL.
        :param estado_inicial: Estado inicial del entorno.
        :param meta: Estado objetivo deseado.
        """
        self.estado_actual = set(estado_inicial)  # Conjunto con el estado actual del entorno
        self.meta = set(meta)                     # Conjunto que representa el estado meta
        self.acciones = []                        # Lista de acciones posibles

    def agregar_accion(self, accion):
        """
        Agrega una acción al conjunto de acciones disponibles.
        :param accion: Objeto de la clase AccionADL.
        """
        self.acciones.append(accion)

    def es_meta(self):
        """
        Verifica si el estado actual cumple el estado meta.
        :return: Verdadero si el estado actual contiene todos los hechos del estado meta.
        """
        return self.meta.issubset(self.estado_actual)

    def ejecutar_accion(self, accion):
        """
        Ejecuta una acción en el estado actual si las precondiciones se cumplen.
        :param accion: Objeto AccionADL a ejecutar.
        """
        if accion.es_ejecutable(self.estado_actual):
            print(f"Ejecutando acción: {accion.nombre}")
            for efecto in accion.efectos.get("eliminar", []):
                self.estado_actual.discard(efecto)  # Eliminar efecto negativo si está en el estado
            for efecto in accion.efectos.get("agregar", []):
                self.estado_actual.add(efecto)      # Agregar efecto positivo al estado actual

    def planificar(self):
        """
        Intenta planificar una secuencia de acciones para alcanzar la meta.
        """
        while not self.es_meta():
            accion_aplicada = False
            for accion in self.acciones:
                if accion.es_ejecutable(self.estado_actual):
                    estado_anterior = self.estado_actual.copy()
                    self.ejecutar_accion(accion)
                    if self.estado_actual != estado_anterior:
                        accion_aplicada = True
                        break
            if not accion_aplicada:
                print("No se puede alcanzar el estado objetivo con las acciones disponibles.")
                return False
        print("Estado meta alcanzado con éxito.")
        return True

# Ejemplo de uso del modelo ADL
if __name__ == "__main__":
    # Definir el estado inicial y la meta
    estado_inicial = {"robot_en_sala", "objeto_en_sala"}
    estado_meta = {"objeto_en_cocina"}

    # Crear el problema ADL
    problema = ProblemaADL(estado_inicial, estado_meta)

    # Definir y agregar acciones
    mover_a_cocina = AccionADL(
        nombre="mover_a_cocina",
        precondiciones={"robot_en_sala"},
        efectos={
            "agregar": {"robot_en_cocina"},
            "eliminar": {"robot_en_sala"}
        }
    )

    recoger_objeto = AccionADL(
        nombre="recoger_objeto",
        precondiciones={"robot_en_cocina", "objeto_en_sala"},
        efectos={
            "agregar": {"robot_con_objeto"},
            "eliminar": {"objeto_en_sala"}
        }
    )

    colocar_objeto = AccionADL(
        nombre="colocar_objeto",
        precondiciones={"robot_con_objeto", "robot_en_cocina"},
        efectos={
            "agregar": {"objeto_en_cocina"},
            "eliminar": {"robot_con_objeto"}
        }
    )

    # Agregar las acciones al problema
    problema.agregar_accion(mover_a_cocina)
    problema.agregar_accion(recoger_objeto)
    problema.agregar_accion(colocar_objeto)

    # Ejecutar la planificación
    problema.planificar()
"""
Clase AccionADL:

Define una acción en ADL con soporte para predicados negativos en las precondiciones.
Método es_ejecutable: Verifica si se cumplen todas las precondiciones de la acción en el estado actual.
Clase ProblemaADL:

Representa el problema de planificación con:
Estado inicial (estado_inicial): Define el estado de inicio.
Meta (estado_meta): Define el objetivo.
Método ejecutar_accion: Verifica y aplica los efectos de la acción en el estado actual si las precondiciones se cumplen.
Método planificar: Ejecuta acciones hasta que se alcance el estado meta o no se puedan aplicar más acciones.
Ejemplo de Uso:

Estado inicial: El robot y el objeto están en la sala.
Estado meta: Mover el objeto a la cocina.
Acciones:
mover_a_cocina: Lleva al robot a la cocina.
recoger_objeto: Permite al robot recoger el objeto si está en la cocina y el objeto en la sala.
colocar_objeto: El robot coloca el objeto en la cocina.
"""