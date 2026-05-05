from lib.interface import *
from lib.arquivo import *

arq = 'dados.txt'

if not arq_existe(arq):
    criar_arquivo(arq)

while True:
    resposta = menu(['Consultar pessoas cadastras', 'Cadastrar pessoas', 'Sair do programa'])
    if resposta == 1:
        ler_arquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    else:
        break
