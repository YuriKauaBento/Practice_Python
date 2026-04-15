n = media = c = maior = menor =  0
opcao = ''

while opcao != 'N':
    n = int(input('Digite um número: '))
    media += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if maior < n:
            maior = n
        if menor > n:
            menor = n
    opcao = input('Deseja continuar? [S]/[N]: ').strip().upper()[0]

print(f'Você digitou {c}, a média entre eles é de: {media / c}')
print(f'O maior número digitado foi {maior} e o menor foi {menor}')