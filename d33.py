a = int(input('Digite um numero '))
b = int(input('Digite um numero '))
c = int(input('Digite um numero '))
menor = a
maior = a

if a > b and b < c:
    menor = b
elif a > c and c < b:
    menor = c

if a < b and b > c:
    maior = b
elif a < c and c > b:
    maior = c

print(f'maior: {maior}')
print(f'Menor: {menor}')