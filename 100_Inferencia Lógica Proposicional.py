# Clase para representar una Base de Conocimiento Proposicional
class BaseDeConocimientoProposicional:
    def __init__(self):
        # Inicializar la base de conocimiento con un conjunto de proposiciones (hechos)
        # y una lista de reglas de inferencia.
        self.proposiciones = set()  # Almacena los hechos conocidos (como 'P', 'Q', etc.)
        self.reglas = []  # Almacena reglas de la forma (premisas, conclusión).

    def agregar_proposicion(self, proposicion):
        # Método para agregar una proposición (hecho) a la base de conocimiento.
        # Las proposiciones son verdades establecidas en el sistema.
        self.proposiciones.add(proposicion)

    def agregar_regla(self, premisas, conclusion):
        # Método para agregar una regla a la base de conocimiento.
        # Cada regla tiene una lista de premisas y una conclusión.
        # Si todas las premisas se cumplen, entonces se infiere la conclusión.
        self.reglas.append((premisas, conclusion))

    def hacer_inferencias(self):
        # Método para realizar inferencias lógicas a partir de las reglas en la base de conocimiento.
        # Verifica si todas las premisas de una regla se cumplen y, si es así,
        # agrega la conclusión a la base de proposiciones (hechos).
        nuevos_hechos = True  # Para seguir haciendo inferencias mientras haya nuevos hechos.
        while nuevos_hechos:
            nuevos_hechos = False  # Inicialmente, asumimos que no habrá nuevos hechos.
            for premisas, conclusion in self.reglas:
                # Verificamos si todas las premisas están en las proposiciones conocidas (hechos).
                if all(premisa in self.proposiciones for premisa in premisas):
                    # Si la conclusión no está ya en las proposiciones conocidas, la agregamos.
                    if conclusion not in self.proposiciones:
                        print(f"Inferencia: {conclusion}")  # Mostramos la inferencia realizada.
                        self.proposiciones.add(conclusion)  # Agregamos la conclusión como nuevo hecho.
                        nuevos_hechos = True  # Marcamos que hemos encontrado nuevos hechos.

    def consultar(self, proposicion):
        # Método para consultar si una proposición (hecho) está en la base de conocimiento.
        return proposicion in self.proposiciones


# Crear una base de conocimiento proposicional
kb = BaseDeConocimientoProposicional()

# Agregar proposiciones (hechos) a la base de conocimiento
# 'P' representa que "Pedro tiene fiebre".
# 'Q' representa que "Pedro tiene tos".
kb.agregar_proposicion('P')
kb.agregar_proposicion('Q')

# Agregar una regla de inferencia:
# Si 'P' (Pedro tiene fiebre) y 'Q' (Pedro tiene tos), entonces 'G' (Pedro tiene gripe).
kb.agregar_regla(['P', 'Q'], 'G')

# Realizar inferencias basadas en las reglas definidas y los hechos conocidos.
kb.hacer_inferencias()

# Consultar si 'G' (Pedro tiene gripe) ha sido inferido a partir de los hechos y las reglas.
if kb.consultar('G'):
    print("Pedro tiene gripe.")
else:
    print("No se ha inferido que Pedro tenga gripe.")
"""
Clase BaseDeConocimientoProposicional: Representa una base de conocimiento proposicional, que puede almacenar proposiciones (hechos) y reglas de inferencia.

Proposiciones: Son los hechos conocidos que agregamos mediante agregar_proposicion. En este caso, 'P' y 'Q' son ejemplos de proposiciones.

Reglas: Definimos reglas de inferencia, como "Si Pedro tiene fiebre ('P') y tiene tos ('Q'), entonces tiene gripe ('G')". Estas reglas son procesadas para realizar inferencias con el método hacer_inferencias.

Inferencia: A partir de los hechos y reglas, el sistema infiere nuevas proposiciones. En este ejemplo, si ambas premisas ('P' y 'Q') son ciertas, entonces se puede inferir 'G' (que Pedro tiene gripe).

Consulta: Se puede consultar si una proposición está en la base de conocimiento con el método consultar.
"""