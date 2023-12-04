import random
from matplotlib import pyplot as plt

N = 10000
sum = 0
dist_list = []

n = 0

for size in range(1, 100):
    n = 0
    while (n < N):
        Ax = random.randint(0, size)
        Ay = random.randint(0, size)
        Bx = random.randint(0, size)
        By = random.randint(0, size)
        
        sum += ((Bx-Ax)**2 + (By-Ay)**2)**0.5
        n += 1
        
    avg = sum/N
    dist_list.append(avg)
    

x = [i for i in range(1, 100)]

plt.plot(x, dist_list)
plt.grid()
plt.show()