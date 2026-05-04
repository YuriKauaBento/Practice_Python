from utilidade import dado
from utilidade import moeda

preco = dado.leia_dinheiro('Digite o preço: R$')
moeda.resumo(preco, 10, 20)