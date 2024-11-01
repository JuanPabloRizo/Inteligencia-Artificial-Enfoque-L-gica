class Razonamiento:
    def razonamiento_deductivo(self, premisa_general, premisa_especifica):
        """Realiza razonamiento deductivo: si las premisas son ciertas, la conclusión también lo es."""
        print(f"Deducción basada en: '{premisa_general}' y '{premisa_especifica}'")
        if "mamíferos" in premisa_general and "perro" in premisa_especifica:
            conclusion = "Por lo tanto, un perro es un animal."
            print("Conclusión:", conclusion)
            return conclusion
        else:
            print("No se puede deducir una conclusión clara.")
            return None

    def razonamiento_inductivo(self, observaciones):
        """Realiza razonamiento inductivo basado en un conjunto de observaciones."""
        print(f"Observaciones: {observaciones}")
        if all("blanco" in obs for obs in observaciones):
            conclusion = "Por inducción, podemos inferir que todos los cisnes son blancos."
            print("Conclusión:", conclusion)
            return conclusion
        else:
            print("No se puede hacer una conclusión general clara.")
            return None

    def razonamiento_abductivo(self, evidencia):
        """Realiza razonamiento abductivo al ofrecer la mejor explicación para la evidencia observada."""
        print(f"Evidencia: {evidencia}")
        if "luces apagadas" in evidencia:
            conclusion = "Una posible explicación es que hay un apagón."
            print("Conclusión Abductiva:", conclusion)
            return conclusion
        else:
            print("No se encuentra una explicación clara.")
            return None

# Pruebas de los distintos tipos de razonamiento
razonamiento = Razonamiento()

# Razonamiento deductivo
razonamiento.razonamiento_deductivo("Todos los mamíferos son animales", "Un perro es un mamífero")

# Razonamiento inductivo
razonamiento.razonamiento_inductivo(["Cisne 1 es blanco", "Cisne 2 es blanco", "Cisne 3 es blanco"])

# Razonamiento abductivo
razonamiento.razonamiento_abductivo("Las luces están apagadas")
"""
Razonamiento Deductivo: La función razonamiento_deductivo toma dos premisas (general y específica) y concluye que si "todos los mamíferos son animales" y "un perro es un mamífero", entonces "un perro es un animal".

Razonamiento Inductivo: La función razonamiento_inductivo toma una lista de observaciones y, si todas contienen la palabra "blanco", induce que "todos los cisnes son blancos".

Razonamiento Abductivo: La función razonamiento_abductivo toma una evidencia y da la mejor explicación; en este caso, si las luces están apagadas, puede ser porque hay un apagón.
"""