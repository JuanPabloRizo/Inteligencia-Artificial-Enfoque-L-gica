# Importación de la biblioteca pyclips para interactuar con CLIPS desde Python
import clips

# Inicializa el entorno CLIPS, creando un nuevo espacio para definir hechos y reglas
env = clips.Environment()

# 1. Definición de hechos difusos para la temperatura
# Aquí se definen categorías difusas de temperatura con sus respectivos rangos
env.assert_string("(fuzzy-temperature low 0.0 30.0)")    # Baja temperatura entre 0 y 30 grados
env.assert_string("(fuzzy-temperature medium 20.0 80.0)") # Temperatura media entre 20 y 80 grados
env.assert_string("(fuzzy-temperature high 70.0 100.0)")  # Alta temperatura entre 70 y 100 grados

# 2. Definición de hechos difusos para la humedad
# Se definen categorías difusas de humedad de manera similar a la temperatura
env.assert_string("(fuzzy-humidity low 0.0 40.0)")        # Baja humedad entre 0 y 40%
env.assert_string("(fuzzy-humidity medium 30.0 70.0)")    # Humedad media entre 30 y 70%
env.assert_string("(fuzzy-humidity high 60.0 100.0)")     # Alta humedad entre 60 y 100%

# 3. Definición de reglas para inferencia
# Se definen las reglas de inferencia basadas en las categorías difusas
# Regla 1: Si la temperatura es baja y la humedad es baja, la velocidad del ventilador es baja
env.assert_string("""
(defrule low-speed
    (fuzzy-temperature low)      ; Hecho difuso de temperatura baja
    (fuzzy-humidity low)         ; Hecho difuso de humedad baja
    =>
    (assert (fuzzy-speed low))   ; Conclusión: velocidad baja del ventilador
)
""")

# Regla 2: Si la temperatura es media y la humedad es media, la velocidad del ventilador es media
env.assert_string("""
(defrule medium-speed
    (fuzzy-temperature medium)   ; Hecho difuso de temperatura media
    (fuzzy-humidity medium)      ; Hecho difuso de humedad media
    =>
    (assert (fuzzy-speed medium)) ; Conclusión: velocidad media del ventilador
)
""")

# Regla 3: Si la temperatura es alta y la humedad es alta, la velocidad del ventilador es alta
env.assert_string("""
(defrule high-speed
    (fuzzy-temperature high)     ; Hecho difuso de temperatura alta
    (fuzzy-humidity high)        ; Hecho difuso de humedad alta
    =>
    (assert (fuzzy-speed high))   ; Conclusión: velocidad alta del ventilador
)
""")

# 4. Definición de un hecho de entrada
# Aquí se establecen los valores de temperatura y humedad actuales
temperature = 75  # Temperatura actual de 75 grados
humidity = 30     # Humedad actual de 30%

# 5. Inferir el estado difuso actual de la temperatura y la humedad
# Dependiendo de los valores, se asocian hechos difusos en el entorno
if temperature < 30:
    env.assert_string("(fuzzy-temperature low)")          # Asocia hecho difuso de temperatura baja
elif 30 <= temperature <= 80:
    env.assert_string("(fuzzy-temperature medium)")       # Asocia hecho difuso de temperatura media
else:
    env.assert_string("(fuzzy-temperature high)")         # Asocia hecho difuso de temperatura alta

if humidity < 40:
    env.assert_string("(fuzzy-humidity low)")             # Asocia hecho difuso de humedad baja
elif 40 <= humidity <= 70:
    env.assert_string("(fuzzy-humidity medium)")          # Asocia hecho difuso de humedad media
else:
    env.assert_string("(fuzzy-humidity high)")            # Asocia hecho difuso de humedad alta

# 6. Ejecutar el motor de inferencia
# Llama al motor de inferencia de CLIPS para evaluar las reglas y hechos
env.run()

# 7. Consultar el resultado de la velocidad
# Se consulta el resultado de la velocidad del ventilador inferida
result = env.eval('(fuzzy-speed ?speed)')  # Se evalúa el hecho difuso de la velocidad
if result:
    print(f"La velocidad del ventilador recomendada es: {result}")  # Imprime la velocidad inferida
else:
    print("No se pudo inferir la velocidad del ventilador.")  # Mensaje si no se pudo inferir
"""
Importaciones y Inicialización: Se importa la biblioteca necesaria para trabajar con CLIPS y se inicializa un nuevo entorno que se usará para definir hechos y reglas.

Hechos Difusos: Se definen las categorías de temperatura y humedad mediante hechos difusos. Esto permite que el sistema pueda manejar información que no es precisa o exacta, sino más bien representaciones borrosas.

Reglas de Inferencia: Las reglas son la lógica que el sistema utilizará para inferir nuevos hechos basados en los hechos existentes. Cada regla asocia combinaciones de hechos difusos con conclusiones.

Hechos de Entrada: Se definen valores de entrada para la temperatura y la humedad, que luego se utilizan para inferir los hechos difusos correspondientes.

Ejecución del Motor de Inferencia: Se ejecuta el motor de inferencia de CLIPS, que evaluará las reglas basándose en los hechos que se han agregado.

Consulta de Resultados: Finalmente, se consulta el resultado de la inferencia sobre la velocidad del ventilador y se imprime, proporcionando una salida clara sobre la decisión del sistema.
"""