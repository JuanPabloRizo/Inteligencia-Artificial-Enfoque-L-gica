# Clase para representar un agente lógico basado en reglas
class AgenteLogico:
    def __init__(self):
        # Inicializar la base de conocimiento (hechos conocidos por el agente)
        self.base_de_conocimiento = set()

    def percibir(self, percepcion):
        # Actualizar la base de conocimiento con la percepción recibida
        print(f"Percepción recibida: {percepcion}")
        self.base_de_conocimiento.add(percepcion)  # Añadir percepción a los hechos conocidos

    def agregar_regla(self, premisas, conclusion):
        # Agregar una regla de inferencia a la base de conocimiento
        # Las reglas se almacenan como tuplas (conjunto de premisas, conclusión)
        self.base_de_conocimiento.add((frozenset(premisas), conclusion))  # frozenset asegura que las premisas sean inmutables y sin orden

    def inferir(self):
        # Realizar inferencias basadas en las reglas de la base de conocimiento
        inferido = True
        while inferido:  # Repetir mientras se puedan inferir nuevos hechos
            inferido = False
            nuevos_hechos = []  # Almacenar temporalmente los nuevos hechos inferidos
            for item in self.base_de_conocimiento:
                if isinstance(item, tuple) and len(item) == 2:  # Verificar si el item es una regla (tupla con premisas y conclusión)
                    premisas, conclusion = item  # Desempaquetar la regla en premisas y conclusión
                    # Verificar si todas las premisas son verdaderas (están en la base de conocimiento)
                    if all(p in self.base_de_conocimiento for p in premisas):
                        if conclusion not in self.base_de_conocimiento:  # Si la conclusión no ha sido inferida aún
                            print(f"Inferencia: {conclusion}")
                            nuevos_hechos.append(conclusion)  # Añadir la conclusión a la lista de nuevos hechos
                            inferido = True  # Señalar que se ha hecho una inferencia
            # Al finalizar la iteración, agregar los nuevos hechos a la base de conocimiento
            self.base_de_conocimiento.update(nuevos_hechos)

    def consultar(self, proposicion):
        # Consultar si una proposición es verdadera en la base de conocimiento
        return proposicion in self.base_de_conocimiento  # Devuelve True si la proposición está en la base de conocimiento

# Ejemplo de uso del agente lógico
if __name__ == "__main__":
    # Crear un agente lógico
    agente = AgenteLogico()

    # Percepciones iniciales del agente
    agente.percibir('El suelo está limpio')
    agente.percibir('El agente tiene la escoba')

    # Agregar reglas a la base de conocimiento
    # Si el suelo está limpio y el agente tiene la escoba, el agente puede descansar
    agente.agregar_regla(['El suelo está limpio', 'El agente tiene la escoba'], 'El agente puede descansar')

    # Realizar inferencias
    agente.inferir()

    # Consultar si el agente puede descansar
    if agente.consultar('El agente puede descansar'):
        print("El agente puede descansar.")
    else:
        print("El agente no puede descansar todavía.")



"""
Clase AgenteLogico:

Es la estructura que representa el agente lógico.
Tiene una base de conocimiento, que almacena hechos y reglas.
Método percibir:

Simula las percepciones del agente en su entorno. Cada percepción se agrega a la base de conocimiento como un hecho.
Método agregar_regla:

Este método permite agregar reglas de inferencia en la forma premisas → conclusión.
Las reglas se almacenan como tuplas donde las premisas se representan como un conjunto inmutable (usando frozenset).
Método inferir:

Este es el núcleo del agente lógico. Recorre la base de conocimiento buscando reglas cuyas premisas se cumplan. Si encuentra tales reglas, infiere la conclusión y la agrega a la base de conocimiento.
El bucle while sigue haciendo inferencias hasta que no se puedan agregar nuevos hechos.
Método consultar:

Verifica si una proposición específica está en la base de conocimiento.
Ejemplo de ejecución:

El agente percibe que "el suelo está limpio" y que "el agente tiene la escoba".
Se agrega una regla: Si el suelo está limpio y el agente tiene la escoba, entonces el agente puede descansar.
Después de inferir, el agente deduce que puede descansar.
"""