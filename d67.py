c = 0
while True:
    n = int(input('Digite um número para visualizar seus 10 primeiros múltiplos:'))

    if n < 0:
        break
    
    for c in range(1, 11):
        print(f'{n} X {c} = {n * c}')
