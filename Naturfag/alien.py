import random
from matplotlib import pyplot as plt
import numpy as np

colonylist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dead = 0
colonies = 100
generations = 20

for i in range(1, colonies+1):
    genlist = [1]
    counted = 0
    uncounted = 1
    
    for j in range(1, generations):
        while uncounted > 0:
            terning = random.randint(1,4)
            
            if terning == 1:
                uncounted -=1
                
            elif terning == 2:
                counted += 1
                uncounted -=1
                
            elif terning == 3:
                counted += 2
                uncounted -=1
                
            elif terning == 4:
                counted += 3
                uncounted -=1
                
        uncounted = counted
        counted = 0
        genlist.append(uncounted)
        
        if uncounted == 0:
            dead += 1
            break
        
        colonylist += genlist
        
    colonylist = [x + y for x, y in zip(colonylist, genlist)]

colonylist = [x/colonies for x in colonylist]
print(colonylist)
print(f"Dead colonies: {dead}")

x = np.linspace(1,generations, generations)
plt.plot(x, colonylist, label="Gjennomsnittlige aliens per koloni")
plt.grid()
plt.legend()
plt.show()