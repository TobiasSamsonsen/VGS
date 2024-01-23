import numpy as np

def vectorLength(vector):
    return np.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)

print("------ Punkt 1 -------")
positionVector1 = np.array([float(input("X: ")), float(input("Y: ")), float(input("Z: "))])
print("------ Punkt 2 -------")
positionVector2 = np.array([float(input("X: ")), float(input("Y: ")), float(input("Z: "))])

vector = positionVector2 - positionVector1

print(f"Distance: {round(vectorLength(vector), 3)}")