import moeda

valor = float(input('Digite o Preço: R$'))
print(f'A metade de {valor} é {moeda.metade(valor)}')
print(f'O dobro de {valor} é {moeda.dobro(valor)}')
print(f'Aumentando 10% de {valor} temos {moeda.aumentar(valor, taxa=10)}')
print(f'Diminuindo 10% de {valor} temos {moeda.diminuir(valor, taxa=10)}')