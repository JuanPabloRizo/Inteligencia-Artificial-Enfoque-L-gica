# Clase para representar un evento
class Evento:
    def __init__(self, descripcion):
        """
        Inicializa un evento con una descripción.
        
        :param descripcion: Descripción del evento (ej. "Juan come una manzana").
        """
        self.descripcion = descripcion  # Almacena la descripción del evento

    def __str__(self):
        """Devuelve una representación en cadena del evento."""
        return f"Evento: {self.descripcion}"


# Clase para representar creencias
class Creencia:
    def __init__(self, proposicion):
        """
        Inicializa una creencia con una proposición.
        
        :param proposicion: Proposición que representa la creencia (ej. "Juan tiene hambre").
        """
        self.proposicion = proposicion  # Almacena la proposición de la creencia

    def __str__(self):
        """Devuelve una representación en cadena de la creencia."""
        return f"Creencia: {self.proposicion}"


# Clase para representar un agente que tiene creencias y puede procesar eventos
class Agente:
    def __init__(self):
        """
        Inicializa el agente con una lista de creencias.
        """
        self.creencias = []  # Lista para almacenar las creencias del agente

    def agregar_creencia(self, creencia):
        """
        Agrega una creencia al agente.
        
        :param creencia: Instancia de la clase Creencia a agregar.
        """
        self.creencias.append(creencia)  # Agrega la creencia a la lista

    def procesar_evento(self, evento):
        """
        Procesa un evento y actualiza las creencias del agente en consecuencia.
        
        :param evento: Instancia de la clase Evento que se va a procesar.
        """
        print(f"Procesando: {evento}")  # Imprime el evento que se está procesando
        # Basado en el evento, se pueden actualizar las creencias
        if "come" in evento.descripcion:  # Si el evento implica que alguien come
            self.agregar_creencia(Creencia("El agente cree que tiene hambre."))  # Se agrega una creencia de hambre

    def mostrar_creencias(self):
        """Muestra todas las creencias del agente."""
        print("Creencias del agente:")
        for creencia in self.creencias:
            print(creencia)  # Imprime cada creencia

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un evento
    evento_comer = Evento("Juan come una manzana")

    # Crear un agente
    agente = Agente()

    # Procesar el evento
    agente.procesar_evento(evento_comer)

    # Mostrar las creencias del agente
    agente.mostrar_creencias()
"""
Clase Evento:

Constructor (__init__): Inicializa un evento con una descripción, que es un texto que representa lo que ocurrió.
Método __str__: Proporciona una representación en cadena del evento para facilitar la impresión.
Clase Creencia:

Constructor (__init__): Inicializa una creencia con una proposición que representa lo que el agente considera verdadero.
Método __str__: Proporciona una representación en cadena de la creencia.
Clase Agente:

Constructor (__init__): Inicializa un agente con una lista vacía de creencias.
Método agregar_creencia: Permite agregar una nueva creencia al agente.
Método procesar_evento: Toma un evento como argumento, lo procesa e interpreta si el evento implica una acción que afecta las creencias del agente. En este caso, si el evento indica que alguien "come", se asume que el agente tiene hambre y se agrega una creencia.
Método mostrar_creencias: Imprime todas las creencias que el agente ha registrado.
Ejemplo de Uso:

Se crea un evento que describe a Juan comiendo una manzana.
Se crea un agente y se procesa el evento. Como resultado, se actualizarán las creencias del agente.
Finalmente, se muestran todas las creencias que el agente tiene después de procesar el evento.
"""