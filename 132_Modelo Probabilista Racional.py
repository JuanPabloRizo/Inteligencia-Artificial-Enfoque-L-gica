# Importar librerías necesarias
from collections import defaultdict

# Clase para representar un Modelo Probabilista Racional
class ModeloProbabilistaRacional:
    def __init__(self):
        """Inicializa el modelo con datos de probabilidad."""
        # Probabilidades previas de enfermedades
        self.probabilidades_enfermedades = {
            'Gripe': 0.1,  # Probabilidad previa de tener gripe
            'Resfriado': 0.3,  # Probabilidad previa de tener resfriado
            'Alergia': 0.2,  # Probabilidad previa de tener alergia
        }

        # Probabilidades condicionales de síntomas dado la enfermedad
        self.probabilidades_condicionales = {
            'Gripe': {'tos': 0.8, 'fiebre': 0.9, 'dolor de cabeza': 0.7},
            'Resfriado': {'tos': 0.7, 'fiebre': 0.3, 'dolor de cabeza': 0.4},
            'Alergia': {'tos': 0.2, 'fiebre': 0.0, 'dolor de cabeza': 0.1},
        }

    def calcular_probabilidad(self, enfermedad, sintomas):
        """
        Calcula la probabilidad posterior de una enfermedad dado un conjunto de síntomas usando el Teorema de Bayes.

        :param enfermedad: Nombre de la enfermedad.
        :param sintomas: Lista de síntomas observados.
        :return: Probabilidad posterior de la enfermedad.
        """
        probabilidad_anterior = self.probabilidades_enfermedades[enfermedad]  # Probabilidad previa
        probabilidad_sintomas_dado_enfermedad = 1.0  # Inicializa la probabilidad condicional

        # Calcular la probabilidad condicional de los síntomas dado la enfermedad
        for sintoma in sintomas:
            if sintoma in self.probabilidades_condicionales[enfermedad]:
                probabilidad_sintomas_dado_enfermedad *= self.probabilidades_condicionales[enfermedad][sintoma]
            else:
                probabilidad_sintomas_dado_enfermedad *= 0  # Si el síntoma no es relevante, probabilidad 0

        # Calcular la probabilidad posterior usando Bayes
        probabilidad_posterior = probabilidad_anterior * probabilidad_sintomas_dado_enfermedad
        return probabilidad_posterior

    def diagnosticar(self, sintomas):
        """
        Realiza un diagnóstico basado en los síntomas ingresados.

        :param sintomas: Lista de síntomas observados.
        :return: El diagnóstico más probable.
        """
        probabilidades = defaultdict(float)  # Inicializa un diccionario para almacenar las probabilidades

        # Calcular la probabilidad posterior para cada enfermedad
        for enfermedad in self.probabilidades_enfermedades:
            probabilidad = self.calcular_probabilidad(enfermedad, sintomas)
            probabilidades[enfermedad] = probabilidad

        # Determinar la enfermedad con la mayor probabilidad posterior
        enfermedad_diagnostico = max(probabilidades, key=probabilidades.get)
        return enfermedad_diagnostico, probabilidades[enfermedad_diagnostico]

# Ejemplo de uso del modelo
if __name__ == "__main__":
    modelo = ModeloProbabilistaRacional()
    sintomas_ingresados = ['tos', 'fiebre']  # Síntomas que el usuario reporta
    diagnostico, probabilidad = modelo.diagnosticar(sintomas_ingresados)

    # Imprimir el diagnóstico y su probabilidad
    print(f"Diagnóstico probable: {diagnostico} con probabilidad {probabilidad:.2f}")
"""
Clase ModeloProbabilistaRacional: Representa un modelo que utiliza probabilidades para hacer inferencias.

Método __init__: Inicializa las probabilidades previas de enfermedades y las probabilidades condicionales de los síntomas.

Método calcular_probabilidad: Calcula la probabilidad posterior de una enfermedad dado un conjunto de síntomas utilizando el Teorema de Bayes. Este método multiplica la probabilidad previa de la enfermedad por la probabilidad de los síntomas dado la enfermedad.

Método diagnosticar: Recibe una lista de síntomas y calcula la probabilidad posterior para cada enfermedad, luego determina cuál enfermedad tiene la mayor probabilidad y la devuelve.

Bloque if __name__ == "__main__": Este bloque ejecuta un ejemplo de uso del modelo, donde se ingresan síntomas y se imprime el diagnóstico más probable.

Ejemplo de Ejecución
Si ejecutas el código y proporcionas los síntomas ['tos', 'fiebre'], obtendrás un diagnóstico que probablemente sea "Gripe" con una probabilidad significativa, ya que esos síntomas están más alineados con esa enfermedad según las probabilidades definidas.
"""