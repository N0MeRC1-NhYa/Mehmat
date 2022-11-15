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
    
    if a == b or delta == 0:
        return delta
    
    for neighbour in [node for node in range(len(graph[a])) if graph[a][node] > 0]:

        if dist[a] + 1 == dist[neighbour]:
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
                dist[neighbour] = dist[s] + 1
                queue.append(neighbour)
    
    return dist[b] != math.inf


def Dinica(a, b):
    
    res_network = [[ 0 for i in range(n)] for j in range(n)]
    
    max_flow = 0
    while bfs(a, b, res_network):
        print(*dist)
        flow = dfs_Din(a, b, math.inf, res_network)
        
        while flow != 0:
            max_flow += flow
            flow = dfs_Din(a, b, math.inf, res_network)
            
        for i in range(n):
           dist[i] = math.inf
        print(*dist)

    print(f"Максимальный поток по Динице: {max_flow}")
    return res_network


def graph_show(title):
    
    F = nx.MultiDiGraph(np.matrix(graph))
    pos = nx.shell_layout(F)
    nx.draw_networkx_edges(F, pos, width=2,  edge_color="b", arrowstyle="->", arrowsize=15, min_target_margin=12)
    labels = nx.get_edge_attributes(F, 'weight')

    t_labels = dict()
    for label in labels.keys():
        t_labels[(label[0], label[1])] = labels[label]

    nx.draw_networkx_edge_labels(F, pos=pos, edge_labels=t_labels, verticalalignment="top", label_pos=0.3)
    
    
    e = np.matrix(edges)
    e[e > 0] = 0
    E = nx.MultiDiGraph(e)
    pos = nx.shell_layout(E)
    nx.draw_networkx_edges(E, pos, width=2, connectionstyle="arc3,rad=0.2", edge_color="r", arrows=True, arrowstyle="->", arrowsize=15)
    l = nx.get_edge_attributes(E, "weight")
    nl = dict()
    for label in l.keys():
        nl[(label[0], label[1])] = l[label]
    nx.draw_networkx_edge_labels(E, pos,edge_labels=nl, verticalalignment="bottom", label_pos=0.3)
    
    G = nx.compose(F, E)
    pos = nx.shell_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos)      
    
    nx.draw_networkx_labels(G, pos, font_size=15, font_family="sans-serif")

    plt.title(f"Максимальный поток {title}")
    plt.show()  
    
         
# edges = Ford_Falkerson(0, 3)
# graph_show("Фалкерсона")

edges = Dinica(0, 3)
#graph_show("Диница")


            