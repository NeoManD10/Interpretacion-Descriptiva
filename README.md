
# Tutorial para ejecutar los programas de análisis

## 1. Pre-requisitos

- Tener **Python 3** instalado.

## 2. Crear y activar un entorno virtual (recomendado)

**En Linux/Mac:**
```bash
python3 -m venv env
source env/bin/activate
```

**En Windows:**
```bash
python -m venv env
env\Scripts\activate
```

---

## 3. Instalar dependencias

Con el entorno virtual activo, ejecuta:
```bash
pip install -r requirements.txt
```

---

## 4. Ejecutar los programas

Asegúrate de estar en la carpeta donde están los archivos y ejecuta los siguientes comandos:

### a) Estadística descriptiva
```bash
python estd_descriptiva.py
```
Muestra la media, mediana, desviación estándar, mínimo, máximo y percentiles de los tiempos de respuesta.

### b) Intervalo de confianza para la media y su histograma
```bash
python 3_1.py
```
Imprime el intervalo de confianza para la media y guarda el gráfico `histograma_media.png`.

### c) Intervalo de confianza para la proporción y su gráfico
```bash
python 3_2.py
```
Imprime la proporción de tiempos mayores a 250 ms y su intervalo de confianza, y guarda el gráfico `proporcion_ic.png`.

---

## 5. Visualización de resultados

- Los resultados se muestran en la **terminal**.
- Los gráficos generados se guardan en la misma carpeta y se pueden abrir como archivos PNG.

---

## 6. Salir del entorno virtual

Cuando termines, puedes salir del entorno virtual ejecutando:
```bash
deactivate
```

---

### Notas

- Si hay algún problema, asegúrarse de tener Python 3.x y haber instalado todas las dependencias del `requirements.txt`.
- Recordar **activar el entorno virtual** antes de ejecutar los scripts.

##Captura de la herramienta utilizada para recolectar los tiempos de respuesta
![muestras](https://github.com/user-attachments/assets/dc5b99d4-7842-4da3-b2b7-6df0e9cf4f74)


