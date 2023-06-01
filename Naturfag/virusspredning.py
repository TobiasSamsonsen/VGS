import random

class Person:
    def __init__(self, position, status):
        self.position = position
        self.status = status
        
population = [] # list of all people in the population

# creating the population
for i in range(10):
    position = [random.randint(0,10), random.randint(0,10)]
    status = random.choices(["Healthy", "Immune"], weights=(90, 10))
    population.append(Person(position, status))


# simulation
for i in range(100):
    for person in population:
        