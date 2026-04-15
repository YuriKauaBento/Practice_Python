peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura * altura)

if imc <= 18.5:
    print(f'Seu IMC é {imc:.2f} e você está abaixo do peso')
elif 18.5 < imc >= 25:
    print(f'Seu IMC é {imc:.2f} e você está no seu peso ideal')
elif 25 < imc >= 30:
    print(f'Seu IMC é {imc:.2f} e você está com sobrepeso')
elif 30 < imc >= 40:
    print(f'Seu IMC é {imc:.2f} e você está em obesidade')
else:
    print(f'Seu IMC é {imc:.2f} e você está em obesidade mórbida')