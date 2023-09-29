def f(x):
    return (1/9)*(x+1)*(x-6)**2

x_min = int(input("Min: "))

x_max = int(input("Max: "))

n = int(input("Antall rektangler: "))

width = (x_max - x_min)/n

area1 = 0
area2 = 0

for i in range(n):
    if f(i*width) <= f((i+1)*width):
        area1 += f(i*width)*width
    else:
        area1 += f((i+1)*width)*width
    
for i in range(n):
    area2 += f(i*width)*width
    
print(f"Areal med geogebra LowerSum funksjon: {round(area1, 4)}")
print(f"Areal med oppgaven sin metode: {round(area2, 4)}")