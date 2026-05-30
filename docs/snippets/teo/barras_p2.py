import matplotlib.pyplot as plt

# Dataset
x = [ 1, 2, 3, 4]
p = [ 1/30, 3/10, 1/2, 1/6]

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
ax.set_title('Función de Probabilidad')

# Eje X
ax.set_xticks(x)

# Eje Y
ax.set_yticks([0, 0.5, 1])

# Cuadrícula
ax.grid(True)

# Exportar JPG SIN mostrar
plt.savefig(
    'funcion_probabilidad.jpg',
    format='jpg',
    dpi=300,
    bbox_inches='tight'
)

# Cerrar figura
plt.close()

print("Archivo JPG exportado correctamente.")