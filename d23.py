numero = input('digite um número de 0 até 9999: ')
numero = list(numero)

print(f"""
        Unidades: {numero[3]}
        Dezenas:  {numero[2]}
        Centenas: {numero[1]}
        milhares: {numero[0]}
""")