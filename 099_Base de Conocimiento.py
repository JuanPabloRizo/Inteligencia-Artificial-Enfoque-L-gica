class BaseDeConocimiento:
    def __init__(self):
        # Inicializar la base de conocimiento con hechos y reglas
        self.hechos = set()  # Conjunto de hechos
        self.reglas = []     # Lista de reglas (implicaciones)

    def agregar_hecho(self, hecho):
        # Agregar un hecho a la base de conocimiento
        self.hechos.add(hecho)

    def agregar_regla(self, premisas, conclusion):
        # Agregar una regla a la base de conocimiento (premisas → conclusion)
        self.reglas.append((premisas, conclusion))

    def hacer_inferencias(self):
        # Realizar inferencias en base a las reglas
        nuevos_hechos = True
        while nuevos_hechos:
            nuevos_hechos = False
            for premisas, conclusion in self.reglas:
                # Si todas las premisas se cumplen, añadir la conclusión a los hechos
                if all(premisa in self.hechos for premisa in premisas):
                    if conclusion not in self.hechos:
                        self.hechos.add(conclusion)
                        nuevos_hechos = True

    def consultar(self, hecho):
        # Consultar si un hecho está en la base de conocimiento
        return hecho in self.hechos

# Crear una base de conocimiento
kb = BaseDeConocimiento()

# Agregar hechos (Pedro tiene fiebre y tos)
kb.agregar_hecho('Fiebre(Pedro)')
kb.agregar_hecho('Tos(Pedro)')

# Agregar una regla (Si una persona tiene fiebre y tos, entonces tiene gripe)
kb.agregar_regla(['Fiebre(Pedro)', 'Tos(Pedro)'], 'Gripe(Pedro)')

# Hacer inferencias basadas en las reglas
kb.hacer_inferencias()

# Consultar si Pedro tiene gripe
print("¿Pedro tiene gripe?", kb.consultar('Gripe(Pedro)'))  # Debería imprimir: True
"""
Clase BaseDeConocimiento: Esta clase contiene una lista de hechos y reglas, y proporciona métodos para agregar hechos y reglas, hacer inferencias y consultar hechos.
Método agregar_hecho: Añade un hecho a la base de conocimiento.
Método agregar_regla: Añade una regla en forma de premisas y conclusión.
Método hacer_inferencias: Este método aplica las reglas sobre los hechos conocidos para deducir nuevos hechos.
Método consultar: Permite consultar si un hecho está en la base de conocimiento.
Ejemplo práctico:
Se agregan los hechos de que Pedro tiene fiebre y tos.
Se añade la regla que dice que si alguien tiene fiebre y tos, entonces tiene gripe.
Se ejecuta el motor de inferencias para deducir si Pedro tiene gripe.
Finalmente, se consulta si la base de conocimiento contiene el hecho de que Pedro tiene gripe.
"""