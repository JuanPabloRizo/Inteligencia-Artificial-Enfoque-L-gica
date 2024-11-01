import random
import time

class Robot:
    def __init__(self, nombre, objetivo, posicion_inicial):
        self.nombre = nombre
        self.objetivo = objetivo
        self.posicion = posicion_inicial
        self.plan = ["mover", "recoger_objeto", "entregar_objeto"]
        self.estado = "inactivo"
    
    def ejecutar_plan(self, entorno):
        """Ejecuta el plan de acciones y adapta la planificación continuamente."""
        for accion in self.plan:
            if accion == "mover":
                self.mover_hacia_objetivo(entorno)
            elif accion == "recoger_objeto" and self.posicion == self.objetivo:
                self.recoger_objeto(entorno)
            elif accion == "entregar_objeto":
                self.entregar_objeto(entorno)

            # Esperar antes de la siguiente acción para simular continuidad
            time.sleep(1)

    def mover_hacia_objetivo(self, entorno):
        """Simula el movimiento del robot hacia su objetivo."""
        print(f"{self.nombre} se mueve hacia el objetivo en {self.objetivo}.")
        if entorno["obstaculo_presente"]:
            print(f"{self.nombre} detectó un obstáculo y replanifica.")
            self.ajustar_plan()
        else:
            self.posicion = self.objetivo
            print(f"{self.nombre} llegó a {self.objetivo}.")
    
    def recoger_objeto(self, entorno):
        """Simula la recogida del objeto."""
        print(f"{self.nombre} recogió el objeto en {self.objetivo}.")
        entorno["objeto_recogido"] = True
    
    def entregar_objeto(self, entorno):
        """Simula la entrega del objeto."""
        if entorno["objeto_recogido"]:
            print(f"{self.nombre} entregó el objeto en la base.")
            self.estado = "completado"
    
    def ajustar_plan(self):
        """Ajusta el plan si hay un obstáculo."""
        print(f"{self.nombre} ajusta su plan debido a un obstáculo.")
        self.plan.insert(0, "esquivar_obstaculo")


class EntornoMultiagente:
    def __init__(self):
        # Estado del entorno compartido por los robots
        self.estado = {
            "obstaculo_presente": random.choice([True, False]),
            "objeto_recogido": False
        }
        self.robots = []
    
    def agregar_robot(self, robot):
        """Agrega un robot al entorno."""
        self.robots.append(robot)
    
    def monitorear_y_coordinacion(self):
        """Simula la planificación continua y la coordinación entre robots."""
        while any(robot.estado != "completado" for robot in self.robots):
            for robot in self.robots:
                print(f"Estado de {robot.nombre}: {robot.estado}")
                robot.ejecutar_plan(self.estado)
                
                # Actualizar la presencia de obstáculos de forma aleatoria
                self.estado["obstaculo_presente"] = random.choice([True, False])
                
                # Monitorear y coordinar si otro robot ya completó la tarea
                if self.estado["objeto_recogido"]:
                    print("El objeto ya fue recogido. No es necesario que otros robots lo recojan.")
                    break


# Ejecución del sistema multiagente
if __name__ == "__main__":
    # Crear el entorno compartido
    entorno = EntornoMultiagente()

    # Crear robots con diferentes objetivos
    robot1 = Robot("Robot1", objetivo="zona_a", posicion_inicial="entrada")
    robot2 = Robot("Robot2", objetivo="zona_b", posicion_inicial="entrada")
    
    # Agregar los robots al entorno
    entorno.agregar_robot(robot1)
    entorno.agregar_robot(robot2)
    
    # Iniciar la planificación continua y coordinación entre los robots
    entorno.monitorear_y_coordinacion()
"""
Clase Robot: Cada robot tiene un plan que sigue secuencialmente:

mover_hacia_objetivo: Mueve al robot hacia el objetivo. Si detecta un obstáculo, ajusta su plan.
recoger_objeto: Simula la recolección de un objeto si el robot está en el objetivo.
entregar_objeto: Simula la entrega del objeto en la base.
ajustar_plan: Si un obstáculo aparece en el camino, el robot añade la acción de esquivarlo al inicio de su plan.
Clase EntornoMultiagente: Representa el entorno compartido por los robots y coordina sus acciones:

estado: Un diccionario que almacena el estado del entorno (como si hay un obstáculo o si el objeto ya ha sido recogido).
agregar_robot: Añade un robot al entorno.
monitorear_y_coordinacion: Controla el flujo de planificación y ejecución de cada robot.
Monitorea el estado y la posición de cada robot, y actualiza la presencia de obstáculos aleatoriamente.
Si un robot completa la recolección del objeto, se informa a los demás robots para evitar acciones redundantes.
Ejecución del Sistema Multiagente:

Los robots inician en la "entrada" y planean moverse a su respectiva zona para recoger el objeto.
La clase EntornoMultiagente permite que ambos robots se adapten a cambios y mantengan la sincronización en sus tareas, evitando que ambos intenten recoger el mismo objeto.
"""