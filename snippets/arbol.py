import matplotlib.pyplot as plt
import networkx as nx

# Crear grafo dirigido
G = nx.DiGraph()

# Raíz
G.add_node("root_A", label="A")

# Primer nivel: R, C, L
for child in ["R", "C", "L"]:
    child_id = f"{child}_node"
    G.add_node(child_id, label=child)
    G.add_edge("root_A", child_id)

    # Segundo nivel: MC y ML
    for sub in ["MC", "ML"]:
        sub_id = f"{sub}_{child}"
        G.add_node(sub_id, label=sub)
        G.add_edge(child_id, sub_id)

        # Tercer nivel: hojas A y B
        for leaf in ["A", "B"]:
            leaf_id = f"{leaf}_{child}_{sub}"
            G.add_node(leaf_id, label=leaf)
            G.add_edge(sub_id, leaf_id)

# Posiciones horizontales manuales
pos = {}
level1 = ["R", "C", "L"]

# Calcular altura total y centrar raíz
max_y = (len(level1)-1)*3
pos["root_A"] = (0, max_y/2)

for i, child in enumerate(level1):
    child_id = f"{child}_node"
    pos[child_id] = (1, i*3)
    for j, sub in enumerate(["MC", "ML"]):
        sub_id = f"{sub}_{child}"
        pos[sub_id] = (2, i*3 + j)
        # Hojas: primero A, luego B
        pos[f"A_{child}_{sub}"] = (3, i*3 + j)
        pos[f"B_{child}_{sub}"] = (3, i*3 + j + 0.5)

# Dibujar
plt.figure(figsize=(12, 6))

# Nodos grandes (A, R, C, L, MC, ML)
big_nodes = ["root_A"] + [f"{child}_node" for child in level1] + [f"{sub}_{child}" for child in level1 for sub in ["MC","ML"]]
nx.draw_networkx_nodes(G, pos, nodelist=big_nodes, node_size=2000, node_color="lightblue")

# Nodos pequeños (A y B repetidos)
small_nodes = [f"{leaf}_{child}_{sub}" for child in level1 for sub in ["MC","ML"] for leaf in ["A","B"]]
nx.draw_networkx_nodes(G, pos, nodelist=small_nodes, node_size=800, node_color="lightgreen")

# Etiquetas
labels = {node: data["label"] for node, data in G.nodes(data=True)}
nx.draw_networkx_labels(G, pos, labels, font_size=10)
nx.draw_networkx_edges(G, pos, arrows=True)

plt.axis("off")
plt.savefig("arbol_horizontal.png")  # guarda la imagen en archivo
