from matplotlib import pyplot as plt

m = 0.0096
g = 9.81
# cd = 0.7

s = 0
v = 0
t = 0
G = m*g

def a(v):
    D = cd*(v**2)
    sum_F = G-D
    aks = sum_F/m
    return aks

t_end = 40
dt = 0.01
s_values = [s]
v_values = [v]
a_values = [a(v)]
t_values = [t]

while s < 417:
    s += v*dt
    v += a(v)*t
    t += dt
    
    s_values.append(s)
    v_values.append(v)
    t_values.append(t)
    a_values.append(a(v))
    
plt.plot(t_values, s_values, label="Strekning")
plt.plot(t_values, v_values, label="Fart")
plt.plot(t_values, a_values, label="Akselerasjon")
plt.grid()
plt.legend()
plt.show()