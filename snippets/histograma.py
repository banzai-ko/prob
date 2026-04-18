import matplotlib.pyplot as plt
#-----------------------------
# Data
#-----------------------------
intervalos = ["56-59","59-62","62-65","65-68","68-71","71-74","74-77","77-80","80-83","83-86"]
fi = [3,4,13,18,27,20,10,8,5,2]
midpoints = [57.5, 60.5, 63.5, 66.5, 69.5, 72.5, 75.5, 78.5, 81.5, 84.5]



# -----------------------------
# 1. Histograma de frecuencias
# -----------------------------


plt.figure(figsize=(8,5))
plt.bar(midpoints, fi, width=3, align='center', edgecolor=None, color="skyblue")
plt.xlabel("Intervalos")
plt.ylabel("Frecuencia")
plt.title("Histograma")
plt.savefig("histograma.png")
plt.close()



