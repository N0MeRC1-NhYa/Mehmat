import networkx as nx
import matplotlib.pyplot as plt
import os
 
visited = set()
 
 
def dfs(graph, cur_node, target):
    
    if cur_node == target:
        return True
 
    if cur_node in visited:
        return False
 
    visited.add(cur_node)
    for neighbour in graph[cur_node]:
        if neighbour not in visited and dfs(graph, neighbour, target):
            return True
 
    return False
 
for j in range(50):
    visited = set()
    with open(os.path.dirname(os.path.abspath(__file__)) + "/tests/test_"  + str(j) + ".txt", "r") as file:
        a, b = [int(i) for i in file.readline().split()]
        nodes = int(file.readline())
        graph = dict()
        for i in range(nodes):
            line = file.readline()
            graph[i] = [int(i) for i in line.split()[1:]]
            
    print(f"Test number {str(j)} gives result: {dfs(graph, a, b)}")
    
    # plot = nx.DiGraph(graph)
    # edges = []
    # for i in graph.keys():d
    #     for j in graph[i]:
    #         edges.append([i, j])
    
    # plot.add_edges_from(edges)
    # pos = nx.spring_layout(plot, k = 2)
    # nx.draw_networkx(plot, pos=pos)
    # plt.title("From " + str(a) + " to " + str(b))
    # plt.show()