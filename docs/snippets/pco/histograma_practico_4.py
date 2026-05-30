import matplotlib.pyplot as plt
#-----------------------------
# Data
#-----------------------------
intervalos = ["50-59","60-69","70-79","80-89","90-99","100-109","110-119"]
fi = [8,10,16,14,10,5,2]
midpoints = [54.5,64.5,74.5,84.5,94.5,104.5,114.5]
width = midpoints[1] - midpoints[0]
# | Clase | Intervalo (cm) |mid     | \(fi\) | \(Fk\) |
# |-------|----------------|--------|--------|--------|
# | 1     | 50–59          |  54,5  |8      | 8      |
# | 2     | 60–69          |  64,5  |10     | 18     |
# | 3     | 70–79          |  74,5  |16     | 34     |
# | 4     | 80–89          |  84,5  |14     | 48     |
# | 5     | 90–99          |  94,5  |10     | 58     |
# | 6     | 100–109        | 104,5  |5      | 63     |
# | 7     | 110–119        | 114,5  |2      | 65     |

# -----------------------------
# 1. Histograma de frecuencias
# -----------------------------


plt.figure(figsize=(8,5))
plt.bar(midpoints, fi, width=width, align='center', edgecolor=None, color="skyblue")
plt.xlabel("Intervalo")
plt.ylabel("Frecuencia")
plt.title("Histograma")
plt.savefig("histograma_pco_4.png")
plt.close()



