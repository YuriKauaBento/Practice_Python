lista = []

for i in range(0,5):
    item = int(input('Digite um número: '))
    if i == 0 or item > lista[-1]:
        lista.append(item)
    else:
        pos = 0
        while pos < len(lista):
            if item <= lista[pos]:
                lista.insert(pos, item)
                break
            pos += 1
print(lista)