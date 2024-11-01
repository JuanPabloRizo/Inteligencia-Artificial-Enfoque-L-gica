class PlanificadorCondicional:
    def __init__(self):
        # Definir el plan inicial vacío y el estado actual del entorno
        self.plan = []
        self.estado_entorno = {
            "ubicacion_robot": "entrada",
            "objeto_encontrado": False,
            "obstaculo_presente": True
        }

    def planificar(self):
        """Genera un plan condicional basado en el estado actual del entorno."""
        # Primer paso: Moverse a la zona de búsqueda
        self.plan.append("mover_a_zona_busqueda")
        
        # Condición para verificar si hay un obstáculo
        if self.estado_entorno["obstaculo_presente"]:
            self.plan.append("evitar_obstaculo")
        
        # Agregar tarea de búsqueda del objeto
        self.plan.append("buscar_objeto")
        
        # Condición para actuar si se encuentra el objeto
        if self.estado_entorno["objeto_encontrado"]:
            self.plan.append("recoger_objeto")
        else:
            # En caso de no encontrar el objeto, buscar en otra zona
            self.plan.append("buscar_en_otro_lugar")
        
        # Agregar paso para regresar a la entrada
        self.plan.append("regresar_a_entrada")

    def ejecutar_plan(self):
        """Ejecuta cada acción del plan y ajusta según las condiciones."""
        for accion in self.plan:
            print(f"Ejecutando acción: {accion}")
            # Ejecutar acción según su tipo
            if accion == "mover_a_zona_busqueda":
                self.estado_entorno["ubicacion_robot"] = "zona_busqueda"
                print("Robot se ha movido a la zona de búsqueda.")

            elif accion == "evitar_obstaculo":
                print("Evitando obstáculo...")
                # Suponer que el robot evita con éxito el obstáculo
                self.estado_entorno["obstaculo_presente"] = False

            elif accion == "buscar_objeto":
                print("Buscando objeto...")
                # Simular si el objeto se encuentra en la primera búsqueda
                if self.estado_entorno["ubicacion_robot"] == "zona_busqueda":
                    self.estado_entorno["objeto_encontrado"] = True
                    print("Objeto encontrado.")

            elif accion == "recoger_objeto":
                print("Recogiendo el objeto...")
                # Simular la recolección del objeto
                self.estado_entorno["objeto_encontrado"] = False

            elif accion == "buscar_en_otro_lugar":
                print("Buscando en otra zona...")
                # Cambiar ubicación de búsqueda
                self.estado_entorno["ubicacion_robot"] = "otra_zona"
                # Suponer que el objeto se encuentra en la segunda búsqueda
                self.estado_entorno["objeto_encontrado"] = True
                print("Objeto encontrado en otra zona.")
            
            elif accion == "regresar_a_entrada":
                self.estado_entorno["ubicacion_robot"] = "entrada"
                print("Regresando a la entrada.")

            # Revisar estado después de cada acción para ajustar en caso de cambio
            if not self.estado_entorno["objeto_encontrado"] and accion == "recoger_objeto":
                print("Error: No hay objeto para recoger.")

# Ejemplo de uso del planificador condicional
if __name__ == "__main__":
    # Crear el planificador
    planificador = PlanificadorCondicional()

    # Generar el plan basado en el estado inicial del entorno
    planificador.planificar()

    # Ejecutar el plan generado
    print("Iniciando ejecución del plan...")
    planificador.ejecutar_plan()
"""
Clase PlanificadorCondicional:

Se define el plan inicial como una lista vacía y el estado actual del entorno, que contiene la ubicación del robot, la presencia de un objeto y la presencia de obstáculos.
Método planificar:

Este método genera un plan basado en condiciones. Primero, el robot se dirige a la zona de búsqueda.
Si hay un obstáculo, el plan incluye una acción para evitarlo.
Luego, se añade la acción de búsqueda del objeto. Si el objeto se encuentra, el plan incluye la acción de recogerlo; si no, agrega una acción para buscar en otra zona.
Finalmente, el robot regresa a la entrada.
Método ejecutar_plan:

Este método ejecuta cada acción en el plan.
Después de cada acción, el estado del entorno se actualiza, y el plan puede ajustarse si ciertas condiciones cambian.
Por ejemplo, si se intenta recoger el objeto pero no se encuentra, imprime un mensaje de error.
"""