import matplotlib.pyplot as plt
#-----------------------------
# Data
#-----------------------------
intervalos = ["0","1","2","3","4","5","6","7"]
fi = [2,4,4,1,3,2,2,2]
midpoints = [2,4,4,1,3,2,2,2]



# -----------------------------
# 1. Histograma de frecuencias
# -----------------------------


plt.figure(figsize=(8,5))
plt.bar(midpoints, fi, width=3, align='center', edgecolor=None, color="skyblue")
plt.xlabel("Grupos")
plt.ylabel("Frecuencia")
plt.title("Histograma")
plt.savefig("histograma_pco.png")
plt.close()



