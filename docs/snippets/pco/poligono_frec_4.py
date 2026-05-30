import matplotlib.pyplot as plt

# -----------------------------
# Data
# -----------------------------
intervalos = ["50-59","60-69","70-79","80-89","90-99","100-109","110-119"]
fi = [8,10,16,14,10,5,2]
midpoints = [54.5,64.5,74.5,84.5,94.5,104.5,114.5]

# | Clase | Intervalo (cm) |mid     | \(fi\) | \(Fk\) |
# |-------|----------------|--------|--------|--------|
# | 1     | 50–59          |  54,5  |8       | 8      |
# | 2     | 60–69          |  64,5  |10      | 18     |
# | 3     | 70–79          |  74,5  |16      | 34     |
# | 4     | 80–89          |  84,5  |14      | 48     |
# | 5     | 90–99          |  94,5  |10      | 58     |
# | 6     | 100–109        | 104,5  |5       | 63     |
# | 7     | 110–119        | 114,5  |2       | 65     |

# -----------------------------
# 2. Polígono de frecuencias
# -----------------------------
plt.figure(figsize=(8,5))
plt.plot(midpoints, fi, marker='o', linestyle='-', color='blue')
plt.xlabel("Intervalos")
plt.ylabel("Frecuencia")
plt.title("Polígono de frecuencias")
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig("poligono_frecuencias.png")
plt.close()


