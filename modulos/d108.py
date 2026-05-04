import moeda

valor = float(input('Digite o Preço: R$'))
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'Aumentando 10% de {moeda.moeda(valor)} temos {moeda.moeda(moeda.aumentar(valor, taxa=10))}')
print(f'Diminuindo 10% de {moeda.moeda(valor)} temos {moeda.moeda(moeda.diminuir(valor, taxa=10))}')