#from datetime import date


def voto(nasc):
    from datetime import date
    h = date.today().year
    idade = h - nasc
    if idade < 16:
        print(f'Com {idade} anos: o voto é NEGADO!')
    elif idade >= 16 and idade < 18 or idade > 65:
        print(f'Com {idade} anos: O voto é OPICIONAL!')
    else:
        print(f'Com {idade} anos: O voto é OBRIGATÓRIO!')


ano = int(input('Em que ano você nasceu? '))
voto(ano)