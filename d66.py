c = soma = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    c += 1

print(f'Foram digitados {c}')
print(f'A soma entre eles é de: {soma}')