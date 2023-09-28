def p(n):
    return (3/2)*n**2 - (1/2)*n

sum = 0
for n in range(1, 10):
    sum += p(n)
    print(sum)