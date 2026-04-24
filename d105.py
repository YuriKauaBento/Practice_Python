def notas(*d, sit=False):
    """
    Analisa as notas de vários alunos.
    :param d: uma ou mais notas dos alunos.
    :param sit: valor opcional, indicando se deve ou não acrescentar a situação.
    :return: dicionário com as informações sobre a situação da turma. 
    """
    n = {}
    n['Total'] = len(d)
    n['Maior'] = max(d)
    n['Menor'] = min(d)
    n['Média'] = sum(d) / len(d)
    if sit == True:
        if n['Média'] < 6:
            n['Situação'] = 'RUIM'
        elif n['Média'] >= 6 and n['Média'] < 7:
            n['Situação'] = 'RAZOÁVEL'
        else:
            n['Situação'] = 'BOA'
    return n


r = notas(10, 10, 8, 9, 4, 1.5, sit=True)
print(r)