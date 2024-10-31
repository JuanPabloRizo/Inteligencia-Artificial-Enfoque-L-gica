# Clase para representar un sistema de lógica no monotónica
class SistemaLogicaNoMonotonica:
    def __init__(self):
        # Base de conocimiento inicial con hechos
        self.base_de_conocimiento = set()
        # Reglas de inferencia con suposiciones por defecto
        self.reglas = []

    def agregar_hecho(self, hecho):
        # Agregar un hecho a la base de conocimiento
        self.base_de_conocimiento.add(hecho)
        print(f"Hecho agregado: {hecho}")

    def agregar_regla(self, condicion, conclusion, excepcion=None):
        # Agregar una regla de inferencia (defeasible)
        # condición: premisa que debe cumplirse
        # conclusion: conclusión derivada si la condición se cumple
        # excepcion: cuando esta premisa es verdadera, la conclusión es inválida
        self.reglas.append((condicion, conclusion, excepcion))

    def hacer_inferencias(self):
        # Realizar inferencias basado en las reglas y hechos actuales
        nuevos_hechos = True
        while nuevos_hechos:
            nuevos_hechos = False
            for condicion, conclusion, excepcion in self.reglas:
                # Verificar si la condición es válida y la excepción no se cumple
                if condicion in self.base_de_conocimiento and (excepcion is None or excepcion not in self.base_de_conocimiento):
                    if conclusion not in self.base_de_conocimiento:
                        print(f"Inferencia: {conclusion}")
                        self.base_de_conocimiento.add(conclusion)
                        nuevos_hechos = True

    def eliminar_hecho(self, hecho):
        # Eliminar un hecho de la base de conocimiento (en caso de que haya nueva información)
        if hecho in self.base_de_conocimiento:
            self.base_de_conocimiento.remove(hecho)
            print(f"Hecho eliminado: {hecho}")
        else:
            print(f"Hecho no encontrado: {hecho}")

    def consultar(self, proposicion):
        # Consultar si una proposición está en la base de conocimiento
        return proposicion in self.base_de_conocimiento


# Ejemplo de uso del sistema de lógica no monotónica
if __name__ == "__main__":
    # Crear un sistema de lógica no monotónica
    sistema = SistemaLogicaNoMonotonica()

    # Agregar hechos a la base de conocimiento
    sistema.agregar_hecho("Es de día")
    
    # Agregar reglas de inferencia
    # Si es de día, entonces probablemente está soleado, a menos que esté nublado
    sistema.agregar_regla("Es de día", "Está soleado", excepcion="Está nublado")

    # Hacer inferencias con los hechos actuales
    sistema.hacer_inferencias()

    # Consultar si está soleado
    if sistema.consultar("Está soleado"):
        print("Conclusión: Está soleado.")
    else:
        print("Conclusión: No se puede inferir que está soleado.")

    # Ahora agregamos un nuevo hecho: Está nublado
    sistema.agregar_hecho("Está nublado")

    # Volvemos a hacer inferencias
    sistema.hacer_inferencias()

    # Consultar si está soleado de nuevo (debería cambiar la inferencia)
    if sistema.consultar("Está soleado"):
        print("Conclusión: Está soleado.")
    else:
        print("Conclusión: No se puede inferir que está soleado.")
"""
Clase SistemaLogicaNoMonotonica: Esta clase representa un sistema que puede almacenar hechos, reglas de inferencia con suposiciones por defecto y excepciones, y puede realizar inferencias basadas en los hechos actuales.

Métodos principales:

agregar_hecho(hecho): Añade un hecho a la base de conocimiento.
agregar_regla(condicion, conclusion, excepcion): Añade una regla de inferencia. La inferencia se realiza solo si la condición es verdadera y no hay excepciones que la invaliden.
hacer_inferencias(): Recorre todas las reglas y realiza inferencias en función de los hechos conocidos.
eliminar_hecho(hecho): Permite eliminar un hecho de la base de conocimiento si nueva información lo invalida.
consultar(proposicion): Verifica si una proposición está en la base de conocimiento.
Ejemplo en acción:

Se agrega el hecho "Es de día" y una regla que dice que "si es de día, entonces probablemente está soleado, a menos que esté nublado".
Primero, como no está nublado, se infiere que "está soleado".
Luego, al agregar el hecho "Está nublado", la inferencia de que "está soleado" ya no es válida debido a la excepción, y el sistema ajusta sus conclusiones en consecuencia.
"""