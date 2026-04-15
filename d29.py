vel = int(input('Informe a velocidade do carro: '))

if vel > 80:
    print(f'Você foi multado! Valor da multa: {(vel - 80) * 7}')