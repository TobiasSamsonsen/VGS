import numpy as np

def vectorLength(vector):
    return np.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)

vector = np.array([float(input("X: ")), float(input("Y: ")), float(input("Z: "))])

print(round(vectorLength(vector), 3))