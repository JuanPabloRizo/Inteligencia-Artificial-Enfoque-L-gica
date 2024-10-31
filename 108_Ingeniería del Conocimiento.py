# Clase para representar un sistema experto simple
class SistemaExperto:
    def __init__(self):
        # Base de conocimiento con reglas (si-síntoma entonces enfermedad)
        self.reglas = {
            'fiebre y tos': 'gripe',
            'fiebre y dolor de cabeza': 'meningitis',
            'tos y dolor de garganta': 'faringitis',
            'dolor de cabeza y fatiga': 'migraña'
        }

    def diagnosticar(self, sintomas):
        # Diagnosticar enfermedad basada en síntomas dados
        for regla, enfermedad in self.reglas.items():
            if all(sintoma in sintomas for sintoma in regla.split(' y ')):
                return enfermedad
        return "No se pudo determinar la enfermedad."

# Ejemplo de uso del sistema experto
if __name__ == "__main__":
    # Crear instancia del sistema experto
    experto = SistemaExperto()

    # Lista de síntomas del paciente
    sintomas_paciente = ['fiebre', 'tos']

    # Diagnosticar enfermedad
    resultado = experto.diagnosticar(sintomas_paciente)
    print(f"Diagnóstico: {resultado}")
"""
Definición de la Clase SistemaExperto:

Se inicializa la clase que contendrá las reglas del sistema experto.
Inicialización de Reglas:

Se define un diccionario reglas donde cada clave es una combinación de síntomas y su valor correspondiente es la enfermedad que se diagnostica si se presentan esos síntomas.
Método diagnosticar:

Este método toma una lista de síntomas como entrada y verifica si coincide con alguna de las reglas definidas.
Se usa un bucle for para iterar sobre las reglas. Si los síntomas coinciden con la clave de la regla, se devuelve la enfermedad asociada.
Ejemplo de Uso:

Se crea una instancia de SistemaExperto.
Se define una lista de síntomas que el paciente presenta.
Se llama al método diagnosticar para obtener el diagnóstico y se imprime el resultado.
"""