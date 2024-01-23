import numpy as np

def vectorLength(vector):
    return np.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)

sum = 0

for x in range(-3, 4):
    for y in range(-3, 4):
        for z in range(-3, 4):
            if vectorLength(np.array([x, y, z])) == 3:
                sum += 1

print(sum)