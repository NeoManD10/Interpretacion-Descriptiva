import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

# Cargar los datos de tiempo de respuesta desde archivo CSV.
df = pd.read_csv('datos_respuesta.csv')

# Calcular la proporción de mediciones mayores a 250 ms.
x = sum(df['tiempo_ms'] > 250)    # Número de respuestas >250 ms
n = len(df)                       # Número total de mediciones
p_hat = x / n                     # Proporción muestral

# Calcular el intervalo de confianza del 95% para la proporción usando el método de Wilson:
alpha = 0.05
z = stats.norm.ppf(1 - alpha/2)   # Valor crítico z para 95%
den = 1 + (z**2)/n
center = (p_hat + (z**2)/(2*n)) / den
margen_wilson = z * ((p_hat*(1-p_hat)/n) + (z**2)/(4*n**2))**0.5 / den
ic_prop = (center - margen_wilson, center + margen_wilson)  # Límite inferior y superior

# Imprimir los resultados en consola.
print(f"Proporción >250 ms: {p_hat:.2f}")
print(f"Intervalo Wilson 95% para la proporción: ({ic_prop[0]:.2f}, {ic_prop[1]:.2f})")

# Visualización: gráfico de barras de la proporción y su intervalo de confianza.
plt.figure(figsize=(5, 5))
plt.bar(['>250 ms'], [p_hat], yerr=[[p_hat-ic_prop[0]], [ic_prop[1]-p_hat]], capsize=15, color='lightgreen')
plt.ylim(0, 1)
plt.ylabel('Proporción')
plt.title('Proporción de tiempos de respuesta >250 ms (IC 95%)')
plt.tight_layout()
plt.savefig('proporcion_ic.png', dpi=300)  # Guarda el gráfico como imagen PNG
plt.show()
