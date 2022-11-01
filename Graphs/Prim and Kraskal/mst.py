# Построение линейного остовного дерева, 
# взвешенного, связанного, неориентированного 
# графа двумя методами (алгоритм Прима, алгоритм Краскаля)
import networkx as  nx
import matplotlib.pyplot as plt
import numpy as np

n = 7

edges = [[1, 2, 3],
         [0, 3, 4],
         [3, 5, 2],
         [2, 4, 5],
         [4, 6, 3], 
         [5, 2, 2],
         [1, 5, 7],
         [0, 4, 4],
         [4, 3, 7],
         [2, 3, 5],
         [0, 6, 5]]

def Kraskal(g_edges):
    
    parent = [i for i in range(n)]
    
    def find_parent(v):
        
        if v == parent[v]:
            return v
        
        return find_parent(parent[v])
    
    nodes = set(range(n))
    result_edges = []
    
    g_edges = sorted(g_edges, key=lambda x:x[2])
    weight_sum = 0
    
    for i in range(len(g_edges)):
        
        if find_parent(g_edges[i][0]) != find_parent(g_edges[i][1]):
            
            weight_sum += g_edges[i][2]
            result_edges.append(g_edges[i][:2])
            parent = [parent[g_edges[i][0]] if p == parent[g_edges[i][1]] else p for p in parent]    
    
    print(f"Вес минимального оставного дерева по Краскалу: {weight_sum}")
    return result_edges

def Prim(g_edges):
    
    nodes = set(range(n))
    result_edges = []
    queue = [min(g_edges, key= lambda x: x[2])]
    weight_sum = 0
    
    while nodes:
        
        cur_edge = queue.pop(0)
        
        nodes.difference_update(cur_edge[:2])
        result_edges.append(cur_edge[:2])
        weight_sum += cur_edge[2]
    
        queue = [e for e in g_edges if (e[0] not in nodes) ^ (e[1] not in nodes)]
        queue = sorted(queue, key=lambda x: x[2])
    
    print(f"Вес минимального оставного дерева по Приму: {weight_sum}")
     
    return result_edges


def draw_graph(alg_res, alg_title):
    G = nx.Graph()
    G.add_weighted_edges_from(edges)

    pos = nx.shell_layout(G)

    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos, width=4, alpha = 0.5,  edge_color="b")      

    nx.draw_networkx_edges(G, pos, width=6, edge_color="r",edgelist=alg_res)

    nx.draw_networkx_labels(G, pos, font_size=15, font_family="sans-serif")
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=labels)

    plt.title(f"{alg_title} MST")
    plt.show()  


Kraskal_edges = Kraskal(edges.copy())
Prim_edges = Prim(edges.copy())

draw_graph(Kraskal_edges, "Kraskal")
draw_graph(Prim_edges, "Prim")
