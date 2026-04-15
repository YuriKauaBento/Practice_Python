cont = 0
soma = 0

for i in range(1, 7):
    num = int(input(f'digite o valor {i}: '))
    if num % 2 == 0:
     cont += 1
     soma += num

print(f'Você informou {cont} números')
print(f'A soma desses valores é: {soma}')