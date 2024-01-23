import numpy as np

print("------ Punkt A -------")
A = np.array([int(input("X: ")), int(input("Y: "))])
print("------ Punkt B -------")
B = np.array([int(input("X: ")), int(input("Y: "))])
print("------ Punkt C -------")
C = np.array([int(input("X: ")), int(input("Y: "))])

VektorBA = B - A

print("------ Punkt D -------")
print(C- VektorBA)