import matplotlib.pyplot as plt

# Datos de la tabla
x = [49.5, 59.5, 69.5, 79.5, 89.5, 99.5, 109.5, 119.5]

Fk = [0,  8, 18, 34, 48, 58, 63, 65 ]


# | Clase | Intervalo (cm) |mid     | \(fi\) | \(Fk\) |
# |-------|----------------|--------|--------|--------|
# | 1     | 50–59          |  54,5  |8      | 8      |
# | 2     | 60–69          |  64,5  |10     | 18     |
# | 3     | 70–79          |  74,5  |16     | 34     |
# | 4     | 80–89          |  84,5  |14     | 48     |
# | 5     | 90–99          |  94,5  |10     | 58     |
# | 6     | 100–109        | 104,5  |5      | 63     |
# | 7     | 110–119        | 114,5  |2      | 65     |

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
plt.savefig("ojiva_pco_5.png", dpi=300)
plt.close()
