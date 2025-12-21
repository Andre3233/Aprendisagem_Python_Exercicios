'''
Programa em Python que permite adicionar produtos com seus preços, conta quantos custam mais de 1000, identifica o mais barato e mostra o total da compra. Ideal para treinar loops, condicionais e validação de input.
'''

print('-'*30)
print(f'{" "*13}LOJA ')
print('-'*30)

total = mais1000 = 0 # mais1000 são os produtos que custão mais de 1000
barato = None #para detetar e ficar com o preço do 1ºproduto
pbarato = '' #pbarato é o produto mais barato
while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: '))

    while preco <= 0: #Não existem produtos com preço 0 então volta a pedir o preço
        preco = float(input('Preço: '))
    total += preco
    if preco > 1000:
        mais1000 += 1
    if barato is None or barato > preco:
        barato = preco
        pbarato = produto

    continuar = str(input('Queres continuar [S/N]? ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Queres continuar [S/N]? ')).strip().upper()
    if continuar == 'N':
        break

print('-'*30,end= ' ')
print(' FIM DO PROGRAMA ', end= ' ')
print('-'*30)
print(f'O total da compra foi R${total:.2f}')
print(f'A {mais1000} produtos que custão mais de R$1000.00')
print(f'O produto mais barato foi {pbarato} que custo R${barato:.2f}')