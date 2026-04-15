def liquidacao():
    preco = float(input('Informe o valor do produto: '))
    valorf = preco - (preco * 5/100)
    return print(f'O valor do produto com desconto é de {valorf:.2f}')


liquidacao()
