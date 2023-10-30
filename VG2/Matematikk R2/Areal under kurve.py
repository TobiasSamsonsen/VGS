import math

def f(x):
    return 3*(math.e**(-(x**2)/2))

# Antall rektangler:
num = 4

# Venstremetoden
x = -2
dx = 4/num
areal = 0

while x < 2:
    areal += f(x)*dx
    x += dx
    
print(f"Areal med venstremetoden = {round(areal, 3)}")

# Høyremetoden
x = -2
dx = 4/num
areal = 0

while x < 2:
    areal += f(x+dx)*dx
    x += dx
    
print(f"Areal med høyremetoden = {round(areal, 3)}")

# Midtmetoden
x = -2
dx = 4/num
areal = 0

while x < 2:
    areal += f(x+(dx/2))*dx
    x += dx
    
print(f"Areal med midtmetoden = {round(areal, 3)}")

# Trapesmetoden
x = -2
dx = 4/num
areal = 0

while x < 2:
    areal += ((f(x)+f(x+dx))/2)*dx
    x += dx
    
print(f"Areal med trapesmetoden = {round(areal, 3)}")