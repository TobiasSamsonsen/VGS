import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as so

data_x = [0.1, 0.3, 0.5, 0.8, 1.0, 1.3, 1.6, 2.0]
data_y = [0.69, 1.17, 1.44, 1.82, 2.08, 2.27, 2.53, 2.80]

plt.plot(data_x, data_y, "o")

def f(x, a, k, c, d):
    return a*np.sin(k*x+c)+d

konstanter = so.curve_fit(f, data_x, data_y)[0]

a = konstanter[0]
k = konstanter[1]
c = konstanter[2]
d = konstanter[3]

print(f"f(x) = {a}sin({k}x + {c}) + {d}")

x = np.linspace(data_x[0], 10,  1000)

plt.plot(x, f(x, a, k, c, d), color="r")
plt.grid()
plt.show()

