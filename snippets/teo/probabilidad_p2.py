import matplotlib.pyplot as plt

# Dataset
x = [0, 1, 2, 3]
p = [1/8, 3/8, 3/8, 1/8]

# Crear figura
fig, ax = plt.subplots(figsize=(8,5))

# Líneas verticales
ax.vlines(x, ymin=0, ymax=p, linewidth=2)

# Puntos
ax.plot(x, p, 'o')

# Etiquetas
ax.set_xlabel('x')
ax.set_ylabel('P(x)')

# Título
ax.set_title('Distribución de Probabilidad')

# Eje X
ax.set_xticks(x)

# Eje Y EXACTAMENTE como pediste
ax.set_yticks([0.25, 0.5, 0.75, 1])

# Cuadrícula
ax.grid(True)

# Exportar JPG SIN mostrar
plt.savefig(
    'distribucion_probabilidad.jpg',
    format='jpg',
    dpi=300,
    bbox_inches='tight'
)

# Cerrar figura
plt.close()

print("Archivo JPG exportado correctamente.")