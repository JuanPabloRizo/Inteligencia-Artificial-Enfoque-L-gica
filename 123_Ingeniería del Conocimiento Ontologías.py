# Importar la biblioteca rdflib para trabajar con RDF y ontologías
from rdflib import Graph, Literal, RDF, URIRef, Namespace

# 1. Crear un grafo RDF
g = Graph()  # Inicializa un nuevo grafo para almacenar la ontología

# 2. Definir un espacio de nombres para la ontología
# Esto ayuda a organizar y referenciar los recursos de manera única
EX = Namespace("http://example.org/")  # Espacio de nombres personalizado

# 3. Definir clases y propiedades de la ontología
# Agregar clases a la ontología
g.add((EX.Animal, RDF.type, RDF.Class))  # Clase base para todos los animales
g.add((EX.Mamifero, RDF.type, RDF.Class))  # Subclase de Animal
g.add((EX.Ave, RDF.type, RDF.Class))  # Subclase de Animal

# 4. Agregar propiedades para describir características
g.add((EX.tienePatas, RDF.type, RDF.Property))  # Propiedad que describe si un animal tiene patas
g.add((EX.tieneAlas, RDF.type, RDF.Property))  # Propiedad que describe si un animal tiene alas

# 5. Crear instancias de las clases
# Definir instancias de animales específicos
g.add((EX.leon, RDF.type, EX.Mamifero))  # León es un mamífero
g.add((EX.condor, RDF.type, EX.Ave))  # Cóndor es un ave

# 6. Agregar características a las instancias
# Definir si los animales tienen ciertas características
g.add((EX.leon, EX.tienePatas, Literal(True)))  # León tiene patas
g.add((EX.condor, EX.tieneAlas, Literal(True)))  # Cóndor tiene alas
g.add((EX.leon, EX.tieneAlas, Literal(False)))  # León no tiene alas

# 7. Consultar la ontología
# Realizar una consulta para encontrar todos los mamíferos
query = """
PREFIX ex: <http://example.org/>
SELECT ?animal
WHERE {
    ?animal a ex:Mamifero.
}
"""
# Ejecutar la consulta y mostrar resultados
print("Mamíferos encontrados:")
for row in g.query(query):
    print(row.animal)

# 8. Mostrar el contenido del grafo
print("\nContenido del grafo:")
for subj, pred, obj in g:
    print(f"{subj} {pred} {obj}")  # Imprimir cada triple en el grafo
"""
Importación de Bibliotecas: Se importa rdflib, que es la biblioteca utilizada para crear y manejar el grafo RDF.

Creación de un Grafo: Se inicializa un grafo vacío donde se almacenarán los datos de la ontología.

Definición del Espacio de Nombres: Se crea un espacio de nombres que ayudará a identificar de manera única los recursos en la ontología.

Definición de Clases y Propiedades: Se definen clases (como Animal, Mamifero, Ave) y propiedades (como tienePatas, tieneAlas) que describen las características de los animales.

Creación de Instancias: Se crean instancias específicas de las clases definidas, como leon y condor, que representan animales concretos.

Agregar Características: Se añaden propiedades a las instancias, indicando si el león tiene patas y alas, y si el cóndor tiene alas.

Consultas a la Ontología: Se define una consulta SPARQL para encontrar todos los mamíferos en el grafo y se ejecuta para mostrar los resultados.

Mostrar el Contenido del Grafo: Se imprime el contenido del grafo, mostrando todas las relaciones y entidades definidas en la ontología.
"""