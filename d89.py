grade = []

while True:
    aluno = [0, 0, 0]
    aluno[0] = input('Nome: ')
    aluno[1] = float(input('Nota 1: '))
    aluno[2] = float(input('Nota 2: '))
    grade.append(aluno)
    aluno.clear
    op = input('Quer continuar? [S]/[N]')
    if op in 'Nn':
        break

print('-='*30)
print(f'{'No.':<4}{'NOME':<10}{'MEDIA':>8}')
print('-'*30)
for i in range(0, len(grade)):
    media = (grade[i][1] + grade[i][2]) / 2
    print(f'{i:<4}{grade[i][0]:<10}{media:>8}')

while True:
    n = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if n == 999:
        break
    print(f'As notas de {grade[n][0]} são [{grade[n][1]}, {grade[n][2]}]')
    