from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class KDecisionList:
    def __init__(self):
        # Inicializa una lista vacía para las reglas de decisión
        self.rules = []

    def add_rule(self, condition, result):
        # Agrega una regla a la lista de decisiones
        self.rules.append((condition, result))

    def predict(self, instance):
        # Evalúa cada regla en la lista
        for condition, result in self.rules:
            if condition(instance):  # Si la condición se cumple
                return result  # Devuelve el resultado asociado
        return None  # Si no hay coincidencias

# Funciones de condición para el K-DL
def condition_setosa(instance):
    return instance[0] < 2.5 and instance[1] < 2.5

def condition_versicolor(instance):
    return instance[0] >= 2.5 and instance[1] < 2.5

def condition_virginica(instance):
    return instance[0] >= 2.5 and instance[1] >= 2.5

# Ejemplo de uso del K-DL
if __name__ == "__main__":
    # Cargar el conjunto de datos de iris
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Crear y entrenar el modelo K-DL
    k_dl = KDecisionList()
    k_dl.add_rule(condition_setosa, 0)      # Iris Setosa
    k_dl.add_rule(condition_versicolor, 1)  # Iris Versicolor
    k_dl.add_rule(condition_virginica, 2)   # Iris Virginica

    # Realizar predicciones
    print("Predicciones usando K-DL:")
    for instance in X:
        prediction = k_dl.predict(instance)
        print(f"Instancia: {instance}, Predicción: {prediction}")

    # Dividir los datos en conjuntos de entrenamiento y prueba para el K-DT
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Crear y entrenar el árbol de decisión
    k_dt = DecisionTreeClassifier(random_state=42)
    k_dt.fit(X_train, y_train)

    # Realizar predicciones con el K-DT
    y_pred = k_dt.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    # Mostrar precisión del K-DT
    print(f"\nPrecisión del K-DT: {accuracy:.2f}")
"""
Clase KDecisionList:

__init__: Inicializa la lista vacía de reglas de decisión.
add_rule: Método para agregar una regla que consta de una condición y un resultado.
predict: Evalúa cada regla en la lista y devuelve el resultado correspondiente si la condición se cumple.
Funciones de Condición:

condition_setosa, condition_versicolor, condition_virginica: Definen las condiciones para clasificar las instancias del conjunto de datos de iris en tres tipos de flores.
Ejemplo de Uso:

Se carga el conjunto de datos de iris y se entrena el K-DL agregando reglas basadas en las condiciones definidas.
Para cada instancia del conjunto de datos, se predice la clase usando el K-DL.
Se utiliza scikit-learn para crear un árbol de decisión (K-DT) y se evalúa su precisión en un conjunto de prueba.
"""