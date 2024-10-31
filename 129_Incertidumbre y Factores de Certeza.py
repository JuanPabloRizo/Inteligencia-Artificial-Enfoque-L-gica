# Clase para representar un sistema de inferencia basado en certeza
class SistemaDeInferencia:
    def __init__(self):
        """Inicializa el sistema de inferencia con un conjunto de hechos y reglas."""
        self.hechos = {}  # Diccionario para almacenar hechos y sus niveles de certeza
        self.reglas = []  # Lista de reglas de inferencia

    def agregar_hecho(self, hecho, certeza):
        """
        Agrega un hecho a la base de conocimiento con su nivel de certeza.
        
        :param hecho: Hecho a agregar (ej. "El cielo es azul").
        :param certeza: Nivel de certeza del hecho (valor entre 0 y 1).
        """
        self.hechos[hecho] = certeza  # Almacena el hecho y su certeza

    def agregar_regla(self, premisas, conclusion):
        """
        Agrega una regla de inferencia a la base de conocimiento.
        
        :param premisas: Lista de premisas (hechos que deben cumplirse).
        :param conclusion: Conclusión a inferir si se cumplen las premisas.
        """
        self.reglas.append((premisas, conclusion))  # Agrega la regla como tupla

    def inferir(self):
        """Realiza inferencias basadas en los hechos y reglas actuales."""
        print("Realizando inferencias:")
        for premisas, conclusion in self.reglas:  # Itera sobre cada regla
            # Verifica si todas las premisas son verdaderas y calcula la certeza
            if all(premisa in self.hechos for premisa in premisas):
                # Calcula el nivel de certeza de la conclusión basado en las premisas
                certeza_conclusion = min(self.hechos[premisa] for premisa in premisas)
                # Almacena la conclusión con su certeza
                self.hechos[conclusion] = certeza_conclusion
                print(f"Inferencia: {conclusion} (Certeza: {certeza_conclusion})")

    def mostrar_hechos(self):
        """Muestra todos los hechos y sus niveles de certeza."""
        print("Hechos conocidos y niveles de certeza:")
        for hecho, certeza in self.hechos.items():
            print(f"{hecho}: Certeza = {certeza:.2f}")  # Imprime cada hecho y su certeza

# Ejemplo de uso del sistema de inferencia
if __name__ == "__main__":
    # Crear un sistema de inferencia
    sistema = SistemaDeInferencia()

    # Agregar hechos iniciales con sus niveles de certeza
    sistema.agregar_hecho("El cielo es azul", 0.9)  # Certeza alta
    sistema.agregar_hecho("Es un día despejado", 0.8)  # Certeza alta

    # Agregar reglas de inferencia
    sistema.agregar_regla(["El cielo es azul", "Es un día despejado"], "El clima es bueno")  # Inferencia

    # Realizar inferencias
    sistema.inferir()

    # Mostrar hechos conocidos y sus niveles de certeza
    sistema.mostrar_hechos()
"""
Clase SistemaDeInferencia:

Constructor (__init__): Inicializa el sistema de inferencia con un diccionario para almacenar hechos (junto con sus niveles de certeza) y una lista para las reglas de inferencia.
Método agregar_hecho: Permite agregar un hecho a la base de conocimiento, junto con su nivel de certeza, que debe estar entre 0 y 1.
Método agregar_regla: Permite agregar una regla de inferencia, que consiste en un conjunto de premisas y una conclusión.
Método inferir: Realiza inferencias basadas en los hechos y reglas actuales. Verifica si todas las premisas son verdaderas y calcula la certeza de la conclusión como el mínimo de las certezas de las premisas. Agrega la conclusión a los hechos junto con su certeza.
Método mostrar_hechos: Imprime todos los hechos conocidos y sus niveles de certeza.
Ejemplo de Uso:

Se crea una instancia de SistemaDeInferencia.
Se agregan hechos iniciales (como el estado del cielo y el clima) con sus niveles de certeza.
Se agregan reglas que inferen el clima basándose en los hechos.
Se realizan inferencias y se muestran los hechos conocidos junto con sus niveles de certeza.
"""