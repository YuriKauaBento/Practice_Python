n = int(input('Digite um número [999 para encerrar]: '))
soma = 0
c = 0

while n != 999:
    soma += n
    n = int(input('Digite um número [999 para encerrar]: '))
    c += 1

print(f'A soma dos valores é de: {soma}')
print(f'Foram digitados {c} números')