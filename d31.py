distancia = float(input('Informe a distância da viagem: '))

if distancia <= 200:
    print(f'Valor da viagem: {distancia * 0.5}')
else:
    print(f'Valor da viagem: {distancia * 0.45}')