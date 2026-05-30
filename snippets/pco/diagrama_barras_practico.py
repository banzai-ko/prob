import matplotlib.pyplot as plt

# Valores de fallos (categorías en el eje X)
x = [0,1,2,3,4,5,6,7]

# Frecuencias absolutas correspondientes
fi = [2,4,4,1,3,2,2,2]

# Gráfico de barras
plt.figure(figsize=(6,4))
plt.bar(x, fi, width=0.6, color="skyblue")

plt.xlabel("Número de fallos")
plt.ylabel("Frecuencia absoluta")
plt.title("Frecuencia absoluta de fallos por lote")
plt.xticks(x)  # asegura que se muestren todas las categorías
plt.tight_layout()

# Guardar directamente sin mostrar
plt.savefig("barras_frecuencia_pco.png", dpi=300)
plt.close()
