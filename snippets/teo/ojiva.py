import matplotlib.pyplot as plt

# Datos de la tabla
x = [1, 2, 3, 4, 5]
Fk = [13, 21, 41, 71, 76]  # Frecuencia acumulada absoluta

# Gráfico de ojiva (línea azul/celeste)
plt.figure(figsize=(8,5))
plt.plot(x, Fk, marker='o', color='skyblue', linewidth=2)  # línea celeste
plt.scatter(x, Fk, color='skyblue')  # puntos celestes

plt.xlabel("x")
plt.ylabel("Frecuencia acumulada (Fk)")
plt.title("Ojiva")
plt.grid(True, linestyle='--', alpha=0.6)

# Ajustar ticks del eje Y a 20, 40, 60, 80
plt.yticks([20, 40, 60, 80])

# Guardar sin mostrar
plt.savefig("ojiva.png", dpi=300)
plt.close()
