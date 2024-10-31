# Clase para representar un objeto en la taxonomía
class Objeto:
    def __init__(self, nombre, descripcion):
        """
        Inicializa un objeto con su nombre y descripción.
        
        :param nombre: Nombre del objeto.
        :param descripcion: Descripción del objeto.
        """
        self.nombre = nombre  # Nombre del objeto
        self.descripcion = descripcion  # Descripción del objeto

    def __str__(self):
        """Devuelve una representación en cadena del objeto."""
        return f"{self.nombre}: {self.descripcion}"


# Clase para representar una categoría en la taxonomía
class Categoria:
    def __init__(self, nombre):
        """
        Inicializa una categoría con su nombre y lista de subcategorías y objetos.
        
        :param nombre: Nombre de la categoría.
        """
        self.nombre = nombre  # Nombre de la categoría
        self.subcategorias = []  # Lista para almacenar subcategorías
        self.objetos = []  # Lista para almacenar objetos en esta categoría

    def agregar_subcategoria(self, subcategoria):
        """
        Agrega una subcategoría a la categoría.
        
        :param subcategoria: Subcategoría a agregar.
        """
        self.subcategorias.append(subcategoria)  # Agrega la subcategoría a la lista

    def agregar_objeto(self, objeto):
        """
        Agrega un objeto a la categoría.
        
        :param objeto: Objeto a agregar.
        """
        self.objetos.append(objeto)  # Agrega el objeto a la lista

    def mostrar(self, nivel=0):
        """
        Muestra la categoría y sus subcategorías y objetos de manera jerárquica.
        
        :param nivel: Nivel de indentación para mostrar jerarquía.
        """
        indentacion = "  " * nivel  # Indentación basada en el nivel
        print(f"{indentacion}- {self.nombre}")  # Muestra el nombre de la categoría

        # Muestra los objetos en esta categoría
        for objeto in self.objetos:
            print(f"{indentacion}  * {objeto}")

        # Muestra las subcategorías
        for subcategoria in self.subcategorias:
            subcategoria.mostrar(nivel + 1)  # Llama recursivamente para mostrar subcategorías


# Ejemplo de uso de la taxonomía
if __name__ == "__main__":
    # Crear categorías
    animales = Categoria("Animales")
    mamiferos = Categoria("Mamíferos")
    aves = Categoria("Aves")

    # Crear objetos
    leon = Objeto("León", "Un gran mamífero carnívoro.")
    elefante = Objeto("Elefante", "El mamífero terrestre más grande.")
    condor = Objeto("Cóndor", "Un ave de gran tamaño que vuela a gran altura.")

    # Agregar objetos a las categorías correspondientes
    mamiferos.agregar_objeto(leon)
    mamiferos.agregar_objeto(elefante)
    aves.agregar_objeto(condor)

    # Agregar subcategorías a la categoría principal
    animales.agregar_subcategoria(mamiferos)
    animales.agregar_subcategoria(aves)

    # Mostrar la taxonomía
    print("Taxonomía de Animales:")
    animales.mostrar()
"""
Definición de la Clase Objeto:

Esta clase representa un objeto que tiene un nombre y una descripción.
El método __str__ proporciona una representación en cadena del objeto, facilitando su visualización.
Definición de la Clase Categoria:

Esta clase representa una categoría que puede contener subcategorías y objetos.
Los métodos agregar_subcategoria y agregar_objeto permiten agregar subcategorías y objetos a la categoría.
El método mostrar imprime la categoría y sus subcategorías y objetos de manera jerárquica, utilizando indentación para mostrar la estructura.
Ejemplo de Uso:

Se crean varias categorías, como Animales, Mamíferos y Aves.
Se crean objetos representativos de estas categorías, como un león, un elefante y un cóndor.
Se agregan objetos a las categorías correspondientes y se organizan jerárquicamente.
Finalmente, se llama al método mostrar para imprimir la taxonomía de animales en la consola.
"""