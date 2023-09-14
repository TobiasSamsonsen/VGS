# Oppgave 1.22, side 50

import matplotlib.pyplot as plt

s = 0
v = 0
t = 0

s_end = 100
dt = 0.001
s_values = [s]
v_values = [v]

def a(v):
    aks = -0.5*v + 6
    return aks
while s < s_end:
    v += a(v)*dt
    s += v*dt
    t += dt
    s_values.append(s)
    v_values.append(v)
    
plt.plot(s_values, v_values, label="v(s)")
plt.legend()
plt.grid()
plt.title("Fart som funksjon av posisjon")
plt.xlabel("$s$ (m)")
plt.ylabel("$v$ (m/s)")
plt.show()