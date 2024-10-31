# Clase para representar un sistema de diagnóstico basado en reglas
class SistemaDiagnostico:
    def __init__(self):
        # Inicializa la base de hechos y reglas
        self.hechos = set()  # Conjunto de hechos conocidos
        self.reglas = []     # Lista de reglas (premisas → conclusión)

    def agregar_hecho(self, hecho):
        # Agrega un hecho conocido al sistema
        self.hechos.add(hecho)

    def agregar_regla(self, premisas, conclusion):
        # Agrega una regla al sistema
        self.reglas.append((premisas, conclusion))

    def inferir(self):
        # Realiza inferencias basadas en las reglas
        cambios = True  # Variable para controlar si hubo cambios en los hechos
        while cambios:
            cambios = False  # Reiniciar cambios en cada iteración
            for premisas, conclusion in self.reglas:
                # Verificar si todas las premisas de la regla están en los hechos conocidos
                if all(premisa in self.hechos for premisa in premisas):
                    # Si la conclusión no está en los hechos, agregarla
                    if conclusion not in self.hechos:
                        print(f"Inferencia: Se concluye que {conclusion}.")
                        self.hechos.add(conclusion)  # Agregar la conclusión a los hechos
                        cambios = True  # Marcar que hubo un cambio

    def consultar(self, hecho):
        # Consulta si un hecho está en la base de hechos
        return hecho in self.hechos

# Crear una instancia del sistema de diagnóstico
sistema = SistemaDiagnostico()

# Agregar hechos conocidos
sistema.agregar_hecho('fiebre')    # Hecho 1: El paciente tiene fiebre
sistema.agregar_hecho('tos')       # Hecho 2: El paciente tiene tos

# Agregar reglas de diagnóstico
sistema.agregar_regla(['fiebre', 'tos'], 'gripe')       # Regla 1: Si tiene fiebre y tos, tiene gripe
sistema.agregar_regla(['gripe'], 'necesita reposo')      # Regla 2: Si tiene gripe, necesita reposo
sistema.agregar_regla(['tos'], 'posiblemente alergia')   # Regla 3: Si tiene tos, posiblemente tiene alergia

# Realizar inferencias
sistema.inferir()

# Consultar si el paciente necesita reposo
if sistema.consultar('necesita reposo'):
    print("El paciente necesita reposo.")
else:
    print("No se ha inferido que el paciente necesite reposo.")
"""
Definición de la Clase SistemaDiagnostico:

Se define una clase llamada SistemaDiagnostico que se utilizará para gestionar hechos y reglas de diagnóstico.
En el constructor __init__, se inicializan:
self.hechos: un conjunto vacío que almacenará los hechos conocidos.
self.reglas: una lista vacía que contendrá las reglas en forma de tuplas (premisas, conclusión).
Método agregar_hecho:

Este método permite agregar un hecho conocido al sistema.
Recibe un argumento hecho, que se añade al conjunto self.hechos.
Método agregar_regla:

Este método permite agregar una regla al sistema de diagnóstico.
Recibe dos argumentos: premisas, que es una lista de hechos necesarios para que se aplique la regla, y conclusion, que es el hecho que se infiere si se cumplen las premisas.
La regla se agrega como una tupla (premisas, conclusión) a la lista self.reglas.
Método inferir:

Este método se encarga de realizar inferencias basadas en las reglas definidas.
Se utiliza un bucle while que continúa ejecutándose mientras haya cambios en los hechos.
Dentro del bucle, se reinicia la variable cambios a False en cada iteración.
Se itera sobre cada regla en self.reglas, verificando si todas las premisas de la regla están en self.hechos.
Si todas las premisas se cumplen y la conclusión no está ya en los hechos, se imprime la inferencia realizada y se agrega la conclusión a self.hechos, marcando que hubo un cambio.
Método consultar:

Este método permite consultar si un hecho específico está presente en self.hechos.
Recibe un argumento hecho y devuelve True si el hecho está en el conjunto, o False en caso contrario.
Creación de una Instancia del Sistema de Diagnóstico:

Se crea una instancia de SistemaDiagnostico llamada sistema.
Agregar Hechos Conocidos:

Se utilizan los métodos agregar_hecho para añadir hechos sobre el estado del paciente, como tener fiebre y tos.
Agregar Reglas de Diagnóstico:

Se utilizan los métodos agregar_regla para definir reglas que relacionan los hechos:
Regla 1: Si el paciente tiene fiebre y tos, se infiere que tiene gripe.
Regla 2: Si se infiere que tiene gripe, se infiere que necesita reposo.
Regla 3: Si el paciente tiene tos, se infiere que posiblemente tiene alergia.
Realizar Inferencias:

Se llama al método inferir, que evalúa las reglas y actualiza los hechos conocidos según las inferencias realizadas.
Consultar Hechos Inferidos:

Finalmente, se consulta si el paciente necesita reposo y se imprime el resultado.
"""