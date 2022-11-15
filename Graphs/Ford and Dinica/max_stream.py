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

def dfs_Falk(a, b, delta, residual_network):
    
    if a == b:
        return delta
 
    if a in visited:
        return 0
 
    visited.add(a)
    
    for neighbour in [node for node in range(len(graph[a])) if graph[a][node] > 0]:

        if neighbour not in visited and residual_network[a][neighbour] < graph[a][neighbour]:
            cur_delta = dfs_Falk(neighbour, b, min(delta, graph[a][neighbour] - residual_network[a][neighbour]), residual_network)
            
            if cur_delta > 0:
                residual_network[a][neighbour] += cur_delta
                residual_network[neighbour][a] -= cur_delta 
                return cur_delta
    return 0
    

def Ford_Falkerson(a, b):
   
    max_flow = 0
    res_network = [[ 0 for i in range(n)] for j in range(n)]
    while True:
        
        delta = dfs_Falk(a, b, math.inf, res_network)
        visited.clear()
                
        if delta > 0:
            max_flow += delta
        else:
            print(f"Максимальный поток: {max_flow}")
            return res_network
        
queue = list()
dist = [math.inf for i in range(n)]

def dfs_Din(a, b, delta, residual_network):
    if a == b:
        return delta
 
    if a in visited:
        return 0
 
    visited.add(a)
    
    for neighbour in [node for node in range(len(graph[a])) if graph[a][node] > 0]:

        if dist[a] == dist[neighbour] + 1:
            cur_delta = dfs_Din(neighbour, b, min(delta, graph[a][neighbour] - residual_network[a][neighbour]), residual_network)
            
            if cur_delta != 0:
                residual_network[a][neighbour] += cur_delta
                residual_network[neighbour][a] -= cur_delta 
                return cur_delta
    return 0
    
def bfs(a, b, res_network):
    
    queue.append(a)
    dist[a] = 0
    
    while queue:
        
        s = queue.pop(0)
        for neighbour in [i for i in range(len(graph[s])) if graph[s][i] > 0]:
            
            if res_network[s][neighbour] < graph[s][neighbour] and dist[s] != math.inf:
                dist[neighbour] = dist[a] + 1
                queue.append(neighbour)
    
    return dist[b] != math.inf


def Dinica(a, b):
    
    res_network = [[ 0 for i in range(n)] for j in range(n)]
    
    max_flow = 0
    while bfs(a, b, res_network):
        
        flow = dfs_Din(a, b, 0, res_network.copy())
        while flow != 0:
            visited.clear()
            max_flow += flow
            flow = dfs_Din(a, b)
            print(flow)
            
        for i in range(n):
           dist[i] = math.inf


        
    
    print(f"Максимальный поток по Динице: {max_flow}")
    return res_network


def graph_show(title):
    
    G = nx.MultiDiGraph(np.matrix(graph) - np.matrix(edges))

    pos = nx.spiral_layout(G)

    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos, width=2, alpha = 0.5,  edge_color="b", arrowstyle="->", arrowsize=15, min_target_margin=12)      

    nx.draw_networkx_labels(G, pos, font_size=15, font_family="sans-serif")

    labels = nx.get_edge_attributes(G, 'weight')

    t_labels = dict()
    for label in labels.keys():
        t_labels[(label[0], label[1])] = labels[label]

    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=t_labels)

    plt.title(f"Максимальный поток {title}")
    plt.show()  
    
         
edges = Ford_Falkerson(0, 3)
graph_show("Фалкерсона")

edges = Dinica(0, 3)
graph_show("Диница")



            