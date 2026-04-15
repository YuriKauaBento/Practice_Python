sexo = input('Informe seu sexo: [M]/[F]').strip().upper()[0]

while sexo not in 'MF':
    sexo = input('Por favor responda [M] para masculino ou [F] para feminino: ').strip().upper()[0]

print(f'Você é do sexo {sexo}')