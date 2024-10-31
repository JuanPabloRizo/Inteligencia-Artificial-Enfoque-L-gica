import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Definición de las variables difusas
temperatura = ctrl.Antecedent(np.arange(0, 41, 1), 'temperatura')
humedad = ctrl.Antecedent(np.arange(0, 101, 1), 'humedad')
ventilador = ctrl.Consequent(np.arange(0, 101, 1), 'ventilador')

# Definición de las funciones de pertenencia
temperatura['baja'] = fuzz.trimf(temperatura.universe, [0, 0, 20])
temperatura['media'] = fuzz.trimf(temperatura.universe, [15, 25, 35])
temperatura['alta'] = fuzz.trimf(temperatura.universe, [30, 40, 40])

humedad['baja'] = fuzz.trimf(humedad.universe, [0, 0, 50])
humedad['media'] = fuzz.trimf(humedad.universe, [25, 50, 75])
humedad['alta'] = fuzz.trimf(humedad.universe, [50, 100, 100])

ventilador['bajo'] = fuzz.trimf(ventilador.universe, [0, 0, 50])
ventilador['medio'] = fuzz.trimf(ventilador.universe, [25, 50, 75])
ventilador['alto'] = fuzz.trimf(ventilador.universe, [50, 100, 100])

# Definición de las reglas de control difuso
regla1 = ctrl.Rule(temperatura['baja'] & humedad['baja'], ventilador['bajo'])
regla2 = ctrl.Rule(temperatura['baja'] & humedad['media'], ventilador['bajo'])
regla3 = ctrl.Rule(temperatura['media'] & humedad['baja'], ventilador['medio'])
regla4 = ctrl.Rule(temperatura['media'] & humedad['media'], ventilador['medio'])
regla5 = ctrl.Rule(temperatura['alta'] & humedad['media'], ventilador['alto'])
regla6 = ctrl.Rule(temperatura['alta'] & humedad['alta'], ventilador['alto'])

# Crear el sistema de control
sistema_control = ctrl.ControlSystem([regla1, regla2, regla3, regla4, regla5, regla6])
simulador = ctrl.ControlSystemSimulation(sistema_control)

# Entrar en la simulación con datos de entrada
temperatura_entrada = 30  # Grado de temperatura
humedad_entrada = 70      # Grado de humedad

simulador.input['temperatura'] = temperatura_entrada
simulador.input['humedad'] = humedad_entrada

# Calcular la salida
simulador.compute()

# Resultado
print(f"Para temperatura = {temperatura_entrada} y humedad = {humedad_entrada}, el ventilador se ajusta a: {simulador.output['ventilador']:.2f}")

# Visualización de las funciones de pertenencia
temperatura.view()
humedad.view()
ventilador.view()
plt.show()
"""
Importaciones: Se importan las bibliotecas necesarias: numpy para manejar arrays, skfuzzy para lógica difusa, y matplotlib para visualización.

Definición de Variables Difusas:

temperatura, humedad, y ventilador son las variables difusas que se definen como antecedentes y consecuentes. Cada uno tiene un rango específico.
Funciones de Pertenencia:

Se definen funciones de pertenencia triangulares para las variables de temperatura, humedad y ventilador, indicando diferentes niveles (bajo, medio, alto).
Definición de Reglas de Control:

Se crean reglas que definen cómo las entradas (temperatura y humedad) afectan la salida (ventilador). Por ejemplo, si la temperatura es baja y la humedad es baja, el ventilador debe estar en un nivel bajo.
Sistema de Control:

Se construye un sistema de control que utiliza las reglas definidas y se crea un simulador.
Simulación:

Se ingresan valores de temperatura y humedad, y se calcula la salida (ajuste del ventilador) en función de las reglas de lógica difusa.
Visualización:

Se visualizan las funciones de pertenencia para las tres variables.
"""