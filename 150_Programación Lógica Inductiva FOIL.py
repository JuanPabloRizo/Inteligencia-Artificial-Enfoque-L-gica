class FOIL:
    def __init__(self):
        # Inicializar el conjunto de reglas
        self.reglas = []

    def aprender(self, ejemplos_positivos, ejemplos_negativos):
        # Aprender reglas a partir de ejemplos positivos y negativos
        while ejemplos_positivos:
            # Inducir una regla
            regla = self.inducir_regla(ejemplos_positivos, ejemplos_negativos)
            if regla is None:
                break
            # Agregar la regla al conjunto de reglas
            self.reglas.append(regla)
            # Filtrar ejemplos positivos cubiertos por la regla
            ejemplos_positivos = [ej for ej in ejemplos_positivos if not regla.evaluar(ej)]

    def inducir_regla(self, ejemplos_positivos, ejemplos_negativos):
        # Generar una regla a partir de ejemplos positivos
        mejor_regla = None
        mejor_cobertura = -1
        
        for ejemplo in ejemplos_positivos:
            # Generar una regla simple a partir del ejemplo positivo
            regla = Regla(ejemplo)
            cobertura = self.cobertura(regla, ejemplos_positivos, ejemplos_negativos)

            # Si la cobertura es mejor que la anterior, actualizar la mejor regla
            if cobertura > mejor_cobertura:
                mejor_cobertura = cobertura
                mejor_regla = regla

        return mejor_regla

    def cobertura(self, regla, ejemplos_positivos, ejemplos_negativos):
        # Contar cuántos ejemplos positivos y negativos cubre la regla
        count_positivos = sum(1 for ej in ejemplos_positivos if regla.evaluar(ej))
        count_negativos = sum(1 for ej in ejemplos_negativos if regla.evaluar(ej))
        return count_positivos - count_negativos

class Regla:
    def __init__(self, ejemplo):
        # Inicializar la regla a partir del ejemplo
        self.atributos = ejemplo

    def evaluar(self, ejemplo):
        # Evaluar si un ejemplo cumple con la regla
        return all(ejemplo.get(atributo) == valor for atributo, valor in self.atributos.items())

# Ejemplo de uso de FOIL
if __name__ == "__main__":
    # Ejemplos positivos
    ejemplos_positivos = [
        {'color': 'rojo', 'forma': 'redonda'},
        {'color': 'rojo', 'forma': 'cuadrada'},
        {'color': 'verde', 'forma': 'redonda'},
    ]

    # Ejemplos negativos
    ejemplos_negativos = [
        {'color': 'azul', 'forma': 'redonda'},
        {'color': 'rojo', 'forma': 'triangular'},
        {'color': 'verde', 'forma': 'cuadrada'},
    ]

    # Crear una instancia de FOIL
    foil = FOIL()
    
    # Aprender reglas a partir de ejemplos
    foil.aprender(ejemplos_positivos, ejemplos_negativos)

    # Imprimir las reglas aprendidas
    for i, regla in enumerate(foil.reglas):
        print(f"Regla {i + 1}: {regla.atributos}")
"""
Clase FOIL:

__init__: Inicializa una lista vacía para almacenar las reglas aprendidas.
aprender: Método principal que aprende reglas. Toma ejemplos positivos y negativos y las refina iterativamente.
inducir_regla: Busca la mejor regla que cubra los ejemplos positivos, utilizando el mejor ejemplo como base.
cobertura: Calcula cuántos ejemplos positivos son cubiertos por la regla y cuántos ejemplos negativos se violan.
Clase Regla:

__init__: Inicializa la regla a partir de un ejemplo, almacenando sus atributos.
evaluar: Método que verifica si un ejemplo cumple con la regla.
Ejemplo de Uso:

Define ejemplos positivos y negativos como diccionarios de atributos.
Crea una instancia de FOIL y llama al método aprender con los ejemplos.
Imprime las reglas aprendidas.
"""