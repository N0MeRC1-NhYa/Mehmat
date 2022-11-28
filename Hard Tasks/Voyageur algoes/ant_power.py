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
            return [res, summ + graph[node][0]] 


def brute_force(vis, i, summ):
    
    cur_min = []
    
    vis.append(i)
    
    if len(vis) == len(graph):
        summ += graph[vis[-1]][0]
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
    
def genetic(population_size = 50, max_epoch =100, population_cut = 0.25, mutation = 0.3):
    
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
            distances.append([i, sum([graph[x][y] for x, y in zip(population[i][::], population[i][1::]) if x != "" and y != ""])])
            distances[i][1] += graph[population[i][-1]][population[i][0]]
        best_population = [population[i] for i, dist in sorted(distances, key = lambda x:x[1])[:int(population_size * population_cut)]]
        
        for i in range(population_size):
           male_p = best_population[np.random.randint(0, len(best_population))]
           female_p = best_population[np.random.randint(0, len(best_population))]
           
           male_r = np.random.random()
           female_r = np.random.random()
           
           if male_r < mutation:
               male_p = population[np.random.randint(0, population_size)]
            
           if female_r < mutation:
               female_p = population[np.random.randint(0, population_size)]
            
           population[i] = crossover(male_p, female_p)
    
    result = population[sorted(distances, key= lambda x:x[1])[0][0]]
    result.append(result[0])
    
    return [result, sum([graph[x][y] for x, y in zip(result[::], result[1::]) if x != "" and y != ""])]
    
    
def ant(a = 2, b = 4, k = 0.5, evap = 0.75, max_ants = 1_00):
    
    def ant_path():
        path = []
        
        nodes = set([i for i in range(1, len(graph))])
        
        start_node = 0
        
        while nodes:
            
            p = dict()
            
            for i in nodes:
                if i != start_node:
                    p[i] = pheromone[start_node][i] ** a + 1 / (graph[start_node][i] ** b)
            
            prob_sum = sum([i for i in p.values()])
            
            
            r = np.random.random()
            
            cur_sum = 0
            for i in p.keys():
                cur_sum += p[i] / prob_sum
                if cur_sum > r:
                    path.append([start_node, i])
                    start_node = i
                    nodes.remove(i)
                    break
        path.append([path[-1][1], 0])
        return path                 
                
    
    pheromone = [[0 for i in range(len(graph))] for i in range(len(graph))]
    
    ant = 0
    while ant < max_ants:
        
        ant += 1
        path = ant_path()
        for i, j in path:
            pheromone[i][j] += k / graph[i][j]
            pheromone[j][i] += k / graph[i][j]
        
        pheromone = [[max(pheromone[i][j] - evap, 0) for i in range(len(pheromone))] for j in range(len(pheromone))]
    path = ant_path()
    return [path, sum([graph[x][y] for x, y in path if x != "" and y != ""])]

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

min_gen_dist = math.inf
min_gen_path = []
op_p_size = 0
op_p_cut = 0
op_p_mut = 0

for p_size in np.arange(15, 50, 5):
    for p_cut in np.arange(0.1, 0.4, 0.05):
        for p_mut in np.arange(0.15, 0.5, 0.05):
            gen, dist = genetic(population_size=p_size, population_cut=p_cut, mutation=p_mut)
            if dist < min_gen_dist:
                op_p_size = p_size
                op_p_cut = p_cut
                op_p_mut = p_mut
                min_gen_dist = dist
                min_gen_path = gen 

temp = [(int(x), int(y)) for x, y in zip(min_gen_path[::], min_gen_path[1::]) if x != "" and y != "" ] 
print(f"Расстояние по генетическому алгоритму: {min_gen_dist} Оптимальные параметры: размер популяции = {op_p_size} процент особей для размножения = {int(op_p_cut * 100)}% вероятность мутации = {int(op_p_mut * 100)}%")
plot(temp, "Генетический алгоритм")

min_ant_dist = math.inf
min_ant_path = []
op_a = 0
op_b = 0
op_k = 0
op_evap = 0

for a in np.arange(0.5, 3, 0.5):
    for b in np.arange(0.5, 3, 0.5):
        for k in np.arange(0.2, 2, 0.2):
            for evap in np.arange(0.25, 2, 0.25):
                ant_, dist = ant(a, b, k, evap)
                if dist < min_ant_dist:
                    op_a = a
                    op_b = b
                    op_k = k
                    op_evap = evap
                    min_ant_dist = dist
                    min_ant_path = ant_
                
print(f"Расстояние по муравьиному алгоритму: {min_ant_dist}\t Оптимальные параметры: a = {op_a} b = {op_b} k = {op_k}  evap = {op_evap}")
plot(min_ant_path, "Муравьиный алгоритм")
