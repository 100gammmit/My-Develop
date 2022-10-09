from random import randrange
ad=[]
bd=[]
for i in range(1000):
    ad.append(list())
    bd.append(list())
    for j in range(1000):
        ad[i].append(randrange(1, 100))
        bd[i].append(randrange(1, 100))
print(ad, bd)
with open('a.dat', 'w') as file:
    for i in range(1000):      
        for a in ad[i]:
            file.write(str(a) + ' ')
        file.write('\n')
            
with open('b.dat', 'w') as file:
    for i in range(1000):      
        for b in bd[i]:
            file.write(str(b) + ' ')
        file.write('\n')        