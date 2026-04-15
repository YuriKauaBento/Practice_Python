def aluguel(dias, km):
    valorf = dias * 60.0 + km * 0.15
    return valorf


dias = float(input('Quantos dias o carro foi utilizado? '))
km = float(input('Quantos quilometros foram rodados? '))
print(f'O valor total do aluguel é: R${aluguel(dias, km)}')