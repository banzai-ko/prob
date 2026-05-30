import matplotlib.pyplot as plt

# Datos
x = [0,1,2,3,4]
Fk = [8,21,41,71,76]

plt.figure(figsize=(8,5))

# Dibujar solo líneas horizontales aisladas entre los valores de x
for i in range(len(x)-1):
    plt.hlines(Fk[i], x[i], x[i+1], colors='green', linewidth=2)

# Marcar los puntos acumulados
plt.scatter(x, Fk, color='green')

# Ajustar el eje X para que muestre solo los valores 1,2,3,4
plt.xticks([1,2,3,4])

plt.xlabel("x")
plt.ylabel("Frecuencia acumulada")
plt.title("Diagrama de frecuencias acumuladas")
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig("frecuencias_acumuladas.png")
plt.close()
