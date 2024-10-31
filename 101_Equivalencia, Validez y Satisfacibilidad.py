import itertools

class LogicaProposicional:
    def __init__(self, proposiciones):
        self.proposiciones = proposiciones

    def evaluar(self, formula, valores):
        """Evaluar una fórmula dada un conjunto de valores de verdad."""
        return eval(formula, {}, valores)

    def generar_tabla_verdad(self):
        """Generar la tabla de verdad para todas las combinaciones de valores de verdad."""
        tabla = []
        for valores in itertools.product([True, False], repeat=len(self.proposiciones)):
            asignacion = dict(zip(self.proposiciones, valores))
            asignacion['resultado'] = self.evaluar('P and Q', asignacion)  # Cambiar 'P and Q' según la fórmula
            tabla.append(asignacion)
        return tabla

    def es_equivalente(self, formula1, formula2):
        """Verifica si dos fórmulas son equivalentes."""
        for valores in itertools.product([True, False], repeat=len(self.proposiciones)):
            asignacion = dict(zip(self.proposiciones, valores))
            resultado1 = self.evaluar(formula1, asignacion)
            resultado2 = self.evaluar(formula2, asignacion)
            if resultado1 != resultado2:
                return False
        return True

    def es_valida(self, formula):
        """Verifica si una fórmula es válida."""
        for valores in itertools.product([True, False], repeat=len(self.proposiciones)):
            asignacion = dict(zip(self.proposiciones, valores))
            if not self.evaluar(formula, asignacion):
                return False
        return True

    def es_satisfacible(self, formula):
        """Verifica si una fórmula es satisfacible."""
        for valores in itertools.product([True, False], repeat=len(self.proposiciones)):
            asignacion = dict(zip(self.proposiciones, valores))
            if self.evaluar(formula, asignacion):
                return True
        return False


if __name__ == "__main__":
    # Definimos las proposiciones
    proposiciones = ['P', 'Q']
    
    # Creamos la clase de lógica proposicional
    logica = LogicaProposicional(proposiciones)

    # Fórmulas a evaluar
    formula1 = 'P and Q'
    formula2 = 'Q and P'  # Equivalente a formula1

    # Generar tabla de verdad
    tabla_verdad = logica.generar_tabla_verdad()
    for fila in tabla_verdad:
        print(f"P: {fila['P']}, Q: {fila['Q']}, Resultado: {fila['resultado']}")

    # Verificar equivalencia
    if logica.es_equivalente(formula1, formula2):
        print(f"{formula1} es equivalente a {formula2}.")
    else:
        print(f"{formula1} NO es equivalente a {formula2}.")

    # Verificar validez
    formula_valida = 'P or not P'
    if logica.es_valida(formula_valida):
        print(f"La fórmula '{formula_valida}' es válida.")
    else:
        print(f"La fórmula '{formula_valida}' NO es válida.")

    # Verificar satisfacibilidad
    formula_satisfacible = 'P and not Q'
    if logica.es_satisfacible(formula_satisfacible):
        print(f"La fórmula '{formula_satisfacible}' es satisfacible.")
    else:
        print(f"La fórmula '{formula_satisfacible}' NO es satisfacible.")
"""
.	Clases y Métodos:
	•	LogicaProposicional: Esta clase maneja la lógica proposicional, permitiendo la evaluación de fórmulas, la generación de tablas de verdad, y la verificación de equivalencia, validez y satisfacibilidad.
	•	evaluar: Toma una fórmula y un conjunto de valores para evaluar el resultado.
	•	generar_tabla_verdad: Crea una tabla de verdad para las proposiciones dadas y evalúa una fórmula específica (en este caso, P and Q).
	•	es_equivalente: Compara dos fórmulas y determina si son equivalentes.
	•	es_valida: Comprueba si una fórmula es válida para todas las asignaciones de valores.
	•	es_satisfacible: Verifica si existe al menos una asignación que haga verdadera la fórmula.
	2.	Uso:
	•	El código define dos proposiciones P y Q, y proporciona ejemplos de cómo evaluar la equivalencia entre P and Q y Q and P, la validez de la fórmula P or not P, y la satisfacibilidad de la fórmula P and not Q.
"""