import networkx as nx
import matplotlib.pyplot as plt
import os
 
visited = set()
queue = []
 
 
def bfs(graph, cur_node, target):
    
    visited.add(cur_node)
    queue.append(cur_node)
    
    if cur_node == target:
        return True
    
    while queue:
        s = queue.pop(0)
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                if target == neighbour:
                    return True
    
    return False
                
            
        
for j in range(50):
    visited = set()
    queue = []
    with open(os.path.dirname(os.path.abspath(__file__)) + "/tests/test_"  + str(j) + ".txt", "r") as file:
        a, b = [int(i) for i in file.readline().split()]
        nodes = int(file.readline())
        graph = dict()
        for i in range(nodes):
            line = file.readline()
            graph[i] = [int(i) for i in line.split()[1:]]
            
    print(f"Test number {str(j)} gives result: {bfs(graph, a, b)}")
    

    
    # plot = nx.DiGraph(graph)
    # edges = []
    # for i in graph.keys():
    #     for j in graph[i]:
    #         edges.append([i, j])
    
    # plot.add_edges_from(edges)
    # pos = nx.spring_layout(plot, k = 2)
    # nx.draw_networkx(plot, pos=pos)
    # plt.title("From " + str(a) + " to " + str(b))
    # plt.show()