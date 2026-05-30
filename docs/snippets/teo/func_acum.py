import matplotlib.pyplot as plt

# Valores de la función de acumulación
x = [1, 2, 3, 4]
F = [1/30, 1/3, 5/6, 1]

# Crear figura
fig, ax = plt.subplots(figsize=(8,5))

# Tramo inicial en y=0
ax.hlines(0, 0, 1, linewidth=2)

# Segmentos horizontales SIN conexiones verticales
for i in range(len(x)-1):
    ax.hlines(F[i], x[i], x[i+1], linewidth=2)

# Último tramo
ax.hlines(F[-1], x[-1], 4.5, linewidth=2)

# Puntos
ax.plot(x, F, 'o')

# Punto inicial
ax.plot(0, 0, 'o')

# Etiquetas
ax.set_xlabel('x')
ax.set_ylabel('F(x)')

# Título
ax.set_title('Función de Acumulación')

# Eje X
ax.set_xticks([0,1,2,3,4])

# Eje Y
ax.set_yticks([0, 0.5, 1])

# Límites
ax.set_xlim(0, 4.5)
ax.set_ylim(0, 1.05)

# Cuadrícula
ax.grid(True)

# Exportar JPG SIN mostrar
plt.savefig(
    'funcion_acumulacion.jpg',
    format='jpg',
    dpi=300,
    bbox_inches='tight'
)

# Cerrar figura
plt.close()

print("Archivo JPG exportado correctamente.")