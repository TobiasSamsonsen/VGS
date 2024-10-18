import matplotlib as plt
import numpy as np

def f(x):
    return (x-1)**2 * np.exp(x) - 0.5

def df(x):
    return (f(x+h) - f(x))/h

def newton_raphson(a, b, accuracy):
    x = (a+b)/2
    
    while abs(f(x)) > accuracy:
        x -= f(x)/df(x)
        
    return x

h = 1E-7

# Oppgave C
# Vis, ved å bruke skjæringssetningen, at denne ligningen har tre løsninger, ett i hvert av intervallene [-5, -1], [-1, 1] og [1, 2]

print(f"f(-5) = {round(f(-5), 6)}, f(-1) = {round(f(-1), 6)}")
print(f"f(-1) = {round(f(-1), 6)}, f(1) = {round(f(1), 6)}")
print(f"f(1) = {round(f(1), 6)}, f(2) = {round(f(2), 6)}")
print(f"\nVi ser at i alle intervallene er det forskjellig fortegn mellom f(a) og f(b), \ndermed har ligningen, i følge skjæringssetningen, en løsning i hvert av intervallene [-5, -1], [-1, 1] og [1, 2]")


print("------------------------------------")
# Oppgave D
''' Bruk Python til å finne en numerisk tilnærming til alle disse tre løsningene til 6 desimalers nøyaktighet. 
Bruk Newton-Raphsons metode og velg passende startverdi for de tre forskjellige løsningene. 
Hvilke startverdier dere valgte må komme fram av besvarelsen deres.
OBS: Pass på å ikke bruk ekstremalverdier som startverdi! (hvorfor ikke?) '''

print(f"Skjæring ved x-akse i intervallet [-5, -1]: x = {round(newton_raphson(-5, -1, 1E-6), 6)}")
print(f"Skjæring ved x-akse i intervallet [-1, 1]: x = {round(newton_raphson(-1, 1, 1E-6), 6)}")
print(f"Skjæring ved x-akse i intervallet [1, 2]: x = {round(newton_raphson(1, 2, 1E-6), 6)}")

print(f"\nJeg valgte startverdiene til å være midtpunktet i intervallet.\nDette fordi det minsker sjansen for at metoden divergerer.\nJeg opplevde at metoden divergerte når jeg valgte a som startverdi i intervallene [a, b], siden disse var i nærheten av ekstremalpunkter")