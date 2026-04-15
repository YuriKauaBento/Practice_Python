def calcular_media(n1, n2):
    media = (n1 + n2) / 2
    return media

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

print(f'Sua média é: {calcular_media(n1, n2):.1f}')