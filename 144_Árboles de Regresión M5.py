import numpy as np
import pandas as pd

class NodoArbol:
    def __init__(self, valor=None, atributo=None, umbral=None):
        self.valor = valor  # Valor de predicción si es hoja
        self.atributo = atributo  # Atributo por el cual se divide
        self.umbral = umbral  # Umbral para la división
        self.hijos = {}  # Diccionario para los nodos hijos

class ArbolRegresionM5:
    def __init__(self, min_size=5):
        self.min_size = min_size  # Tamaño mínimo de las hojas

    def fit(self, X, y):
        # Ajustar el árbol a los datos
        self.root = self._crear_nodo(X, y)

    def _crear_nodo(self, X, y):
        # Crear un nodo para el árbol
        if len(y) <= self.min_size:
            return NodoArbol(valor=np.mean(y))  # Devolver hoja con media

        # Si todos los valores de y son iguales, devolver hoja
        if np.all(y == y[0]):
            return NodoArbol(valor=y[0])
        
        # Encontrar el mejor atributo y umbral para dividir
        mejor_atributo, mejor_umbral = self._mejor_division(X, y)
        
        if mejor_atributo is None:  # No se puede dividir más
            return NodoArbol(valor=np.mean(y))
        
        # Dividir los datos en función del mejor atributo y umbral
        izquierda_idx = X[:, mejor_atributo] < mejor_umbral
        derecha_idx = X[:, mejor_atributo] >= mejor_umbral
        
        # Crear nodos hijos recursivamente
        nodo = NodoArbol(atributo=mejor_atributo, umbral=mejor_umbral)
        nodo.hijos['izquierda'] = self._crear_nodo(X[izquierda_idx], y[izquierda_idx])
        nodo.hijos['derecha'] = self._crear_nodo(X[derecha_idx], y[derecha_idx])
        
        return nodo

    def _mejor_division(self, X, y):
        mejor_ganancia = float('-inf')  # Inicializar ganancia
        mejor_atributo = None
        mejor_umbral = None
        
        # Evaluar todos los atributos
        for atributo in range(X.shape[1]):
            umbrales = np.unique(X[:, atributo])  # Valores únicos del atributo
            for umbral in umbrales:
                # Dividir los datos
                izquierda_idx = X[:, atributo] < umbral
                derecha_idx = X[:, atributo] >= umbral
                
                if len(y[izquierda_idx]) == 0 or len(y[derecha_idx]) == 0:
                    continue
                
                # Calcular la ganancia de información de la división
                ganancia = self._ganancia(y, y[izquierda_idx], y[derecha_idx])
                
                # Actualizar si esta división es mejor
                if ganancia > mejor_ganancia:
                    mejor_ganancia = ganancia
                    mejor_atributo = atributo
                    mejor_umbral = umbral
        
        return mejor_atributo, mejor_umbral

    def _ganancia(self, y_total, y_izquierda, y_derecha):
        # Calcular la ganancia de la división
        media_total = np.mean(y_total)
        varianza_total = np.var(y_total) * len(y_total)
        varianza_izquierda = np.var(y_izquierda) * len(y_izquierda) if len(y_izquierda) > 0 else 0
        varianza_derecha = np.var(y_derecha) * len(y_derecha) if len(y_derecha) > 0 else 0
        
        # Ganancia es la reducción de la varianza
        return varianza_total - (varianza_izquierda + varianza_derecha)

    def predict(self, X):
        # Hacer predicciones para las instancias dadas
        return np.array([self._predecir(self.root, x) for x in X])

    def _predecir(self, nodo, instancia):
        # Recursivamente predecir usando el árbol
        if nodo.valor is not None:  # Si es una hoja
            return nodo.valor
        
        # Dividir según el atributo y umbral
        if instancia[nodo.atributo] < nodo.umbral:
            return self._predecir(nodo.hijos['izquierda'], instancia)
        else:
            return self._predecir(nodo.hijos['derecha'], instancia)

# Ejemplo de uso del árbol de regresión M5
if __name__ == "__main__":
    # Crear datos de ejemplo
    datos = np.array([[1, 2], [1, 4], [1, 6],
                      [2, 2], [2, 4], [2, 6],
                      [3, 2], [3, 4], [3, 6]])
    
    etiquetas = np.array([1.5, 1.7, 2.0,
                          2.5, 2.8, 3.0,
                          3.5, 3.8, 4.0])

    # Crear y ajustar el modelo
    arbol_m5 = ArbolRegresionM5(min_size=2)
    arbol_m5.fit(datos, etiquetas)

    # Hacer predicciones
    nuevas_instancias = np.array([[1, 3], [2, 5], [3, 5]])
    predicciones = arbol_m5.predict(nuevas_instancias)

    # Mostrar predicciones
    for instancia, prediccion in zip(nuevas_instancias, predicciones):
        print(f"Predicción para {instancia}: {prediccion:.2f}")
"""
Clase NodoArbol:

Representa un nodo del árbol. Contiene el valor de la predicción (si es hoja), el atributo por el que se divide y el umbral de división. También tiene un diccionario de hijos.
Clase ArbolRegresionM5:

Contiene el método fit para ajustar el árbol a los datos, y el método _crear_nodo para construir los nodos del árbol de forma recursiva.
calcular_ganancia: Evalúa la ganancia de la división en función de la varianza. Utiliza el cálculo de varianza total y varianza ponderada por las divisiones.
predict: Realiza predicciones en base a nuevas instancias, recorriendo el árbol según los atributos y umbrales.
Función _mejor_division:

Evalúa todas las divisiones posibles basadas en los atributos y encuentra el que ofrece la mayor ganancia de información.
Ejemplo de Uso:

Crea un conjunto de datos de ejemplo y etiquetas continuas.
Crea un árbol de regresión M5, lo ajusta a los datos y realiza predicciones sobre nuevas instancias.
"""