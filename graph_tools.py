import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter

# Degree Distribution
def degree_dist(G):
    # Degrees list
    degrees = [G.degree(n) for n in G.nodes()]
    
    # Degree distribution
    degree_counts = Counter(degrees)
    keys = sorted(degree_counts.keys())
    
    values = [degree_counts[k] for k in keys]
    
    # Dergee distribution normalised
    # values = [float(i) / sum(values) for i in values]
    return degrees, values, keys

# Plotting information spreading on networks
def visualise_simulations(G, positions, iterations):
    color_map = []
    for iteration in range(G.number_of_nodes()):
        color_map.append('green')

    for iteration in iterations:
        for index, status in iteration['status'].items():
            if status == 1:
                color_map[index] = 'red'
            if status == 2:
                color_map[index] = 'grey'

        nx.draw(G, positions, node_color = color_map, with_labels = True)
        plt.show()
