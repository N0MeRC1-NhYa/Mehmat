import numpy as np
import os


if not os.path.exists("/".join(os.path.abspath(__file__).split("/")[:-1]) + "/tests/"):
    os.mkdir("/".join(os.path.abspath(__file__).split("/")[:-1]) + "/tests/")

for i in range(50):
    with open(os.path.dirname(os.path.abspath(__file__)) + "/tests/test_" + str(i) + ".txt", "w") as file:
        nodes = np.random.randint(15)
        a = np.random.randint(nodes) if nodes > 0 else 0
        b = np.random.randint(nodes) if nodes > 0 else 0
        
        while a == b and nodes > 1:
            b = np.random.randint(nodes) if nodes > 0 else 0
        
        string = str(a) + " " + str(b) + "\n"
        string += str(nodes) + "\n"
        
        for j in range(nodes):
            edges = np.random.randint(nodes, size=int(np.random.randint(20) / np.random.uniform(1.5, 4)))
            generated_values = set(edges.tolist())
            generated_values.discard(j)
            string += str(j) + " " + " ".join(map(str, sorted(list(generated_values)))) + "\n"
        
        file.write(string)