# Clase para representar un Sistema Experto de Diagnóstico
class SistemaExperto:
    def __init__(self):
        """Inicializa la base de conocimiento y el motor de inferencia."""
        self.base_de_conocimiento = {}  # Diccionario para almacenar reglas de diagnóstico
        self.sintomas = []  # Lista para almacenar síntomas ingresados por el usuario

    def agregar_regla(self, enfermedad, sintomas):
        """
        Agrega una regla a la base de conocimiento.
        
        :param enfermedad: Nombre de la enfermedad.
        :param sintomas: Lista de síntomas asociados con la enfermedad.
        """
        self.base_de_conocimiento[enfermedad] = sintomas  # Almacena la enfermedad y sus síntomas

    def diagnosticar(self):
        """Realiza el diagnóstico basado en los síntomas conocidos."""
        print("Diagnóstico basado en los síntomas ingresados:")
        # Verifica si hay síntomas ingresados
        if not self.sintomas:
            print("No se han ingresado síntomas.")
            return
        
        print(f"Sintomas ingresados: {self.sintomas}")  # Imprime los síntomas ingresados

        # Itera a través de cada enfermedad en la base de conocimiento
        for enfermedad, sintomas in self.base_de_conocimiento.items():
            print(f"Verificando enfermedad: {enfermedad} con síntomas {sintomas}")  # Muestra la enfermedad y sus síntomas
            # Verifica si todos los síntomas de la enfermedad están presentes
            if all(sintoma in self.sintomas for sintoma in sintomas):
                print(f"Posible enfermedad: {enfermedad}")  # Imprime la enfermedad diagnosticada
        
        # Si no se encontró ninguna enfermedad coincidente
        if all(not all(sintoma in self.sintomas for sintoma in sintomas) for sintomas in self.base_de_conocimiento.values()):
            print("No se encontró ninguna enfermedad que coincida con los síntomas ingresados.")

    def ingresar_sintomas(self):
        """Permite al usuario ingresar síntomas."""
        while True:
            sintoma = input("Ingresa un síntoma (o 'salir' para terminar): ")
            if sintoma.lower() == 'salir':
                break
            self.sintomas.append(sintoma)  # Agrega el síntoma a la lista

# Ejemplo de uso del sistema experto
if __name__ == "__main__":
    # Crear un sistema experto
    sistema = SistemaExperto()

    # Agregar reglas de diagnóstico
    sistema.agregar_regla('Gripe', ['fiebre', 'tos', 'dolor de cabeza'])
    sistema.agregar_regla('Resfriado', ['tos', 'estornudos', 'dolor de garganta'])
    sistema.agregar_regla('Alergia', ['estornudos', 'picazón', 'ojos llorosos'])

    # Ingresar síntomas
    sistema.ingresar_sintomas()

    # Realizar diagnóstico
    sistema.diagnosticar()
"""
Clase SistemaExperto:

Constructor (__init__): Inicializa la base de conocimiento como un diccionario y una lista para almacenar los síntomas ingresados por el usuario.
Método agregar_regla: Permite agregar una regla a la base de conocimiento. La regla consiste en una enfermedad y una lista de síntomas asociados.
Método diagnosticar: Realiza el diagnóstico basado en los síntomas ingresados. Itera a través de las enfermedades en la base de conocimiento y verifica si todos los síntomas de una enfermedad están presentes en la lista de síntomas. Si es así, imprime la posible enfermedad diagnosticada.
Método ingresar_sintomas: Permite al usuario ingresar síntomas. El usuario puede ingresar síntomas uno por uno hasta que escriba 'salir'.
Ejemplo de Uso:

Se crea una instancia de SistemaExperto.
Se agregan reglas de diagnóstico para diferentes enfermedades y sus síntomas asociados.
El sistema permite al usuario ingresar síntomas.
Finalmente, el sistema diagnostica posibles enfermedades basándose en los síntomas ingresados.
"""