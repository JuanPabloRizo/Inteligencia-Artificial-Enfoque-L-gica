# Clase para representar una acción en STRIPS
class AccionSTRIPS:
    def __init__(self, nombre, precondiciones, efectos):
        """
        Inicializa una acción en el modelo STRIPS.
        :param nombre: Nombre de la acción
        :param precondiciones: Lista de precondiciones necesarias para la acción
        :param efectos: Lista de efectos que produce la acción
        """
        self.nombre = nombre
        self.precondiciones = precondiciones  # Hechos que deben cumplirse antes de ejecutar
        self.efectos = efectos                # Hechos que resultan tras la acción

# Clase para representar el problema de planificación
class ProblemaSTRIPS:
    def __init__(self, estado_inicial, meta):
        """
        Inicializa el problema de planificación.
        :param estado_inicial: Estado inicial del entorno
        :param meta: Estado objetivo que se desea alcanzar
        """
        self.estado_actual = estado_inicial     # Estado inicial en el que empieza el planificador
        self.meta = meta                        # Estado objetivo que queremos alcanzar
        self.acciones = []                      # Lista de acciones disponibles

    def agregar_accion(self, accion):
        """
        Agrega una acción al conjunto de acciones disponibles.
        :param accion: Objeto AccionSTRIPS que se puede ejecutar
        """
        self.acciones.append(accion)

    def es_meta(self):
        """
        Verifica si el estado actual cumple con el estado meta.
        :return: Verdadero si el estado actual contiene todos los elementos de la meta
        """
        return all(hecho in self.estado_actual for hecho in self.meta)

    def aplicar_accion(self, accion):
        """
        Aplica una acción, si las precondiciones se cumplen, y actualiza el estado actual.
        :param accion: Objeto AccionSTRIPS que se intentará ejecutar
        """
        # Verificar si todas las precondiciones se cumplen en el estado actual
        if all(pre in self.estado_actual for pre in accion.precondiciones):
            print(f"Ejecutando acción: {accion.nombre}")
            # Remover efectos negativos (hechos que deben eliminarse)
            for efecto in accion.efectos["eliminar"]:
                if efecto in self.estado_actual:
                    self.estado_actual.remove(efecto)
            # Agregar efectos positivos
            for efecto in accion.efectos["agregar"]:
                self.estado_actual.add(efecto)
        else:
            print(f"No se puede ejecutar {accion.nombre}, precondiciones no cumplidas.")

    def planificar(self):
        """
        Planifica una secuencia de acciones para alcanzar el estado meta.
        """
        # Bucle para intentar alcanzar el estado meta
        while not self.es_meta():
            accion_aplicada = False
            for accion in self.acciones:
                # Intentar aplicar una acción y verificar si acerca al estado meta
                estado_anterior = self.estado_actual.copy()  # Guardar el estado actual antes de aplicar la acción
                self.aplicar_accion(accion)                  # Intentar ejecutar la acción
                # Verificar si la acción fue aplicada y cambió el estado
                if estado_anterior != self.estado_actual:
                    accion_aplicada = True
                    break
            # Si no se pudo aplicar ninguna acción, el plan falla
            if not accion_aplicada:
                print("No se puede alcanzar el objetivo con las acciones disponibles.")
                return False
        print("Se alcanzó el estado meta.")
        return True

# Ejemplo de uso
if __name__ == "__main__":
    # Definir el estado inicial y el objetivo
    estado_inicial = {"robot_en_cocina", "caja_en_cocina"}
    estado_meta = {"caja_en_sala"}

    # Crear el problema de planificación
    problema = ProblemaSTRIPS(estado_inicial, estado_meta)

    # Definir y agregar acciones
    mover_caja_a_sala = AccionSTRIPS(
        nombre="mover_caja_a_sala",
        precondiciones={"robot_en_cocina", "caja_en_cocina"},
        efectos={
            "agregar": {"caja_en_sala", "robot_en_sala"},
            "eliminar": {"caja_en_cocina", "robot_en_cocina"}
        }
    )

    mover_robot_a_cocina = AccionSTRIPS(
        nombre="mover_robot_a_cocina",
        precondiciones={"robot_en_sala"},
        efectos={
            "agregar": {"robot_en_cocina"},
            "eliminar": {"robot_en_sala"}
        }
    )

    # Agregar las acciones al problema
    problema.agregar_accion(mover_caja_a_sala)
    problema.agregar_accion(mover_robot_a_cocina)

    # Ejecutar la planificación
    problema.planificar()
"""
Clase AccionSTRIPS: Define una acción en el modelo STRIPS, especificando:

Precondiciones: Los hechos que deben cumplirse antes de la acción.
Efectos: Lo que la acción produce, divididos en hechos que se agregan o se eliminan del estado actual.
Clase ProblemaSTRIPS: Representa el problema de planificación.

Estado inicial (estado_inicial): Describe cómo comienza el entorno.
Meta (estado_meta): Describe el objetivo o el estado deseado.
Métodos:
es_meta: Comprueba si el estado actual cumple con el objetivo.
aplicar_accion: Ejecuta una acción si sus precondiciones están en el estado actual.
planificar: Busca aplicar una secuencia de acciones para alcanzar el objetivo.
Ejemplo de uso:

Estado inicial: El robot y la caja están en la cocina.
Estado meta: La caja debe estar en la sala.
Acciones:
mover_caja_a_sala: Mueve la caja a la sala si el robot y la caja están en la cocina.
mover_robot_a_cocina: Lleva al robot de vuelta a la cocina si está en la sala.
Planificación: Ejecuta acciones que cambian el estado hasta alcanzar el estado meta o hasta que no haya acciones válidas.
"""