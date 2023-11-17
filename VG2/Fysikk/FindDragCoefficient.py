from math import pi

m = 0.0096
g = 9.81
p = 1.225 #kg/m^3
A = pi * 0.008**2 #pi*r**2


s = 0
v = 0
t = 0
dt = 0.0001

def a(v):
    if v < 1:
        Fd = (1/2)*(p)*(v)*(Cd)*(A)
    else:
        Fd = (1/2)*(p)*(v**2)*(Cd)*(A)
    # print(f"Cd = {Cd}\t Fd = {Fd}")
    F = (m*g) - (Fd)
    a = F/m
    return a

for Cd in range(0, 1001):
    Cd /= 1000
    s = 0
    v = 0
    t = 0
    
    while s < 800:
        s += v*dt
        v += a(v)*dt
        t += dt
    print(f"Tid = {t:0.6f}s\t Cd = {Cd}")