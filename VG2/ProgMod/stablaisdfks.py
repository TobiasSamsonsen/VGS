import random
from matplotlib import pyplot as plt

N = 10000
sum = 0
size = 100
dist_list = []

n = 0

while (n < N):
    Ax = random.randint(0, size)
    Ay = random.randint(0, size)
    Bx = random.randint(0, size)
    By = random.randint(0, size)
    
    sum += ((Bx-Ax)**2 + (By-Ay)**2)**0.5
    n += 1
    
    avg = sum/(n+1)
    dist_list.append(avg)
    
x = [i for i in range(N)]
    
plt.plot(x, dist_list)
    

# x = [i for i in range(1, 100)]

# plt.plot(x, dist_list)
plt.grid()
plt.show()