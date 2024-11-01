class SistemaClasificacion:
    def __init__(self):
        # Definir un conjunto de reglas para la clasificación
        self.reglas = {
            'Es A': lambda x: x['atributo1'] == 'alto' and x['atributo2'] == 'rojo',
            'Es B': lambda x: x['atributo1'] == 'bajo' and x['atributo2'] == 'verde',
            'Es C': lambda x: x['atributo1'] == 'medio' and x['atributo2'] == 'azul'
        }

    def clasificar(self, datos):
        # Clasificar los datos y proporcionar explicaciones
        resultados = {}
        for i, dato in enumerate(datos):
            resultado = self.clasificar_dato(dato)
            resultados[f'Dato {i + 1}'] = resultado
        return resultados

    def clasificar_dato(self, dato):
        # Clasificar un solo dato según las reglas
        for etiqueta, regla in self.reglas.items():
            if regla(dato):
                # Retornar la etiqueta y la explicación
                return {
                    'etiqueta': etiqueta,
                    'explicacion': f"{etiqueta} porque atributo1 es '{dato['atributo1']}' y atributo2 es '{dato['atributo2']}'"
                }
        return {'etiqueta': 'Desconocido', 'explicacion': 'No se aplicaron reglas.'}

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia del sistema de clasificación
    sistema = SistemaClasificacion()

    # Datos de entrada para la clasificación
    datos_a_clasificar = [
        {'atributo1': 'alto', 'atributo2': 'rojo'},
        {'atributo1': 'bajo', 'atributo2': 'verde'},
        {'atributo1': 'medio', 'atributo2': 'azul'},
        {'atributo1': 'bajo', 'atributo2': 'rojo'},  # Sin clasificación
    ]

    # Clasificar los datos
    resultados = sistema.clasificar(datos_a_clasificar)

    # Imprimir los resultados con explicaciones
    for dato, resultado in resultados.items():
        print(f"{dato}: Etiqueta = {resultado['etiqueta']}, Explicación = {resultado['explicacion']}")
"""
Clase SistemaClasificacion:

__init__: Define un conjunto de reglas en forma de diccionario. Cada regla se asocia con una etiqueta y es una función lambda que toma un dato como entrada.
clasificar: Toma una lista de datos, clasifica cada uno de ellos y devuelve los resultados en un diccionario.
clasificar_dato: Clasifica un solo dato verificando cada regla. Si una regla se cumple, devuelve la etiqueta correspondiente y una explicación de por qué se aplicó esa regla.
Ejemplo de Uso:

Se crean instancias del sistema de clasificación.
Se define un conjunto de datos que se clasificarán.
Se llama al método clasificar y se imprimen los resultados junto con sus explicaciones.
"""