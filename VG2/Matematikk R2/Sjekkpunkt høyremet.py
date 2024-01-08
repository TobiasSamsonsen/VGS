def f(x):
    return 3*(x**0.5)
    
n = 10000
x = 0
end = 9
dx = (end - x)/n

sum = 0

while x < end:
    sum += f(x+dx)*dx
    x += dx
    
print(round(sum, 1))