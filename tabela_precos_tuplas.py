#Mostra uma lista de produtos com os respetivos preços, formatada como uma tabela. Exemplo de tuplas, loops com step e formatação de strings em Python.
listagem = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Liro', 34.90)
print('-'*35)
print(f'{" "*8}Listagem de Preços')
print('-'*35)

for i in range(0, len(listagem), 2):
    print(f'{listagem[i]:.<20}R$ {listagem[i+1]:.2f}')