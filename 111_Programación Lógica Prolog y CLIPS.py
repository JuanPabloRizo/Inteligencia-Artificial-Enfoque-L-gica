# Importamos las librerías necesarias para trabajar con Prolog y CLIPS
from pyswip import Prolog  # Para Prolog
import clips  # Para CLIPS

# Función para trabajar con Prolog
def ejecutar_prolog():
    # Crear una instancia del motor Prolog
    prolog = Prolog()

    # Agregamos hechos a Prolog. Estos hechos representan las relaciones padre-hijo.
    prolog.assertz("padre(juan, maria)")  # Juan es el padre de María
    prolog.assertz("padre(juan, pedro)")  # Juan es el padre de Pedro
    prolog.assertz("madre(ana, maria)")   # Ana es la madre de María
    prolog.assertz("madre(ana, pedro)")   # Ana es la madre de Pedro

    # Definimos una regla en Prolog: dos personas son hermanos si tienen el mismo padre y no son la misma persona.
    prolog.assertz("hermano(X, Y) :- padre(Z, X), padre(Z, Y), X \= Y")

    # Hacemos una consulta: ¿María es hermana de Pedro?
    resultado = list(prolog.query("hermano(maria, pedro)"))

    # Mostrar los resultados de la consulta
    if resultado:
        print("Prolog: María es hermana de Pedro")
    else:
        print("Prolog: María no es hermana de Pedro")


# Función para trabajar con CLIPS
def ejecutar_clips():
    # Creamos un entorno de CLIPS para manejar reglas y hechos
    env = clips.Environment()

    # Definimos una regla en CLIPS para determinar si dos personas son hermanos.
    # La regla dice que si Juan es padre de dos personas diferentes, entonces esas dos personas son hermanos.
    env.build("""
    (defrule regla-hermanos
       (padre juan ?hijo1)  ; Si Juan es el padre de ?hijo1
       (padre juan ?hijo2)  ; y Juan también es el padre de ?hijo2
       (neq ?hijo1 ?hijo2)  ; y ?hijo1 no es igual a ?hijo2
       =>
       (assert (hermanos ?hijo1 ?hijo2)))  ; Entonces podemos afirmar que ?hijo1 y ?hijo2 son hermanos
    """)

    # Agregamos hechos a la base de conocimientos de CLIPS
    env.assert_string("(padre juan maria)")  # Juan es el padre de María
    env.assert_string("(padre juan pedro)")  # Juan es el padre de Pedro

    # Ejecutamos las reglas en CLIPS
    env.run()

    # Consultamos si se ha inferido que María y Pedro son hermanos
    for fact in env.facts():
        if "hermanos" in fact.template.name:
            print(f"CLIPS: {fact[0]} es hermano/a de {fact[1]}")  # Imprimimos los hermanos inferidos


# Función principal que ejecuta ambos lenguajes
def main():
    # Ejecutar lógica Prolog
    print("Ejecutando Prolog:")
    ejecutar_prolog()  # Llamamos a la función que trabaja con Prolog
    
    # Ejecutar lógica CLIPS
    print("\nEjecutando CLIPS:")
    ejecutar_clips()  # Llamamos a la función que trabaja con CLIPS


# Llamamos a la función principal si este archivo se ejecuta directamente
if __name__ == "__main__":
    main()
