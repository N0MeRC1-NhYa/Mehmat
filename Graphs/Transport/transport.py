import osmnx as ox
import os
import math

def Dijkstra(a):
    
    distances[a] = 0
    
    while True:
        print("iteration")
        curr_key = ""
        curr_min = math.inf
            
        for i in distances.keys():    
                
            if distances[i] >= curr_min or i in visited:
                continue
                
            curr_key = i
            curr_min = distances[i]
        
        if curr_key == "":
            break       
            
            
        for neighbour, weight in edges[a]:
            distances[neighbour] = min(distances[neighbour], distances[curr_key] + weight)
            
            if distances[neighbour] == distances[curr_key] + weight:
                    path[neighbour] = path[curr_key] + str(neighbour) + "->"
        
        visited.add(curr_key)
    
    return 
            
place = ["Saratov, Russia"]
G = ox.graph_from_place(place, retain_all=True, simplify = True, network_type='all')

edges = dict()
distances = dict()

visited = {}

a = input("Введите стартовую точку: ")
b = input("Введите конечную точку: ")

path = f"{a}->"

for u, v, key, data in G.edges(keys=True, data=True):
    
    if str(u) in distances.keys():
        distances[str(u)] = math.inf
    
    if str(v) in distances.keys():
        distances[str(v)] = math.inf
    
    if str(u) in edges.keys():
        edges[str(u)].append((str(v), data["length"]))
    else:
        edges[str(u)] = [(str(v), data["length"])]

    if  data["reversed"]:
        if str(v) in edges.keys():
            edges[str(v)].append((str(u), data["length"]))
        else:
            edges[str(v)] = [(str(u), data["length"])]


print("Data read")
Dijkstra(a)
print("Dijkstra ran")
print(*distances)    

#print([i["highway"] for i in data])     
fig, ax = ox.plot_graph(G, node_size=0,edge_linewidth=0.2, dpi = 300, bgcolor = "#061529", save = False,edge_alpha=1)
fig.tight_layout(pad=0)

fig.savefig(os.path.dirname(os.path.abspath(__file__)) + "/pics/Saratov.png", dpi=300, bbox_inches='tight', format="png", 
            facecolor=fig.get_facecolor(), transparent=False)
