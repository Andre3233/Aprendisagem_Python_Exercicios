#Permite ao utilizador inserir 4 números, mostra quantas vezes o número 9 aparece, a posição do primeiro 3 e lista os números pares.
n = tuple(int(input(f'Digite o {i+1}º valor: ')) for i in range(4))

print(f'Digitaste os seguintes valores {n}')
print(f'O numero 9 apareceu {n.count(9)} vezes')
print(f'O primeiro numero 3 esta na posição {n.index(3)}')
pares = tuple(i for i in n if i % 2 == 0)
print(f'Os numeros pares são: {pares}')