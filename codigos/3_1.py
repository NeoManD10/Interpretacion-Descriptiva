import pandas as pd
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos de tiempo de respuesta desde archivo CSV.
df = pd.read_csv('datos_respuesta.csv')
media = df['tiempo_ms'].mean()            # Media muestral
s = df['tiempo_ms'].std(ddof=1)           # Desviación estándar muestral (con Bessel)
n = len(df)                               # Número de mediciones

# Calcular el intervalo de confianza 95% para la media usando t de Student:
alpha = 0.05                              # Nivel de significancia (5%)
dfree = n - 1                             # Grados de libertad
t_crit = stats.t.ppf(1 - alpha/2, dfree)  # Valor crítico t para 95% y n-1 g.l.

# Calcular error estándar y margen de error.
se = s / np.sqrt(n)
margen = t_crit * se

# Calcular el intervalo de confianza final.
ic_media = (media - margen, media + margen)

# Mostrar el resultado por pantalla.
print(f"Intervalo de confianza 95% para la media: ({ic_media[0]:.2f}, {ic_media[1]:.2f}) ms")

# Visualización: histograma de los tiempos con la media señalada.
plt.figure(figsize=(8, 5))
plt.hist(df['tiempo_ms'], bins=8, color='skyblue', edgecolor='black')
plt.axvline(media, color='red', linestyle='dashed', linewidth=2, label=f'Media = {media:.2f} ms')
plt.xlabel('Tiempo de respuesta (ms)')
plt.ylabel('Frecuencia')
plt.title('Histograma de tiempos de respuesta')
plt.legend()
plt.tight_layout()
plt.savefig('histograma_media.png', dpi=300)  # Guarda el gráfico como imagen PNG
plt.show()
