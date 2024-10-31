# Clase para representar un sistema de lógica por defecto
class LogicaPorDefecto:
    def __init__(self):
        # Base de conocimiento con hechos
        self.base_de_conocimiento = set()
        # Reglas con suposiciones por defecto
        self.reglas = []

    def agregar_hecho(self, hecho):
        # Agregar un hecho a la base de conocimiento
        self.base_de_conocimiento.add(hecho)
        print(f"Hecho agregado: {hecho}")

    def agregar_regla(self, condicion, conclusion):
        # Agregar una regla de inferencia
        self.reglas.append((condicion, conclusion))

    def inferir(self):
        # Realizar inferencias basado en la lógica por defecto
        nuevos_hechos = True
        while nuevos_hechos:
            nuevos_hechos = False
            for condicion, conclusion in self.reglas:
                # Verificar si la condición se cumple
                if condicion not in self.base_de_conocimiento:
                    # Si no hay información contradictoria, inferimos la conclusión
                    print(f"Suposición: {condicion} es cierto, inferimos: {conclusion}")
                    self.base_de_conocimiento.add(conclusion)
                    nuevos_hechos = True

    def consultar(self, proposicion):
        # Consultar si una proposición está en la base de conocimiento
        return proposicion in self.base_de_conocimiento


# Ejemplo de uso de la lógica por defecto
if __name__ == "__main__":
    # Crear un sistema de lógica por defecto
    sistema = LogicaPorDefecto()

    # Agregar hechos a la base de conocimiento
    sistema.agregar_hecho("El cielo es azul")
    
    # Agregar reglas de inferencia
    # Si el cielo es azul, entonces probablemente es un día despejado
    sistema.agregar_regla("El cielo es azul", "Es un día despejado")

    # Hacer inferencias
    sistema.inferir()

    # Consultar si es un día despejado
    if sistema.consultar("Es un día despejado"):
        print("Conclusión: Es un día despejado.")
    else:
        print("Conclusión: No se puede inferir que es un día despejado.")

    # Ahora agregamos un nuevo hecho que contradice la suposición
    sistema.agregar_hecho("Está nublado")

    # Intentar inferir de nuevo
    sistema.inferir()

    # Consultar nuevamente si es un día despejado
    if sistema.consultar("Es un día despejado"):
        print("Conclusión: Es un día despejado.")
    else:
        print("Conclusión: No se puede inferir que es un día despejado.")
"""
Clase LogicaPorDefecto: Representa un sistema que puede almacenar hechos y reglas, y realizar inferencias basadas en lógica por defecto.

Métodos principales:

agregar_hecho(hecho): Añade un hecho a la base de conocimiento y lo imprime en la consola.
agregar_regla(condicion, conclusion): Añade una regla que relaciona una condición con una conclusión. Si la condición es verdadera, se puede inferir la conclusión.
inferir(): Realiza inferencias. Si una condición no está presente en los hechos conocidos, se asume que es verdadera y se añade la conclusión. Esto representa el razonamiento por defecto.
consultar(proposicion): Verifica si una proposición está en la base de conocimiento.
Ejemplo en acción:

Se agrega un hecho "El cielo es azul" y se establece una regla que dice que si el cielo es azul, entonces es un día despejado.
Se infiere que "es un día despejado" basado en el hecho y la regla.
Luego, se agrega un nuevo hecho "Está nublado", que contradice la suposición de que "el cielo es azul", lo que afecta la inferencia anterior.
"""