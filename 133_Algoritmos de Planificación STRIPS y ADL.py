class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        """
        Inicializa una acción con su nombre, precondiciones y efectos.
        :param nombre: Nombre de la acción.
        :param precondiciones: Lista de condiciones que deben ser verdaderas para ejecutar la acción.
        :param efectos: Lista de efectos que resultan de ejecutar la acción.
        """
        self.nombre = nombre
        self.precondiciones = precondiciones
        self.efectos = efectos

class Planificador:
    def __init__(self, estado_inicial):
        """
        Inicializa el planificador con un estado inicial.
        :param estado_inicial: Estado inicial del mundo.
        """
        self.estado = estado_inicial
        self.plan = []

    def puede_ejecutar(self, accion):
        """
        Verifica si se puede ejecutar una acción dada la situación actual.
        :param accion: La acción a verificar.
        :return: True si se puede ejecutar, False en caso contrario.
        """
        return all(condicion in self.estado for condicion in accion.precondiciones)

    def ejecutar_accion(self, accion):
        """
        Ejecuta una acción y actualiza el estado actual.
        :param accion: La acción a ejecutar.
        """
        self.estado.update(accion.efectos)  # Agrega los efectos al estado actual
        self.plan.append(accion.nombre)  # Añade la acción al plan

    def planificar(self, acciones, objetivo):
        """
        Genera un plan para alcanzar el objetivo.
        :param acciones: Lista de acciones disponibles.
        :param objetivo: Conjunto de condiciones que se deben cumplir para alcanzar el objetivo.
        :return: El plan generado o None si no se puede alcanzar el objetivo.
        """
        while not objetivo.issubset(self.estado):
            for accion in acciones:
                if self.puede_ejecutar(accion):
                    self.ejecutar_accion(accion)
                    print(f"Ejecutando acción: {accion.nombre}")
                    break
            else:
                # No se puede ejecutar ninguna acción, plan fallido
                return None
        return self.plan

# Ejemplo de uso
if __name__ == "__main__":
    # Estado inicial
    estado_inicial = {"en_casa", "tiene_clave"}
    
    # Definición de acciones
    acciones = [
        Accion("abrir_puerta", ["en_casa", "tiene_clave"], ["puerta_abierta"]),
        Accion("salir", ["puerta_abierta"], ["fuera_de_casa"]),
    ]

    # Estado objetivo
    objetivo = {"fuera_de_casa"}

    # Crear el planificador
    planificador = Planificador(set(estado_inicial))
    
    # Planificar
    plan = planificador.planificar(acciones, set(objetivo))

    # Mostrar el plan
    if plan:
        print("Plan generado:", plan)
    else:
        print("No se pudo generar un plan para alcanzar el objetivo.")
"""
Clase Accion:

Representa una acción con un nombre, precondiciones y efectos.
__init__: Inicializa la acción.
Clase Planificador:

Inicializa el estado del mundo y mantiene un plan de acciones a ejecutar.
puede_ejecutar: Verifica si una acción puede ejecutarse dadas las condiciones actuales del estado.
ejecutar_accion: Ejecuta la acción, actualizando el estado y agregando la acción al plan.
planificar: Genera un plan para alcanzar el objetivo dado un conjunto de acciones. Utiliza un bucle para ejecutar acciones hasta que se cumplan las condiciones del objetivo.
Ejemplo de uso:

Se define un estado inicial y una lista de acciones disponibles.
Se define un objetivo que se desea alcanzar.
Se crea una instancia del planificador y se invoca el método planificar para generar el plan.
"""