import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

with open('matrix.txt', 'r') as f:
    matrix = []
    for line in f:
        matrix.append([int(x) for x in line.split()])

G = nx.from_numpy_array(np.array(matrix), create_using=nx.Graph)

pos = nx.spring_layout(G)
nx.draw(G, pos)
labels = {i: i for i in range(len(G.nodes))}
nx.draw_networkx_labels(G, pos, labels)

plt.show()