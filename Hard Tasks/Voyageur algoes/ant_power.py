# Задача коммивояжера. Полным перебором; 
# генетического; муравьиного.

import matplotlib.pyplot as plt
import matplotlib
from matplotlib.widgets import Button
import math
import numpy as np

def plot(path, title):
    ax = fig.gca()
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])

    
    for i in range(len(path)):
        x1, y1 = dots[path[i][0]]
        x2, y2 = dots[path[i][1]]
        plt.plot([x1, x2], [y1, y2])
     
    for x, y in dots:
        plt.scatter(x, y)
    
    plt.title(title)
    
    plt.show()

def primitive():
    
    res = []
    node = 0
    visited.add(node)
    
    while True:
        
        min_node = [i for i in range(len(graph)) if i not in visited][0]
        
        for i in range(len(graph[node])):
            if  graph[node][i] < graph[node][min_node] and i not in visited:
                min_node = i
        
        res.append([node, min_node])
        node = min_node
        visited.add(node)
        
        if len(visited) == len(graph):
            res.append([node, 0])
            return res 
    
def btn_pressed(evt):
    dots.append((evt.xdata, evt.ydata))
    evt.inaxes.plot(evt.xdata, evt.ydata, 'o')
    fig.canvas.draw()
    
    
matplotlib.rcParams['backend'] = 'Qt5Cairo' 

fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)

ax = fig.gca()
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])

dots = []

cid = fig.canvas.mpl_connect('button_press_event', btn_pressed)

plt.title("Отметьте необходимые пункты")
plt.show()

graph = [[math.inf for i in range(len(dots))] for i in range(len(dots))]
visited = set()

for i in range(len(dots)):
    for j in range(i + 1, len(dots)):
        dist = math.sqrt((dots[i][0] - dots[j][0]) ** 2 + (dots[i][1] - dots[j][1]) ** 2) 
        graph[i][j] = dist
        graph[j][i] = dist


    
prim = primitive()
plot(prim, "Жадный алгоритм")