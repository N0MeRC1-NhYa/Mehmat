import numpy as np
import matplotlib.pyplot as plt
import math 

def plot(matrix, title):
    X, Y = np.meshgrid(np.arange(0, size), np.arange(0, size))
    plt.contourf(X, Y, matrix)
    plt.title(title)
    plt.show()
    
def create_matrix(size):
    r = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        r[i][size - 1] = 1
        r[0][i] = 1
    
    r[size - 1][size - 1] = 0.5
    r[0][0] = 0.5
    
    return r

def analytic(x, y, max_n):
    res = 0
    for n in range(1, max_n):
        res += 2 / math.sinh(math.pi * n) * (1 - math.cos(math.pi * n)) / (math.pi * n) * (math.sinh(math.pi * n * x) * math.sin(math.pi * n * y) + math.sinh(math.pi * n * y) * math.sin(math.pi * n * x))
    
    return res
        

size = int(input("Введите размер матрицы: "))
matrix = create_matrix(size)
n = int(input("Введите число повторений цикла: "))

for i in range(n):
    for i in range(1, size - 1):
        for j in range(1, size - 1):
            matrix[i][j] = 0.25 * (matrix[i - 1][j] + matrix[i + 1][j] + matrix[i][j - 1] + matrix[i][j + 1])
    
print(np.matrix(matrix))
plot(matrix, "Изолинии")


matrix_analytic = create_matrix(size)

for i in range(1, size - 1):
        for j in range(1, size - 1):
            matrix_analytic[i][j] = analytic(i / (size - 1),j / (size - 1), n)

print(np.matrix(matrix_analytic))
plot(matrix_analytic, "Изолинии. Аналитический метод")

            