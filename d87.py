num = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = 0
third = 0

for i in range(0, 3):
    for c in range(0, 3):
        num[i][c] = int(input('Digite um número: '))
for i in range(0, 3):
    for e in range(0, 3):
        print(f'{num[i][e]:^5}', end='')
        if num[i][e] % 2 == 0:
            soma_par += num[i][e]
    print()

for i in range(0, 3):
    third += num[i][2]

"""for n in range(0, len(num)):
    for e in range(0, len(num[n])):
        if num[n][e] % 2 == 0:
                soma_par += num[n][e]
        if e % 3 == 0:
                third += num[n][e]"""

print(soma_par)
print(third)
print(max(num[1]))
