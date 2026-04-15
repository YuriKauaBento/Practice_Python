exp = input('Digite uma expressão algébrica: ')
lista = []

for sim in exp:
    if sim == '(':
        lista.append('(')
    elif sim == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) == 0:
    print('A expressão é válida!')
else:
    print('A expressão não é válida!')
