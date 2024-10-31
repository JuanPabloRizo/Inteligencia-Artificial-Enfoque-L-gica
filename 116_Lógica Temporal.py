# Clase para representar un sistema de lógica temporal con estados
class LogicaTemporal:
    def __init__(self, estados):
        # Los estados representan los valores de las proposiciones en cada momento del tiempo
        self.estados = estados

    def G(self, proposicion):
        # Verifica si una proposición es verdadera en todos los estados (Globally)
        return all(proposicion(estado) for estado in self.estados)

    def F(self, proposicion):
        # Verifica si una proposición es verdadera en algún estado futuro (Finally)
        return any(proposicion(estado) for estado in self.estados)

    def X(self, proposicion):
        # Verifica si una proposición es verdadera en el siguiente estado (Next)
        return proposicion(self.estados[1]) if len(self.estados) > 1 else False

    def U(self, proposicion1, proposicion2):
        # Verifica si proposicion1 es verdadera hasta que proposicion2 lo sea (Until)
        for estado in self.estados:
            if proposicion2(estado):
                return True
            if not proposicion1(estado):
                return False
        return False

# Ejemplo de proposiciones (funciones que dependen del estado)
def es_sol(lluvia):
    # Ejemplo de proposición: True si no está lloviendo
    return not lluvia

def es_lluvia(lluvia):
    # Ejemplo de proposición: True si está lloviendo
    return lluvia

# Estados a lo largo del tiempo (True indica lluvia, False indica sol)
# [Día 1: sol, Día 2: lluvia, Día 3: lluvia, Día 4: sol]
estados = [False, True, True, False]

# Crear el sistema de lógica temporal
lt = LogicaTemporal(estados)

# Verificar algunas propiedades temporales
print(f"Siempre es sol: {lt.G(es_sol)}")  # Globally: ¿Siempre es sol?
print(f"En algún momento será sol: {lt.F(es_sol)}")  # Finally: ¿Algún momento será sol?
print(f"Será lluvia en el siguiente instante: {lt.X(es_lluvia)}")  # Next: ¿Lluvia en el siguiente?
print(f"Es sol hasta que haya lluvia: {lt.U(es_sol, es_lluvia)}")  # Until: ¿Es sol hasta que haya lluvia?
"""
Clase LogicaTemporal:

Se utiliza para representar un sistema en el que se pueden verificar proposiciones en diferentes momentos del tiempo.
Tiene métodos para los operadores modales G (Globally), F (Finally), X (Next) y U (Until).
Métodos de la clase:

G(proposicion): Verifica si la proposición es verdadera en todos los estados del sistema (siempre verdadera).
F(proposicion): Verifica si la proposición es verdadera en al menos uno de los estados futuros.
X(proposicion): Verifica si la proposición es verdadera en el siguiente estado (paso temporal).
U(proposicion1, proposicion2): Verifica si proposicion1 es verdadera hasta que proposicion2 se haga verdadera.
Proposiciones:

Se utilizan funciones es_sol y es_lluvia como ejemplos de proposiciones, que determinan si en un estado dado está lloviendo o hay sol.
Estados:

Los estados se representan como una lista de valores booleanos donde True indica lluvia y False indica sol.
"""