def conversor_dollar(real):
    dollar = 3.27
    return real / dollar


real = float(input('Informe o valor R$  '))
print(f'O valor convertido em dolares é: {conversor_dollar(real):.2f}')