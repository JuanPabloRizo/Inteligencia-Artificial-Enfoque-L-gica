# Algoritmo AQ para la inducción de conceptos

class AlgoritmoAQ:
    def __init__(self):
        # Inicializa la hipótesis
        self.hipotesis = []

    def entrenar(self, ejemplos_positivos, ejemplos_negativos):
        # Para cada ejemplo positivo, se intenta crear una regla
        for ejemplo in ejemplos_positivos:
            nueva_regla = self.generar_regla(ejemplo)

            # Asegurarse de que la nueva regla no contradiga ejemplos negativos
            if self.validar_regla(nueva_regla, ejemplos_negativos):
                self.hipotesis.append(nueva_regla)

    def generar_regla(self, ejemplo):
        # Genera una regla a partir de un ejemplo positivo
        return {atributo: valor for atributo, valor in ejemplo.items()}

    def validar_regla(self, regla, ejemplos_negativos):
        # Verifica si la regla se aplica a algún ejemplo negativo
        for ejemplo_negativo in ejemplos_negativos:
            if all(ejemplo_negativo.get(k) == v for k, v in regla.items()):
                return False  # La regla no es válida si coincide con un ejemplo negativo
        return True  # La regla es válida

    def mostrar_hipotesis(self):
        # Muestra las hipótesis generadas
        if not self.hipotesis:
            print("No se generaron hipótesis.")
            return
        print("Hipótesis generadas:")
        for regla in self.hipotesis:
            print(regla)

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplos positivos
    ejemplos_positivos = [
        {'color': 'rojo', 'forma': 'redonda'},
        {'color': 'rojo', 'forma': 'cuadrada'},
        {'color': 'verde', 'forma': 'redonda'},
    ]

    # Ejemplos negativos
    ejemplos_negativos = [
        {'color': 'azul', 'forma': 'cuadrada'},
        {'color': 'verde', 'forma': 'cuadrada'},
        {'color': 'rojo', 'forma': 'triangular'},
    ]

    # Crear una instancia del Algoritmo AQ
    algoritmo_aq = AlgoritmoAQ()

    # Entrenar el modelo con ejemplos positivos y negativos
    algoritmo_aq.entrenar(ejemplos_positivos, ejemplos_negativos)

    # Mostrar las hipótesis generadas
    algoritmo_aq.mostrar_hipotesis()
"""
Clase AlgoritmoAQ:

__init__: Inicializa la lista de hipótesis.
entrenar: Toma ejemplos positivos y negativos como entrada. Para cada ejemplo positivo, genera una regla (una hipótesis) y verifica si es válida contra los ejemplos negativos. Si es válida, la agrega a la lista de hipótesis.
generar_regla: Genera una regla a partir de un ejemplo positivo. En este caso, crea un diccionario que representa los atributos y sus valores.
validar_regla: Comprueba si la regla generada se aplica a algún ejemplo negativo. Si es así, la regla no es válida.
mostrar_hipotesis: Muestra todas las hipótesis generadas.
Ejemplo de Uso:

Se definen ejemplos positivos y negativos que consisten en características como el color y la forma.
Se crea una instancia del algoritmo AQ, se entrena con los ejemplos y se muestran las hipótesis generadas.
"""