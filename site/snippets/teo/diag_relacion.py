import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

# -----------------------------------
# FIGURA
# -----------------------------------
fig, ax = plt.subplots(figsize=(10, 6))

# -----------------------------------
# CONJUNTOS
# A = {4,1,2,3,5,6}
# B = {1,0}
# -----------------------------------

# Dibujar óvalos de los conjuntos
conjunto_A = Ellipse((2, 4), 3, 7,
                     fill=False, linewidth=2)

conjunto_B = Ellipse((8, 4), 3, 3,
                     fill=False, linewidth=2)

ax.add_patch(conjunto_A)
ax.add_patch(conjunto_B)

# Títulos
ax.text(2, 7.8, "A", fontsize=16,
        ha='center', fontweight='bold')

ax.text(8, 5.8, "B", fontsize=16,
        ha='center', fontweight='bold')

# -----------------------------------
# ELEMENTOS DEL CONJUNTO A
# ORDEN PEDIDO:
# 4,1,2,3,5,6
# -----------------------------------

A = {
    4: (2, 6.5),
    1: (2, 5.5),
    2: (2, 4.5),
    3: (2, 3.5),
    5: (2, 2.5),
    6: (2, 1.5)
}

# -----------------------------------
# ELEMENTOS DEL CONJUNTO B
# ORDEN PEDIDO:
# 1,0
# -----------------------------------

B = {
    1: (8, 5),
    0: (8, 3)
}

# -----------------------------------
# DIBUJAR ELEMENTOS
# -----------------------------------

for valor, (x, y) in A.items():
    ax.text(x, y, str(valor),
            fontsize=14,
            ha='center',
            va='center',
            bbox=dict(boxstyle="circle",
                      facecolor='white',
                      edgecolor='black'))

for valor, (x, y) in B.items():
    ax.text(x, y, str(valor),
            fontsize=14,
            ha='center',
            va='center',
            bbox=dict(boxstyle="circle",
                      facecolor='white',
                      edgecolor='black'))

# -----------------------------------
# RELACIONES
# 4 -> 1
# 1,2,3,5,6 -> 0
# -----------------------------------

for valor, (x, y) in A.items():

    if valor == 4:
        destino = B[1]
    else:
        destino = B[0]

    ax.annotate(
        '',
        xy=(destino[0]-0.3, destino[1]),
        xytext=(x+0.3, y),
        arrowprops=dict(
            arrowstyle='->',
            linewidth=1.8
        )
    )

# -----------------------------------
# CONFIGURACIÓN
# -----------------------------------

ax.set_xlim(0, 10)
ax.set_ylim(0, 9)

ax.axis('off')

# -----------------------------------
# EXPORTAR JPG SIN MOSTRAR
# -----------------------------------

plt.savefig(
    "diagrama_relacion.jpg",
    format='jpg',
    dpi=300,
    bbox_inches='tight'
)

plt.close()

print("Archivo JPG exportado correctamente.")