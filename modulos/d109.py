import moeda

valor = float(input('Digite o Preço: R$'))
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, m=True)}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, m=True)}')
print(f'Aumentando 10% de {moeda.moeda(valor)} temos {moeda.aumentar(valor, taxa=10, m=True)}')
print(f'Diminuindo 10% de {moeda.moeda(valor)} temos {moeda.diminuir(valor, taxa=10, m=True)}')