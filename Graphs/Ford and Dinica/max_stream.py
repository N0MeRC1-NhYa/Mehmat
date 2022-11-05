# Максимальный поток в сети двумя методами 
# (алгоритм Форда Фалкерсона, алгоритм диница)

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math


n = 6
graph = [[0, 6, 0, 0, 0, 9],
         [0, 0, 4, 0, 8, 5],
         [0, 0, 0, 8, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 7, 10, 0, 0], 
         [0, 0, 0, 0, 5, 0]]

visited = set()

def dfs(a, b, delta, residual_network):
    
    if a == b:
        return delta
 
    if a in visited:
        return 0
 
    visited.add(a)
    
    for neighbour in [node for node in range(len(graph[a])) if graph[a][node] > 0]:

        if neighbour not in visited and residual_network[a][neighbour] < graph[a][neighbour]:
            cur_delta = dfs(neighbour, b, min(delta, graph[a][neighbour] - residual_network[a][neighbour]), residual_network)
            
            if cur_delta > 0:
                residual_network[a][neighbour] += cur_delta
                residual_network[neighbour][a] -= cur_delta 
                return cur_delta
    return 0
    

def bfs(a, b):
    pass
    

def Ford_Falkerson(graph, a, b):
   
    max_flow = 0
    res_network = [[ 0 for i in range(n)] for j in range(n)]
    while True:
        
        delta = dfs(a, b, math.inf, res_network)
        visited.clear()
                
        if delta > 0:
            max_flow += delta
        else:
            print(f"Максимальный поток: {max_flow}")
            return res_network
        
         
edges = Ford_Falkerson(graph.copy(), 0, 3)
print(edges)

# G = nx.MultiDiGraph(edges)

# pos = nx.spring_layout(G, scale=5)

# nx.draw_networkx_nodes(G, pos, node_size=700)
# nx.draw_networkx_edges(G, pos, width=4, alpha = 0.5,  edge_color="b", arrows=True)      

# nx.draw_networkx_labels(G, pos, font_size=15, font_family="sans-serif")
# # labels = nx.get_edge_attributes(G, 'weight')
# # nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=labels)

# plt.title("Max flow")
# plt.show()  
            