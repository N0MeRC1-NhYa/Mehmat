# Задача коммивояжера. Полным перебором; 
# генетического; муравьиного.

import matplotlib.pyplot as plt
import matplotlib
from matplotlib.widgets import Button
import math
import numpy as np

def plot(path, title):
    
    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.2)

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
    summ = 0
    res = []
    node = 0
    visited.add(node)
    
    while True:
        
        min_node = [i for i in range(len(graph)) if i not in visited][0]
        
        for i in range(len(graph[node])):
            if  graph[node][i] < graph[node][min_node] and i not in visited:
                min_node = i
        summ += graph[node][min_node]
        res.append([node, min_node])
        node = min_node
        visited.add(node)
        
        if len(visited) == len(graph):
            res.append([node, 0])
            return [res, summ] 

prev_min = math.inf

def brute_force(vis, i, summ):
    
    cur_min = []
    
    vis.append(i)
    
    if len(vis) == len(graph):
        if prev_min[-1] > summ:
            prev_min.append(summ)
            return vis.copy()
        return cur_min
    
    
    for node in range(len(graph)):
        if node not in vis:
            temp_res = brute_force(vis, node, summ + graph[i][node])
            
            if temp_res: 
                cur_min = temp_res
        
            vis.pop()
            
    return cur_min 
    
def genetic(population_size = 50, max_epoch =10_000, population_cut = 0.25, mutation = 0.3):
    
    def crossover(m, f):
        border = np.random.randint(0, len(graph))
        res = m[:border]
        for n in f:
            if n not in res: 
                res.append(n)
        
        return res
    
    epoch = 0
            
    population = []
    for i in range(population_size):
        ar = [i for i in range(len(graph))]
        np.random.shuffle(ar)
        population.append(ar) 
    while epoch < max_epoch:

        epoch += 1
        distances = []
        for i in range(population_size):
            distances.append((i, sum([graph[x][y] for x, y in zip(population[i][::], population[i][1::]) if x != "" and y != ""])))
        best_population = [population[i] for i, dist in sorted(distances, key = lambda x:x[1])[:int(population_size * population_cut)]]
        
        for i in range(population_size):
           male_p = best_population[np.random.randint(0, len(best_population))]
           female_p = best_population[np.random.randint(0, len(best_population))]
           
           male_r = np.random.random()
           female_r = np.random.random()
           
           if male_r < mutation:
               male_p = population[np.random.randint(0, population_size)]
            
           if male_r < mutation:
               female_p = population[np.random.randint(0, population_size)]
            
           population[i] = crossover(male_p, female_p)
            
    return [population[sorted(distances, key= lambda x:x[1])[0][0]], sorted(distances, key= lambda x:x[1])[0][1]]
    
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


    
prim, prim_s = primitive()
print(f"Расстояние по жадному алгоритму: {prim_s}")
plot(prim, "Жадный алгоритм")


prev_min = [math.inf]

brute = brute_force([], 0, 0)
temp = [(int(x), int(y)) for x, y in zip(brute[::], brute[1::]) if x != "" and y != "" ] 
temp.append((temp[-1][1], temp[0][0]))
print(f"Расстояние по полному перебору: {prev_min[-1]}")
plot(temp, "Полный перебор")

gen, dist = genetic()
temp = [(int(x), int(y)) for x, y in zip(gen[::], gen[1::]) if x != "" and y != "" ] 
temp.append((temp[-1][1], temp[0][0]))
print(f"Расстояние по генетическому алгоритму: {dist}")
plot(temp, "Генетический алгоритм")

