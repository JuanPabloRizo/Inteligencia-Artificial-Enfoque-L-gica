# Clase para representar un sistema de encadenamiento en lógica de primer orden
class SistemaInferencia:
    def __init__(self):
        # Base de conocimientos donde se almacenan los hechos
        self.base_de_conocimiento = set()
        # Conjunto de reglas, cada una definida por premisas y conclusión
        self.reglas = []

    def agregar_hecho(self, hecho):
        """ Agrega un hecho a la base de conocimiento """
        self.base_de_conocimiento.add(hecho)

    def agregar_regla(self, premisas, conclusion):
        """ Agrega una regla (premisas => conclusión) a la base de conocimiento """
        self.reglas.append((premisas, conclusion))

    def encadenamiento_hacia_adelante(self):
        """ Realiza encadenamiento hacia adelante para deducir nuevos hechos """
        nuevo_hecho = True
        while nuevo_hecho:
            nuevo_hecho = False
            for premisas, conclusion in self.reglas:
                # Si todas las premisas de la regla están en la base de conocimiento
                if all(premisa in self.base_de_conocimiento for premisa in premisas):
                    # Y la conclusión no está en la base, se añade
                    if conclusion not in self.base_de_conocimiento:
                        print(f"Inferencia hacia adelante: {conclusion}")
                        self.base_de_conocimiento.add(conclusion)
                        nuevo_hecho = True

    def encadenamiento_hacia_atras(self, objetivo):
        """ Realiza encadenamiento hacia atrás para intentar probar el objetivo """
        # Si el objetivo ya está en la base de conocimiento
        if objetivo in self.base_de_conocimiento:
            print(f"El hecho {objetivo} ya está en la base de conocimiento.")
            return True
        
        # Recorremos las reglas para encontrar alguna que pueda inferir el objetivo
        for premisas, conclusion in self.reglas:
            if conclusion == objetivo:
                print(f"Probando si se puede inferir {objetivo} a través de {premisas}")
                # Intentamos demostrar todas las premisas de la regla
                if all(self.encadenamiento_hacia_atras(premisa) for premisa in premisas):
                    # Si todas las premisas son demostrables, añadimos el objetivo
                    self.base_de_conocimiento.add(objetivo)
                    print(f"Inferencia hacia atrás: {objetivo}")
                    return True
        
        # Si no se puede demostrar el objetivo
        print(f"No se pudo demostrar {objetivo}.")
        return False

# Ejemplo de uso
if __name__ == "__main__":
    # Crear sistema de inferencia
    sistema = SistemaInferencia()

    # Agregar hechos a la base de conocimiento
    sistema.agregar_hecho("humano(Sócrates)")

    # Agregar reglas a la base de conocimiento
    # Ejemplo: si algo es humano, entonces es mortal
    sistema.agregar_regla(["humano(X)"], "mortal(X)")

    # Encadenamiento hacia adelante para inferir hechos adicionales
    sistema.encadenamiento_hacia_adelante()

    # Encadenamiento hacia atrás para verificar si Sócrates es mortal
    if sistema.encadenamiento_hacia_atras("mortal(Sócrates)"):
        print("Conclusión: Sócrates es mortal.")
    else:
        print("No se pudo concluir si Sócrates es mortal.")
"""
Clase SistemaInferencia:
Esta clase representa el sistema de inferencia basado en lógica de primer orden.

Método agregar_hecho: Agrega un hecho a la base de conocimiento.
Método agregar_regla: Agrega una regla definida por premisas y una conclusión.
Método encadenamiento_hacia_adelante: Busca deducir nuevos hechos a partir de los hechos actuales y las reglas, agregando nuevas conclusiones cuando se cumplen las premisas.
Método encadenamiento_hacia_atras: Intenta probar un objetivo partiendo de reglas que lo podrían concluir, verificando recursivamente cada premisa.
Ejemplo de Uso:

Hechos: Añadimos que Sócrates es humano (humano(Sócrates)).
Reglas: Si X es humano, entonces X es mortal.
Encadenamiento hacia adelante: Intentamos deducir hechos automáticamente. En este caso, deduciríamos que mortal(Sócrates).
Encadenamiento hacia atrás: Intentamos probar si Sócrates es mortal al verificar las premisas necesarias.
"""