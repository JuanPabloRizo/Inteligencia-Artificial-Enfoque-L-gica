# Clase para representar una regla lógica
class Regla:
    def __init__(self, premisas, conclusion):
        """
        Inicializa una regla con premisas y una conclusión.
        
        :param premisas: Lista de premisas que forman la regla (ej. ["A", "B"]).
        :param conclusion: Conclusión que se infiere si se cumplen las premisas (ej. "C").
        """
        self.premisas = premisas  # Almacena las premisas de la regla
        self.conclusion = conclusion  # Almacena la conclusión de la regla

    def __str__(self):
        """Devuelve una representación en cadena de la regla."""
        premisas_str = ", ".join(self.premisas)
        return f"Si {premisas_str}, entonces {self.conclusion}"


# Clase para representar una red semántica
class RedSemantica:
    def __init__(self):
        """Inicializa la red semántica como un diccionario."""
        self.red = {}  # Diccionario para almacenar relaciones

    def agregar_relacion(self, concepto1, concepto2, relacion):
        """
        Agrega una relación entre dos conceptos a la red semántica.
        
        :param concepto1: Primer concepto (ej. "Perro").
        :param concepto2: Segundo concepto (ej. "Animal").
        :param relacion: Tipo de relación (ej. "es un tipo de").
        """
        if concepto1 not in self.red:
            self.red[concepto1] = []  # Inicializa una lista para el concepto1
        self.red[concepto1].append((relacion, concepto2))  # Agrega la relación

    def mostrar_red(self):
        """Muestra todas las relaciones en la red semántica."""
        print("Red Semántica:")
        for concepto, relaciones in self.red.items():
            for relacion, concepto_relacionado in relaciones:
                print(f"{concepto} {relacion} {concepto_relacionado}")


# Clase para representar un sistema que utiliza reglas y redes semánticas
class Sistema:
    def __init__(self):
        """Inicializa el sistema con una lista de reglas y una red semántica."""
        self.reglas = []  # Lista para almacenar reglas
        self.red_seman = RedSemantica()  # Instancia de la red semántica

    def agregar_regla(self, regla):
        """
        Agrega una regla al sistema.
        
        :param regla: Instancia de la clase Regla a agregar.
        """
        self.reglas.append(regla)  # Agrega la regla a la lista

    def inferir(self):
        """Realiza inferencias basadas en las reglas."""
        print("Realizando inferencias:")
        for regla in self.reglas:
            print(regla)  # Imprime cada regla al hacer la inferencia

    def agregar_relacion_a_red(self, concepto1, concepto2, relacion):
        """Agrega una relación a la red semántica."""
        self.red_seman.agregar_relacion(concepto1, concepto2, relacion)

    def mostrar_red_seman(self):
        """Muestra la red semántica del sistema."""
        self.red_seman.mostrar_red()


# Ejemplo de uso
if __name__ == "__main__":
    # Crear un sistema
    sistema = Sistema()

    # Agregar reglas
    sistema.agregar_regla(Regla(["El cielo es azul"], "Es un día soleado"))
    sistema.agregar_regla(Regla(["El perro es un animal"], "El perro tiene un corazón"))

    # Realizar inferencias
    sistema.inferir()

    # Agregar relaciones a la red semántica
    sistema.agregar_relacion_a_red("Perro", "Animal", "es un tipo de")
    sistema.agregar_relacion_a_red("Gato", "Animal", "es un tipo de")

    # Mostrar la red semántica
    sistema.mostrar_red_seman()
"""
Clase Regla:

Constructor (__init__): Inicializa una regla con un conjunto de premisas y una conclusión. Las premisas son condiciones que deben cumplirse para que la conclusión sea verdadera.
Método __str__: Proporciona una representación en cadena de la regla para facilitar la impresión.
Clase RedSemantica:

Constructor (__init__): Inicializa la red semántica como un diccionario, donde las claves son conceptos y los valores son listas de relaciones con otros conceptos.
Método agregar_relacion: Permite agregar una relación entre dos conceptos. La relación puede ser de varios tipos (por ejemplo, "es un tipo de").
Método mostrar_red: Imprime todas las relaciones que se han agregado a la red semántica.
Clase Sistema:

Constructor (__init__): Inicializa el sistema con una lista de reglas y una instancia de la red semántica.
Método agregar_regla: Agrega una regla al sistema.
Método inferir: Realiza inferencias basadas en las reglas. Aquí, simplemente se imprimen las reglas para mostrar cómo funciona el sistema.
Método agregar_relacion_a_red: Permite agregar relaciones a la red semántica.
Método mostrar_red_seman: Muestra la red semántica actual del sistema.
Ejemplo de Uso:

Se crea un sistema que permite agregar reglas y realizar inferencias.
Se agregan algunas reglas que relacionan conceptos y se imprimen.
Se agregan relaciones a la red semántica y se muestran todas las relaciones.
"""