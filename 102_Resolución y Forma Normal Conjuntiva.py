from sympy import symbols, Or, Not, Implies, to_cnf

# Definición de las proposiciones
P, Q, R = symbols('P Q R')

# Función para aplicar la resolución entre dos cláusulas
def resolver(clause1, clause2):
    resolvente = set()
    for literal in clause1:
        if Not(literal) in clause2:
            # Crear el resolvente eliminando el literal y su negación
            resolvente = (clause1.union(clause2)) - {literal, Not(literal)}
            return resolvente
    return None

# Clase para manejar resolución por refutación
class Resolucion:
    def __init__(self):
        self.clausulas = []  # Lista para almacenar las cláusulas en FNC

    def agregar_clausula(self, clausula):
        """Agrega una cláusula en FNC."""
        self.clausulas.append(set(clausula))  # Convierte la cláusula a un conjunto

    def resolver_todas(self):
        """Aplica la resolución a todas las cláusulas."""
        nuevos = set()  # Conjunto para nuevas cláusulas deducidas
        while True:
            pares = [(self.clausulas[i], self.clausulas[j]) for i in range(len(self.clausulas)) for j in range(i+1, len(self.clausulas))]
            for (ci, cj) in pares:
                resolvente = resolver(ci, cj)  # Aplicar resolución entre cláusulas
                if resolvente is not None:
                    if not resolvente:  # Si el resolvente es vacío
                        return True  # Se deduce una contradicción
                    nuevos.add(frozenset(resolvente))  # Añadir la nueva cláusula
            # Si no hay nuevas cláusulas, finalizar
            if nuevos.issubset(set(map(frozenset, self.clausulas))):
                return False  # No se deducen nuevas cláusulas
            for nuevo in nuevos:
                if set(nuevo) not in self.clausulas:
                    self.clausulas.append(set(nuevo))  # Añadir la cláusula deducida

# Función principal
if __name__ == "__main__":
    # Fórmula original con implicaciones
    formula = Implies(P, Q)  # Si P entonces Q

    # Convertir la fórmula a Forma Normal Conjuntiva (FNC)
    fnc_formula = to_cnf(formula)
    print(f"Fórmula en FNC: {fnc_formula}")

    # Crear una instancia de Resolucion
    resolucion = Resolucion()

    # Agregar cláusulas en FNC
    resolucion.agregar_clausula([P])           # P
    resolucion.agregar_clausula([Not(Q), P])    # ¬Q ∨ P
    resolucion.agregar_clausula([Q])            # Q

    # Agregar la negación de la conclusión que queremos probar
    resolucion.agregar_clausula([Not(P)])       # ¬P

    # Intentar probar P por refutación
    if resolucion.resolver_todas():
        print("Se dedujo una contradicción, P es verdadero.")
    else:
        print("No se pudo deducir P.")
"""
Definición de Proposiciones: Se definen las proposiciones 
P, Q y R utilizando sympy.

Función resolver: Esta función toma dos cláusulas, busca un literal en una que esté negado en la otra, y devuelve el resolvente. Si no encuentra tal par, devuelve None.

Clase Resolucion:

Tiene métodos para agregar cláusulas y aplicar resolución hasta que se encuentre una contradicción o no se puedan deducir más cláusulas.
Utiliza un conjunto para almacenar las cláusulas para evitar duplicados.
Función Principal:

Convierte una fórmula que contiene una implicación a su forma normal conjuntiva.
Crea una instancia de la clase Resolucion, agrega cláusulas y prueba la proposición.
"""