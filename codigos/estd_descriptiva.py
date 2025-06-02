import pandas as pd

# Cargar archivo CSV con los datos de tiempo de respuesta.
df = pd.read_csv('datos_respuesta.csv')

# Calcular la media aritmética de los tiempos de respuesta (en ms).
media = df['tiempo_ms'].mean()

# Calcular la mediana de los tiempos de respuesta.
mediana = df['tiempo_ms'].median()

# Calcular la desviación estándar muestral (variabilidad de los tiempos).
desviacion = df['tiempo_ms'].std()

# Encontrar el valor mínimo observado.
minimo = df['tiempo_ms'].min()

# Encontrar el valor máximo observado.
maximo = df['tiempo_ms'].max()

# Calcular el percentil 25% (cuartil inferior).
percentil_25 = df['tiempo_ms'].quantile(0.25)

# Calcular el percentil 75% (cuartil superior).
percentil_75 = df['tiempo_ms'].quantile(0.75)

# Imprimir todos los estadísticos calculados.
print(f"Media: {media:.2f} ms")
print(f"Mediana: {mediana:.2f} ms")
print(f"Desviación estándar: {desviacion:.2f} ms")
print(f"Mínimo: {minimo} ms")
print(f"Máximo: {maximo} ms")
print(f"Percentil 25%: {percentil_25} ms")
print(f"Percentil 75%: {percentil_75} ms")
