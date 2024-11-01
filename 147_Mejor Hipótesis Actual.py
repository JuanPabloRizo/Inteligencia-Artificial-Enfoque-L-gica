import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

# Clase para representar la Mejor Hipótesis Actual
class MejorHipotesisActual:
    def __init__(self):
        # Inicializa las hipótesis y su desempeño
        self.hipotesis = []
        self.mejor_hipotesis = None
        self.mejor_precision = 0

    def agregar_hipotesis(self, clasificador):
        # Agrega un clasificador a la lista de hipótesis
        self.hipotesis.append(clasificador)

    def evaluar_hipotesis(self, X_train, y_train, X_test, y_test):
        # Evaluar cada hipótesis y actualizar la mejor
        for hipotesis in self.hipotesis:
            hipotesis.fit(X_train, y_train)  # Entrenar el clasificador
            predicciones = hipotesis.predict(X_test)  # Realizar predicciones
            precision = accuracy_score(y_test, predicciones)  # Calcular precisión

            print(f"Precisión del clasificador {type(hipotesis).__name__}: {precision:.2f}")

            # Actualizar la mejor hipótesis si la precisión es mayor
            if precision > self.mejor_precision:
                self.mejor_precision = precision
                self.mejor_hipotesis = hipotesis

    def predecir(self, X):
        # Realiza predicciones utilizando la mejor hipótesis actual
        if self.mejor_hipotesis is not None:
            return self.mejor_hipotesis.predict(X)
        else:
            raise ValueError("No hay hipótesis evaluadas.")

# Ejemplo de uso
if __name__ == "__main__":
    # Cargar el conjunto de datos de iris
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Crear una instancia de MejorHipotesisActual
    mejor_hipotesis = MejorHipotesisActual()

    # Agregar diferentes clasificadores como hipótesis
    mejor_hipotesis.agregar_hipotesis(KNeighborsClassifier(n_neighbors=3))
    mejor_hipotesis.agregar_hipotesis(DecisionTreeClassifier(random_state=42))
    mejor_hipotesis.agregar_hipotesis(SVC(kernel='linear', random_state=42))

    # Evaluar las hipótesis y encontrar la mejor
    mejor_hipotesis.evaluar_hipotesis(X_train, y_train, X_test, y_test)

    # Realizar predicciones con la mejor hipótesis
    predicciones = mejor_hipotesis.predecir(X_test)
    print(f"Predicciones de la mejor hipótesis: {predicciones}")
"""
Clase MejorHipotesisActual:

__init__: Inicializa una lista para las hipótesis y variables para almacenar la mejor hipótesis y su precisión.
agregar_hipotesis: Método para agregar clasificadores (hipótesis) a la lista.
evaluar_hipotesis: Este método entrena cada clasificador en el conjunto de entrenamiento, realiza predicciones en el conjunto de prueba y calcula la precisión. Si la precisión de una hipótesis es mejor que la anterior mejor, la actualiza.
predecir: Realiza predicciones utilizando la mejor hipótesis actual.
Ejemplo de Uso:

Se carga el conjunto de datos de iris y se divide en conjuntos de entrenamiento y prueba.
Se crea una instancia de MejorHipotesisActual y se agregan diferentes clasificadores.
Se evalúan las hipótesis para encontrar la mejor y se utilizan para realizar predicciones en el conjunto de prueba.
"""