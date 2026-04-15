v = []

for i in range(0, 5):
    v.append(int(input('Digite um número: ')))

print(f'O menor número é o {min(v)} que está na posição {v.index(min(v))}')
print(f'O maior número é o {max(v)} que está na posição {v.index((max(v)))}')