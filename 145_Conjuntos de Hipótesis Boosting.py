import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class AdaBoost:
    def __init__(self, n_estimators=50):
        self.n_estimators = n_estimators  # Número de modelos débiles a entrenar
        self.models = []  # Lista para almacenar los modelos
        self.alphas = []  # Lista para almacenar los pesos de cada modelo

    def fit(self, X, y):
        # Inicializar pesos de los ejemplos
        n_samples = X.shape[0]
        w = np.ones(n_samples) / n_samples  # Pesos uniformes al inicio
        
        for _ in range(self.n_estimators):
            # Crear y entrenar un modelo débil
            model = DecisionTreeClassifier(max_depth=1)  # Un árbol de decisión simple (stump)
            model.fit(X, y, sample_weight=w)  # Entrenar con pesos

            # Predicciones del modelo
            y_pred = model.predict(X)
            
            # Calcular el error
            error = np.sum(w * (y_pred != y)) / np.sum(w)
            
            # Calcular el peso del modelo (alpha)
            alpha = 0.5 * np.log((1 - error) / (error + 1e-10))  # Evitar división por cero
            self.models.append(model)  # Agregar modelo a la lista
            self.alphas.append(alpha)  # Agregar peso del modelo a la lista
            
            # Actualizar los pesos
            w *= np.exp(-alpha * y * y_pred)  # Actualizar pesos
            w /= np.sum(w)  # Normalizar pesos para que sumen 1

    def predict(self, X):
        # Hacer predicciones con los modelos entrenados
        # Sumar las predicciones ponderadas
        preds = np.zeros(X.shape[0])
        for alpha, model in zip(self.alphas, self.models):
            preds += alpha * model.predict(X)
        
        # Retornar la clase con mayor predicción
        return np.sign(preds)  # Convertir las predicciones a -1 o 1

# Ejemplo de uso del algoritmo AdaBoost
if __name__ == "__main__":
    # Generar un conjunto de datos de ejemplo
    X, y = make_classification(n_samples=100, n_features=20, n_informative=10, n_redundant=10, random_state=42)
    
    # Cambiar las etiquetas a -1 y 1
    y[y == 0] = -1

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Crear y entrenar el modelo AdaBoost
    model = AdaBoost(n_estimators=50)
    model.fit(X_train, y_train)

    # Hacer predicciones
    y_pred = model.predict(X_test)

    # Calcular y mostrar la precisión
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Precisión del modelo AdaBoost: {accuracy:.2f}")
"""
Clase AdaBoost:

__init__: Inicializa el número de estimadores (modelos débiles) y listas para almacenar los modelos y sus pesos.
fit: Ajusta el modelo a los datos. Comienza asignando pesos iguales a todos los ejemplos y luego entrena un modelo débil en cada iteración:
Entrena un árbol de decisión simple (stump).
Calcula el error y el peso del modelo.
Actualiza los pesos para que los ejemplos mal clasificados tengan más peso en la próxima iteración.
Método predict:

Realiza predicciones acumulando las salidas de los modelos ponderadas por sus pesos y devuelve la clase con la suma más alta.
Ejemplo de Uso:

Genera un conjunto de datos sintéticos para clasificar.
Ajusta el modelo AdaBoost a los datos de entrenamiento y evalúa su precisión en el conjunto de prueba.
"""