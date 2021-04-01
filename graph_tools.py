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
