import networkx as nx
import matplotlib.pyplot as plt
import os
import math
import numpy as np

for j in range(4, 5): 
    
    graph = []
    
    with open(os.path.dirname(os.path.abspath(__file__)) + "/tests/test_"  + str(j) + ".txt", "r") as file:
        
        a, b = [int(i) for i in file.readline().split()]
        n = int(file.readline())              
        
        for i in range(n):
            graph.append([int(i) for i in file.readline().split()]) 

    visited = set()
    distances = [math.inf] * n
    path = dict()
    
    distances[a] = 0
    path[a] = f"{a}->"

    while True:
        
        # В начале необходимо найти досигаемый на текущей 
        # итерации узел с минимальным расстоянием до него
        
        curr_index = n + 1
        curr_min = math.inf
        
        for i in range(n):    
            
            if distances[i] >= curr_min or i in visited:
                continue
            
            curr_index = i
            curr_min = distances[i]
        
        # Если не нашлось индекса с которым мы можем 
        # работать на текущей итерации значит мы либо 
        # прошли по всем вершинам, либо наш граф несвязный
        
        if curr_index == n + 1:
            break       
        
        for neighbour in range(n):
            
            if graph[curr_index][neighbour] > 0:
                distances[neighbour] =  min(distances[neighbour],
                                            distances[curr_index] + graph[curr_index][neighbour])
                
                if distances[neighbour] == distances[curr_index] + graph[curr_index][neighbour]:
                    path[neighbour] = path[curr_index] + str(neighbour) + "->"
        
        visited.add(curr_index)

    print(f"Distance from {a} to {b} is {distances[b]}. Path is {path[b][:-2]}")      


    G = nx.Graph(np.matrix(graph))
    pos = nx.shell_layout(G)

    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(     G, pos, width=4, alpha = 0.5,  edge_color="b")    

    m = path[b].split("->")
    desired_path = { (int(x), int(y)) for x, y in zip(m[::], m[1::]) if x != "" and y != "" }   

    nx.draw_networkx_edges(G, pos, width=6, edge_color="r",edgelist=desired_path)

    nx.draw_networkx_labels(G, pos, font_size=15, font_family="sans-serif")
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=labels)

    plt.title("From " + str(a) + " to " + str(b))
    plt.show()   

