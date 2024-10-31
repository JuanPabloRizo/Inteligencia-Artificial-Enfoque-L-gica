class EncadenamientoHaciaAtras:
    def __init__(self):
        # Inicializa la base de hechos y reglas
        self.hechos = set()
        self.reglas = []

    def agregar_hecho(self, hecho):
        # Agrega un hecho a la base de hechos
        self.hechos.add(hecho)

    def agregar_regla(self, premisas, conclusion):
        # Agrega una regla en forma de (premisas → conclusión)
        self.reglas.append((premisas, conclusion))

    def puede_inferir(self, conclusion):
        # Verifica si se puede deducir la conclusión
        if conclusion in self.hechos:
            return True  # La conclusión es un hecho

        # Verificar si hay reglas que llevan a esta conclusión
        for premisas, cons in self.reglas:
            if cons == conclusion:
                # Recursivamente verificar si las premisas se pueden probar
                if all(self.puede_inferir(premisa) for premisa in premisas):
                    return True
        return False  # No se puede deducir la conclusión

# Ejemplo de uso
if __name__ == "__main__":
    sistema = EncadenamientoHaciaAtras()
    
    # Agregar hechos iniciales
    sistema.agregar_hecho('P')  # Hecho: "P es verdadero"
    sistema.agregar_hecho('Q')  # Agregar Q como un hecho: "Q es verdadero"
    
    # Agregar reglas
    sistema.agregar_regla(['P', 'Q'], 'R')  # Regla: "Si P y Q son verdaderos, entonces R es verdadero"
    sistema.agregar_regla(['R'], 'S')        # Regla: "Si R es verdadero, entonces S es verdadero"

    # Probar si se puede inferir S
    if sistema.puede_inferir('S'):
        print("Se puede inferir S.")
    else:
        print("No se puede inferir S.")

"""
Encadenamiento Hacia Delante:

Se inicializan hechos y reglas.
Las reglas son de la forma 
premisas→conclusion.    
Se aplican las reglas repetidamente hasta que no se pueden deducir nuevos hechos.
Se imprime cada inferencia realizada.
Encadenamiento Hacia Atrás:

Similar al anterior, pero se busca comprobar si se puede llegar a una conclusión a partir de los hechos existentes.
Si la conclusión es un hecho, se devuelve True. Si no, se buscan reglas que lleven a la conclusión y se verifica recursivamente.
"""