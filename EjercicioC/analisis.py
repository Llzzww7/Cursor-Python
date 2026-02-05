#Pandas es una librería de Python usada para análisis y manipulación de datos.
#Calcular estadísitcas simples: media, mediana, desviación estándar de cada columna.)
import pandas as pd
import matplotlib.pyplot as plt

# Leer el CSV (está en la misma carpeta que este script)
df = pd.read_csv("datos.csv")

print("Primeras filas del dataset:")
print(df.head(), "\n")

# Estadísticas simples para cada columna
for col in df.columns:
    print(f"Columna: {col}")
    print(f"  Media: {df[col].mean()}")
    print(f"  Mediana: {df[col].median()}")
    print(f"  Desviación estándar: {df[col].std()}")
    print()

# Gráfica de dispersión col1 vs col2
plt.scatter(df["col1"], df["col2"])
plt.xlabel("col1")
plt.ylabel("col2")
plt.title("Scatter plot: col1 vs col2")
plt.grid(True)
plt.show()

## Matplotlib es una biblioteca de Python para hacer gráficos.
# Sirve para:
#Dibujar gráficas de líneas, barras, dispersión (scatter), histogramas, etc.
#Visualizar datos de forma sencilla cuando haces análisis de datos o ciencia de datos.
#El módulo que estás usando, matplotlib.pyplot, ofrece funciones tipo:
#plt.plot(...), plt.scatter(...), plt.bar(...), plt.hist(...), plt.show(), etc.
#En tu caso, la usamos para dibujar un gráfico de dispersión entre col1 y col2 y ver la relación entre esas dos columnas de números.


