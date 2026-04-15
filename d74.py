"""from random import randint
n = []

for i in range(0, 6):
    n.append(randint(1, 50))
    
nn = tuple(n)
print(nn)
print(f'maior: {max(nn)}')
print(f'menor: {min(nn)}')"""

from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10,),
     randint(1, 10), randint(1, 10))

for m in n:
    print(f'{n} ', end=' ')

print(max(n))
print(min(n))