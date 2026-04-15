primeiro = int(input('digite o primeiro termo: '))
razao = int(input('digite o segundo termo: '))
termo = primeiro
c = 1

while c <= 10:
    print(termo, end=' ')
    print('->' if c < 10 else '', end=' ')
    termo += razao
    c += 1

print('FIM')