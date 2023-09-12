startradio = 580
sum = 0

for i in range(1,13):
    prodMonth = startradio+(30*(i-1))
    sum += prodMonth
    print(f"Måned {i} : {prodMonth}")
    
print(f"2021 : {sum}")

sum = 0

for i in range(1,73):
    prodMonth = startradio+(30*(i-1))
    print(f"Måned {i} : {prodMonth}")
    if i > 60:
        sum += prodMonth
print(sum)