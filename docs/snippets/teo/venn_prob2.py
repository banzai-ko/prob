import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Probabilidades
only_A = 0.6
only_B = 0.05
both = 0.2
outside = 0.15

fig, ax = plt.subplots(figsize=(6,6))

# Radio de los círculos
radius = 0.8
offset = 0.6

# Dibujar círculos
circle_A = Circle((-offset, 0), radius, fill=False, edgecolor="black", linewidth=2)
circle_B = Circle(( offset, 0), radius, fill=False, edgecolor="black", linewidth=2)

ax.add_patch(circle_A)
ax.add_patch(circle_B)

# 🔤 Etiquetas de conjuntos
ax.text(-offset, radius + 0.1, "A", fontsize=14, ha="center")
ax.text( offset, radius + 0.1, "B", fontsize=14, ha="center")

# Valores dentro de regiones
ax.text(-offset-0.3, 0, f"{only_A:.2f}", fontsize=12)
ax.text( offset+0.3, 0, f"{only_B:.2f}", fontsize=12)
ax.text(0, 0, f"{both:.2f}", fontsize=12, ha="center", va="center")

# Fuera de ambos conjuntos
ax.text(-1.0, -1.0, f"{outside:.2f}", fontsize=12)

# Rectángulo del universo U
rect_x = -2
rect_y = -1.5
rect_width = 4
rect_height = 3

ax.add_patch(plt.Rectangle((rect_x, rect_y), rect_width, rect_height,
                           fill=False, edgecolor="black", linewidth=2))

ax.text(rect_x + rect_width - 0.2, rect_y + rect_height - 0.2, "U", fontsize=14)

plt.title("Diagrama de Venn")
plt.axis("equal")
plt.axis("off")
plt.savefig("venn_prob_2.png")
plt.close()