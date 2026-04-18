import matplotlib.pyplot as plt

# Datos
niveles = ["Bueno", "Regular", "Malo"]
fi = [62, 25, 13]

# Gráfico de barras (todas del mismo color y ancho fijo)
plt.figure(figsize=(6,4))
plt.bar(niveles, fi, width=0.3, color="skyblue")

plt.xlabel("Nivel")
plt.ylabel("Frecuencia absoluta")
plt.title("Frecuencia absoluta")
plt.tight_layout()

# Guardar directamente sin mostrar
plt.savefig("barras_frecuencia_absoluta.png", dpi=300)
plt.close()
