# Importación de bibliotecas necesarias
import numpy as np          # Para cálculos numéricos y manipulación de arrays
import skfuzzy as fuzz      # Biblioteca para lógica difusa
import matplotlib.pyplot as plt  # Para la visualización de gráficos

# Definición del rango de valores de 0 a 10, con 100 puntos equidistantes
x = np.linspace(0, 10, 100)  

# Definición de los conjuntos difusos utilizando funciones de pertenencia triangular

# Conjunto difuso 'bajo': 
# La pertenencia es 1 para valores ≤ 0 y desciende linealmente hasta 0 en 5
bajo = fuzz.trimf(x, [0, 0, 5])   

# Conjunto difuso 'medio': 
# La pertenencia es 0 en 0, 1 en 5 y desciende linealmente hasta 0 en 10
medio = fuzz.trimf(x, [0, 5, 10])  

# Conjunto difuso 'alto': 
# La pertenencia es 1 en 10 y desciende linealmente desde 5
alto = fuzz.trimf(x, [5, 10, 10])   

# Visualización de los conjuntos difusos
plt.figure(figsize=(10, 5))  # Crear una figura con un tamaño específico
plt.plot(x, bajo, label='Bajo', color='blue')    # Graficar conjunto 'bajo' en azul
plt.plot(x, medio, label='Medio', color='green')  # Graficar conjunto 'medio' en verde
plt.plot(x, alto, label='Alto', color='red')      # Graficar conjunto 'alto' en rojo

# Configuración del gráfico
plt.title('Conjuntos Difusos')            # Título del gráfico
plt.xlabel('Valor')                       # Etiqueta del eje X
plt.ylabel('Grado de Pertenencia')        # Etiqueta del eje Y
plt.ylim(0, 1)                            # Limitar el eje Y entre 0 y 1
plt.legend()                              # Mostrar la leyenda
plt.grid()                                # Mostrar una cuadrícula en el gráfico
plt.show()                                # Mostrar el gráfico

# Ejemplo de valores a evaluar
valores_a_evaluar = [2, 5, 8]  # Valores para los que se calculará el grado de pertenencia

# Evaluar y mostrar el grado de pertenencia para cada conjunto difuso
for valor in valores_a_evaluar:
    # Calcular el grado de pertenencia al conjunto 'bajo'
    grado_bajo = fuzz.interp_membership(x, bajo, valor)  

    # Calcular el grado de pertenencia al conjunto 'medio'
    grado_medio = fuzz.interp_membership(x, medio, valor)  

    # Calcular el grado de pertenencia al conjunto 'alto'
    grado_alto = fuzz.interp_membership(x, alto, valor)  

    # Imprimir resultados para el valor actual
    print(f"Valor: {valor}")  # Mostrar el valor que se evalúa
    print(f"Grado de pertenencia a 'Bajo': {grado_bajo:.2f}")  # Mostrar grado de pertenencia al conjunto 'bajo'
    print(f"Grado de pertenencia a 'Medio': {grado_medio:.2f}")  # Mostrar grado de pertenencia al conjunto 'medio'
    print(f"Grado de pertenencia a 'Alto': {grado_alto:.2f}")  # Mostrar grado de pertenencia al conjunto 'alto'
    print("-" * 30)  # Línea separadora para mayor claridad
"""
Importaciones: Se explican las bibliotecas importadas y su propósito.
Definición del Rango: Se detalla el rango de valores que se utilizará para definir los conjuntos difusos.
Definición de Conjuntos Difusos: Cada conjunto se explica con respecto a su función de pertenencia.
Visualización: Se comentan las configuraciones del gráfico, incluyendo el título, etiquetas y la cuadrícula.
Evaluación de Valores: Se describen los pasos para evaluar los grados de pertenencia y cómo se imprimen los resultados.
"""