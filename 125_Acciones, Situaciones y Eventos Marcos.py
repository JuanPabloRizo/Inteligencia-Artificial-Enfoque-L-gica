# Clase para representar un marco (frame) que contiene información sobre una situación o acción
class Marco:
    def __init__(self, nombre):
        """
        Inicializa un marco con un nombre y un diccionario para almacenar atributos.
        
        :param nombre: Nombre del marco (ej. acción, situación, evento).
        """
        self.nombre = nombre  # Nombre del marco
        self.atributos = {}  # Diccionario para almacenar atributos del marco

    def agregar_atributo(self, clave, valor):
        """
        Agrega un atributo al marco.
        
        :param clave: Nombre del atributo.
        :param valor: Valor del atributo.
        """
        self.atributos[clave] = valor  # Almacena el atributo en el diccionario

    def obtener_atributo(self, clave):
        """
        Obtiene el valor de un atributo del marco.
        
        :param clave: Nombre del atributo a obtener.
        :return: Valor del atributo, o None si no existe.
        """
        return self.atributos.get(clave, None)  # Retorna el valor del atributo, o None si no existe

    def __str__(self):
        """Devuelve una representación en cadena del marco."""
        return f"Marco: {self.nombre}, Atributos: {self.atributos}"


# Clase para representar un evento que utiliza un marco
class Evento:
    def __init__(self, marco):
        """
        Inicializa un evento basado en un marco específico.
        
        :param marco: Marco que describe el evento.
        """
        self.marco = marco  # Marco asociado al evento

    def ejecutar(self):
        """Ejecuta la acción asociada al evento."""
        print(f"Ejecutando evento: {self.marco.nombre}")
        for clave, valor in self.marco.atributos.items():
            print(f"{clave}: {valor}")  # Imprime los atributos del evento

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un marco para una acción
    comer = Marco("Comer")
    comer.agregar_atributo("quien", "Juan")  # Agregar atributo: quien
    comer.agregar_atributo("que", "manzana")  # Agregar atributo: que
    comer.agregar_atributo("donde", "cocina")  # Agregar atributo: donde

    # Crear un evento basado en el marco
    evento_comer = Evento(comer)

    # Ejecutar el evento
    evento_comer.ejecutar()  # Imprime la información del evento

    # Mostrar información del marco
    print(comer)  # Muestra el marco completo
"""
Clase Marco:

Constructor (__init__): Inicializa un marco con un nombre y un diccionario vacío para almacenar atributos.
Método agregar_atributo: Permite agregar un atributo al marco en forma de clave-valor.
Método obtener_atributo: Devuelve el valor de un atributo específico, o None si no existe.
Método __str__: Proporciona una representación en cadena del marco, mostrando su nombre y atributos.
Clase Evento:

Constructor (__init__): Inicializa un evento asociado a un marco específico.
Método ejecutar: Imprime el nombre del evento y todos sus atributos.
Ejemplo de Uso:

Se crea un marco llamado "Comer" que tiene atributos como "quien", "que", y "donde".
Se crea un evento que utiliza el marco "Comer".
Al llamar al método ejecutar, se imprime la información del evento y sus atributos.
Finalmente, se muestra la información completa del marco.
"""