import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Probabilidades
only_A = 0.15
only_B = 0.05
both = 0.55
outside = 0.25

fig, ax = plt.subplots(figsize=(6,6))

# Radio de los círculos
radius = 0.8
# Separación simétrica respecto al centro
offset = 0.6

# Dibujar círculos centrados
circle_A = Circle((-offset, 0), radius, fill=False, edgecolor="black", linewidth=2)
circle_B = Circle(( offset, 0), radius, fill=False, edgecolor="black", linewidth=2)

ax.add_patch(circle_A)
ax.add_patch(circle_B)

# Etiquetas
ax.text(-offset-0.3, 0, f"{only_A:.2f}", fontsize=12)
ax.text( offset+0.3, 0, f"{only_B:.2f}", fontsize=12)

# Texto de la intersección con pequeño corrimiento a la izquierda
ax.text(-0, -0, f"{both:.2f}", fontsize=12, ha="center", va="center")

# Texto fuera de ambos conjuntos
ax.text(-1.0, -1.0, f"{outside:.2f}", fontsize=12)

# Rectángulo del conjunto universal U de 4x3 centrado
rect_x = -2   # esquina inferior izquierda en X
rect_y = -1.5 # esquina inferior izquierda en Y
rect_width = 4
rect_height = 3

ax.add_patch(plt.Rectangle((rect_x, rect_y), rect_width, rect_height,
                           fill=False, edgecolor="black", linewidth=2))
ax.text(rect_x + rect_width - 0.2, rect_y + rect_height - 0.2, "U", fontsize=14)

plt.title("Diagrama")
plt.axis("equal")
plt.axis("off")
plt.savefig("venn.png")
plt.close()
