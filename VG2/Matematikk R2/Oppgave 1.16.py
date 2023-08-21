rekke = [1,1]

for n in range(2,21):
    rekke.append(rekke[n-2] + rekke[n-1])
    
print(rekke)

for i in rekke:
    if rekke.index(i) > 0:
        print(rekke[rekke.index(i)] / rekke[rekke.index(i)-1])
        
print("---------------------")
print((1+(5**(1/2)))/2)

# Forholdet mellom an og an-1 nærmer seg det gylne snitt