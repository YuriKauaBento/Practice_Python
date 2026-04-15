cidade = input('Digite o nome de sua cidade: ')
cidade = cidade.upper()
separar = cidade.split()

if separar[0] == 'SANTO':
    print('O nome de sua cidade começa com Santo.')
else:
    print('O nome de sua cidade não começa com Santo.')