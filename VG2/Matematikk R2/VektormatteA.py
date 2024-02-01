import numpy as np

print("------ Vektor 1 -------")
u = np.array([int(input("X: ")), int(input("Y: "))])
print("------ Vektor 2 -------")
v = np.array([int(input("X: ")), int(input("Y: "))])

utregning1 = u + v
utregning2 = u - v
utregning3 = 2*u + 3*v

print(utregning1)
print(utregning2)
print(utregning3)

print(u[0])
print(v[1])