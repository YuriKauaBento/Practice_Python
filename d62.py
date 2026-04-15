primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('digite a razao: '))
termo = primeiro
c = 1
total = 0
mais = 10

while mais > 0:
    total += mais
    while c <= total:
        print(termo, end=' ')
        print('->' if c > 1 else '', end=' ')
        termo += razao
        c += 1
    print('PAUSA')
    mais = int(input('quantos termos você quer visualizar a mais? '))

print(f'Foram calculados {termo} termos')
print('FIM')