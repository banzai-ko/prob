import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(10, 4))

# -------------------------
# UNIVERSO U
# -------------------------
U = patches.Rectangle(
    (0, 0), 10, 4,
    fill=False,
    linewidth=2
)
ax.add_patch(U)

# -------------------------
# CONJUNTO A
# -------------------------
A = patches.Ellipse(
    (5, 2),
    9, 3,
    fill=False,
    linewidth=2
)
ax.add_patch(A)

# -------------------------
# DIVISIONES B
# -------------------------
labels = ["B1", "B2", "B3", "B4"]

x_start = 0
total_width = 10
n = 4
cell_width = total_width / n

for i in range(n):
    x = x_start + i * cell_width

    rect = patches.Rectangle(
        (x, 0),
        cell_width,
        4,
        fill=False,
        linewidth=1.5
    )
    ax.add_patch(rect)

    # 🔥 etiquetas fuera del óvalo A, cerca del borde inferior
    ax.text(
        x + cell_width/2,
        0.25,   # <- movido hacia abajo
        labels[i],
        ha="center",
        va="center",
        fontsize=12
    )

# -------------------------
# Etiqueta A
# -------------------------

ax.text(0.5, 3, "A", fontsize=14)
# -------------------------
# FORMATO
# -------------------------
ax.set_xlim(0, 10)
ax.set_ylim(0, 4)
ax.set_aspect('equal')
ax.axis('off')

plt.title("Probabilidad Total")

plt.savefig("prob_total.png", dpi=300, bbox_inches="tight")
plt.close()