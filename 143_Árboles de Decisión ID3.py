import math
from collections import Counter

class NodoArbol:
    def __init__(self, atributo=None, hijos=None, etiqueta=None):
        self.atributo = atributo  # Atributo por el cual se divide en este nodo
        self.hijos = hijos if hijos is not None else {}  # Diccionario de hijos del nodo
        self.etiqueta = etiqueta  # Etiqueta de clase si es una hoja

# Función para calcular la entropía de un conjunto de datos
def calcular_entropia(datos):
    # Contar las etiquetas
    etiquetas = [fila[-1] for fila in datos]
    total = len(etiquetas)
    frecuencia = Counter(etiquetas)
    
    # Calcular la entropía
    entropia = 0
    for cuenta in frecuencia.values():
        probabilidad = cuenta / total
        entropia -= probabilidad * math.log2(probabilidad)
    return entropia

# Función para calcular la ganancia de información de un atributo
def calcular_ganancia(datos, atributo):
    entropia_inicial = calcular_entropia(datos)
    total = len(datos)
    
    # Dividir los datos según los valores del atributo
    valores = set(fila[atributo] for fila in datos)
    entropia_ponderada = 0
    for valor in valores:
        subconjunto = [fila for fila in datos if fila[atributo] == valor]
        entropia_ponderada += (len(subconjunto) / total) * calcular_entropia(subconjunto)
    
    # Calcular la ganancia de información
    ganancia = entropia_inicial - entropia_ponderada
    return ganancia

# Función principal de ID3 para construir el árbol
def id3(datos, atributos):
    etiquetas = [fila[-1] for fila in datos]
    
    # Si todas las instancias tienen la misma etiqueta, devolver una hoja
    if len(set(etiquetas)) == 1:
        return NodoArbol(etiqueta=etiquetas[0])
    
    # Si no hay más atributos para dividir, devolver una hoja con la etiqueta más común
    if not atributos:
        etiqueta_comun = Counter(etiquetas).most_common(1)[0][0]
        return NodoArbol(etiqueta=etiqueta_comun)
    
    # Elegir el mejor atributo basado en la ganancia de información
    ganancias = [(atributo, calcular_ganancia(datos, atributo)) for atributo in atributos]
    mejor_atributo = max(ganancias, key=lambda x: x[1])[0]
    
    # Crear el nodo raíz con el mejor atributo
    nodo = NodoArbol(atributo=mejor_atributo)
    
    # Dividir los datos por el valor del mejor atributo y construir subárboles
    valores = set(fila[mejor_atributo] for fila in datos)
    for valor in valores:
        subconjunto = [fila for fila in datos if fila[mejor_atributo] == valor]
        if subconjunto:
            # Crear subárbol para cada subconjunto, excluyendo el atributo usado
            subatributos = [a for a in atributos if a != mejor_atributo]
            nodo.hijos[valor] = id3(subconjunto, subatributos)
    
    return nodo

# Función para hacer predicciones con el árbol de decisión
def predecir(nodo, instancia):
    # Si el nodo es una hoja, devolver su etiqueta
    if nodo.etiqueta is not None:
        return nodo.etiqueta
    
    # Elegir el atributo y el valor para el siguiente nodo
    valor_atributo = instancia[nodo.atributo]
    if valor_atributo in nodo.hijos:
        return predecir(nodo.hijos[valor_atributo], instancia)
    else:
        return None  # Si no hay coincidencia en los valores, devuelve None

# Ejemplo de datos para construir el árbol de decisión
# Cada fila es una instancia: [atributo1, atributo2, ..., etiqueta]
datos = [
    ["sol", "calor", "alta", "no"],
    ["sol", "calor", "normal", "si"],
    ["nublado", "calor", "alta", "si"],
    ["lluvia", "frío", "alta", "si"],
    ["lluvia", "fresco", "normal", "no"],
    ["nublado", "frío", "normal", "si"],
    ["sol", "fresco", "alta", "no"],
    ["lluvia", "fresco", "normal", "si"]
]

# Atributos que usaremos (índices de las columnas de atributos en datos)
atributos = [0, 1, 2]  # ["clima", "temperatura", "humedad"]

# Construir el árbol de decisión
arbol = id3(datos, atributos)

# Prueba de predicción
instancia = ["lluvia", "fresco", "alta"]  # Clima: lluvia, temperatura: fresco, humedad: alta
prediccion = predecir(arbol, instancia)
print(f"Predicción para {instancia}: {prediccion}")
"""
NodoArbol: Representa cada nodo del árbol. Almacena el atributo que se usa para dividir y los posibles hijos (subárboles) o la etiqueta si es una hoja.

calcular_entropia: Calcula la entropía de un conjunto de datos. La entropía mide la incertidumbre; entre más baja, mejor está clasificado el conjunto.

calcular_ganancia: Calcula la ganancia de información de un atributo específico. La ganancia de información mide cuánto se reduce la entropía al dividir el conjunto según ese atributo.

id3: Función principal para construir el árbol. Selecciona el mejor atributo según la ganancia de información y lo utiliza como nodo raíz. Divide los datos por el valor de ese atributo y construye subárboles recursivamente para cada valor posible.

predecir: Hace una predicción utilizando el árbol de decisión. Si el nodo es una hoja, devuelve la etiqueta de esa hoja. Si no, navega por el árbol según los valores de los atributos de la instancia hasta llegar a una hoja.

Explicación del Proceso
Construcción del árbol: Primero, calculamos la entropía de todo el conjunto y luego, para cada atributo, calculamos la ganancia de información. Seleccionamos el atributo con la mayor ganancia de información como nodo raíz.
Recursividad: El proceso se repite para cada subconjunto de datos hasta que ya no se puedan hacer más divisiones.
Predicción: Una vez que se ha construido el árbol, podemos utilizarlo para predecir la clase de una instancia desconocida al navegar por el árbol según los valores de sus atributos.
"""