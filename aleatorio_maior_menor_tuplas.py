#Gera 5 números aleatórios entre 0 e 10, mostra os valores sorteados e indica qual é o maior e o menor número.
from random import randint

n = tuple(randint(0, 10) for _ in range(5))
print(f'Os valores surteados foram: {n}')
print(f'O maior numero é {max(n)}')
print(f'O menor numero é {min(n)}')