import matplotlib.pyplot as plt

def a(n):
    if n == 1:
        return 100
    else:
        return a(n-1) + 10
    
def b(n):
    if n == 1:
        return 100
    else:
        return a(n-1)*1.05
    
    
print("Første tilbud:")
for i in range(1, 5):
    print(f"Uke {i}: {a(i)}")
    
print()
print("Andre tilbud:")
for i in range(1, 5):
    print(f"Uke {i}: {b(i)}")