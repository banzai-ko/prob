import matplotlib.pyplot as plt

# Datos de la tabla
x = [0,1, 2, 3, 4, 5, 6, 7]
Fk = [2, 6, 10, 11, 14, 16, 18, 20 ]

plt.figure(figsize=(8,8))
plt.plot(x, Fk, marker='o', color='skyblue', linewidth=2)  # línea celeste
plt.scatter(x, Fk, color='skyblue')  # puntos celestes

plt.xlabel("x")
plt.ylabel("Frecuencia acumulada (Fk)")
plt.title("Ojiva")
plt.grid(True, linestyle='--', alpha=0.6)

# Ajustar ticks del eje Y a 20, 40, 60, 80
plt.yticks([5, 10, 15, 20])

# Guardar sin mostrar
plt.savefig("ojiva_pco.png", dpi=300)
plt.close()
