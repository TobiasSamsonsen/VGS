sum = 0
a1 = 1
a2 = 1
an = 2
nums = []

while an <= 4E6:
    if an % 2 == 0:
        sum += an
    a2 = a1
    a1 = an
    an = a1 + a2
print(sum)