def a(n):
    if n == 1:
        return a1
    else:
        return a(n-1) + n

a1 = 2

print(f"a(6) = {a(6)}")

print("-------------------")

for i in range(1, 11):
    print(f"a({i}) = {a(i)}")
    
    
print("-------------------")    
sum = 0

for i in range(1, 101):
    sum += a(i)
    
print(f"Summen av de 100 første leddene er {sum}")

print("-------------------")

sum = 0
i = 10
while sum <= 2000:
    sum += a(i)
    i += 1
    
print(f"Det minste n slik at summen av de n første leddene er større enn 2000 er {i-1}")