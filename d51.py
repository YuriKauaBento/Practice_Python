first = int(input('Primeiro termo: '))
sec = int(input('Razão: '))
dec = first + (10 - 1) * sec

for i in range (first, dec + sec, sec):
    print(i, end= ' ->')

print('ACABOU')