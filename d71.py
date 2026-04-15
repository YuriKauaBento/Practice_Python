valor = int(input('quanto quer sacar? '))
cinquenta = vinte = dez = um = 0
total = valor

while True:
    if (total - 50) >= 0:
        total -= 50
        cinquenta += 1
    elif (total - 20) >= 0:
        total -= 20
        vinte += 1
    elif (total - 10) >= 0:
        total -= 10
        dez += 1
    elif(total - 1) >= 0:
        total -= 1
        um += 1
    else:
        break

print(f"""notas de 50: {cinquenta}
notas de 20: {vinte}
notas de 10: {dez}
notas de 1: {um}
""")
