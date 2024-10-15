import matplotlib as plt
import numpy as np

def f(x):
    return (x-1)**2 * np.exp(x) - 0.5

def df(x):
    return (f(x+h) - f(x))/h

def newton_raphson(a, b, accuracy):
    x = a
    
    
    while (x - f(x)/df(x)) < a or (x - f(x)/df(x)) > b:
        x += 0.01
    
    while abs(f(x)) > accuracy:
        if f(a)*f(x) < 0:
            x = x + f(x)/df(x)
        else:
            x = x - f(x)/df(x)
        
    return x

h = 1E-7

# Oppgave C
# Vis, ved å bruke skjæringssetningen, at denne ligningen har tre løsninger, ett i hvert av intervallene [-5, -1], [-1, 1] og [1, 2]

print(f"f(-5) = {f(-5)}, f(-1) = {f(-1)}, f-verdiene har forskjellig fortegn, så det er en skjæring i intervallet [-5, -1]")
print(f"f(-1) = {f(-1)}, f(1) = {f(1)}, f-verdiene har forskjellig fortegn, så det er en skjæring i intervallet [-1, 1]")
print(f"f(1) = {f(1)}, f(2) = {f(2)}, f-verdiene har forskjellig fortegn, så det er en skjæring i intervallet [1, 2]")


print("------------------------------------")
# Oppgave D
''' Bruk Python til å finne en numerisk tilnærming til alle disse tre løsningene til 6 desimalers nøyaktighet. 
Bruk Newton-Raphsons metode og velg passende startverdi for de tre forskjellige løsningene. 
Hvilke startverdier dere valgte må komme fram av besvarelsen deres.
OBS: Pass på å ikke bruk ekstremalverdier som startverdi! (hvorfor ikke?) '''

print(f"Skjæring ved x-akse: x = {round(newton_raphson(-5, -1, 1E-6), 6)}")
print(f"Skjæring ved x-akse: x = {round(newton_raphson(-1, 1, 1E-6), 6)}")
print(f"Skjæring ved x-akse: x = {round(newton_raphson(1, 2, 1E-6), 6)}")