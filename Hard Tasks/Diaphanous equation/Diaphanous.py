# Решить следующее диафантово уравнение: a+2b+3c+4d=30,
# где а, b, c, d неизвестные целые положительные числа. 
# Решить 2 способами: полным перебором; с помощью генетического алгоритма

import matplotlib as plt
import numpy as np


def equation(a, b, c, d):
    return a + 2*b + 3*c + 4*d - 30

def default_run():
    default_iter_cnt = 0

    for a in range(1, 22):
        for b in range(1, 12):
            for c in range(1, 8):
                for  d in range(1, 7):
                    default_iter_cnt += 1
                    if equation(a, b, c, d) == 0:
                        print(default_iter_cnt)
                        return [a, b, c, d]
    


def genetic(population_size, mutation):

    population = [[np.random.randint(1, 30),
                np.random.randint(1, 30),
                np.random.randint(1, 30), 
                np.random.randint(1, 30)] for i in range(population_size)]
    
    while True:
        fitness_score = []
        
        for a, b, c, d in population:

            if equation(a, b, c, d) == 0:
                return [a, b, c, d]
            
            fitness_score.append(1 / equation(a, b, c, d))
        
        

        total_fitness = sum(fitness_score)

        new_population_male = []
        new_population_female  = []
        
        for i in range(population_size):
            r_m = np.random.random()
            r_f = np.random.random()
            summ = 0
            i = 0
            for j in range(len(fitness_score)):
                summ += fitness_score[j] / total_fitness
                if r_m < summ:
                    new_population_male.append(population[j]) 
                    r_m = 2
                if r_f < summ:
                    new_population_female.append(population[j])
                    r_f = 2
                    
                if r_f == r_m == 2:
                    break
                
        for i in range(population_size):
            h = np.random.randint(1,4)
            population[i] = new_population_male[i][:h] + new_population_female[i][h:]
            m = np.random.random()
            if m < mutation:
                population[i][np.random.randint(1, 4)] = np.random.randint(1, 31)
                
        
        
    
print(genetic(50, 0.5))