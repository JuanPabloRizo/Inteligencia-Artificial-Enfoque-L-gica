# Clase para representar un razonador por defecto
class RazonadorPorDefecto:
    def __init__(self):
        """
        Inicializa el razonador con un conjunto de hechos conocidos y reglas.
        """
        self.hechos = set()  # Conjunto de hechos conocidos
        self.reglas = []  # Lista de reglas de inferencia

    def agregar_hecho(self, hecho):
        """
        Agrega un hecho a la base de conocimiento.
        
        :param hecho: Hecho a agregar (ej. "El canario es un pájaro").
        """
        self.hechos.add(hecho)  # Agrega el hecho al conjunto

    def agregar_regla(self, premisas, conclusion):
        """
        Agrega una regla de inferencia a la base de conocimiento.
        
        :param premisas: Lista de premisas que deben cumplirse (ej. ["El pájaro es un canario"]).
        :param conclusion: Conclusión a inferir si se cumplen las premisas (ej. "El canario puede volar").
        """
        self.reglas.append((premisas, conclusion))  # Agrega la regla como tupla

    def inferir(self):
        """
        Realiza inferencias basadas en los hechos y reglas actuales.
        """
        print("Realizando inferencias:")
        for premisas, conclusion in self.reglas:  # Itera sobre cada regla
            if all(premisa in self.hechos for premisa in premisas):  # Verifica si todas las premisas son verdaderas
                if conclusion not in self.hechos:  # Si la conclusión no es un hecho conocido
                    print(f"Inferencia: {conclusion}")  # Imprime la conclusión inferida
                    self.hechos.add(conclusion)  # Agrega la conclusión a los hechos

    def mostrar_hechos(self):
        """Muestra todos los hechos conocidos."""
        print("Hechos conocidos:")
        for hecho in self.hechos:
            print(hecho)  # Imprime cada hecho conocido

# Ejemplo de uso del razonador por defecto
if __name__ == "__main__":
    # Crear un razonador por defecto
    razonador = RazonadorPorDefecto()

    # Agregar hechos iniciales
    razonador.agregar_hecho("El canario es un pájaro")
    razonador.agregar_hecho("La mayoría de los pájaros pueden volar")

    # Agregar reglas de inferencia
    razonador.agregar_regla(["El canario es un pájaro", "La mayoría de los pájaros pueden volar"],
                            "El canario puede volar")  # Razonamiento por defecto

    # Realizar inferencias
    razonador.inferir()

    # Mostrar hechos conocidos
    razonador.mostrar_hechos()

    # Supongamos que ahora tenemos nueva información
    print("\nNueva información: El canario tiene una herida en el ala y no puede volar.")
    razonador.agregar_hecho("El canario tiene una herida en el ala")

    # Realizamos las inferencias nuevamente
    razonador.inferir()

    # Mostrar hechos conocidos después de la nueva información
    razonador.mostrar_hechos()
"""
Clase RazonadorPorDefecto:

Constructor (__init__): Inicializa el razonador con un conjunto vacío de hechos y una lista vacía de reglas.
Método agregar_hecho: Permite agregar un hecho a la base de conocimiento. Los hechos son afirmaciones que se consideran verdaderas en el contexto actual.
Método agregar_regla: Permite agregar una regla de inferencia. Cada regla está compuesta por un conjunto de premisas y una conclusión que se infiere si las premisas son verdaderas.
Método inferir: Realiza inferencias utilizando las reglas y los hechos actuales. Itera sobre cada regla y verifica si todas las premisas son verdaderas. Si lo son, se infiere la conclusión y se agrega a los hechos.
Método mostrar_hechos: Imprime todos los hechos conocidos en la base de conocimiento.
Ejemplo de Uso:

Se crea una instancia de RazonadorPorDefecto.
Se agregan hechos iniciales sobre un canario y sus capacidades de vuelo.
Se agregan reglas que inferen que un canario puede volar si es un pájaro.
Se realizan inferencias basadas en los hechos y reglas actuales, y se muestran las conclusiones inferidas.
Se introduce nueva información que indica que el canario no puede volar y se realizan las inferencias nuevamente para mostrar cómo el razonador se adapta a la nueva información.
"""