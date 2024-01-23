import numpy as np

print("------ Vektor 1 -------")
u = np.array([float(input("X: ")), float(input("Y: "))])
print("------ Vektor 2 -------")
v = np.array([float(input("X: ")), float(input("Y: "))])

utregning1 = u + v
utregning2 = u - v
utregning3 = 2*u + 3*v

print(utregning1)
print(utregning2)
print(utregning3)

print(u[0])
print(v[1])