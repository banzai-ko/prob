import matplotlib.pyplot as plt

# -----------------------------
# Data
# -----------------------------
intervalos = ["56-59","59-62","62-65","65-68","68-71","71-74","74-77","77-80","80-83","83-86"]
fi = [3,4,13,18,27,20,10,8,5,2]
midpoints = [57.5, 60.5, 63.5, 66.5, 69.5, 72.5, 75.5, 78.5, 81.5, 84.5]


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


