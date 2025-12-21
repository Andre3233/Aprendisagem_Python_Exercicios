""" Jogo de Par ou Ímpar em Python.
O utilizador escolhe um número e se quer par ou ímpar. 
O computador escolhe outro número aleatório. 
O programa verifica quem ganhou e conta quantas vitórias o utilizador consegue consecutivamente. """

from random import randint

print('=-='*20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-='*20)
cont = 0
while True:
    n = int(input('Digite um valor: '))
    op = str(input('Par ou impar? [P/I] ')).strip().upper()
    while op not in 'PI':
        op = str(input('Par ou impar? [P/I] ')).strip().upper()
    bot = randint(1, 10)
    soma = n + bot
    print('-'*20)
    resultado = 'P' if soma % 2 == 0 else 'I'
    print(f"Tu jogaste {n} e o computador {bot}. Total de {soma} DEU {'PAR' if resultado == 'P' else 'IMPAR'}")
    print('-'*20)
    if op == resultado:
        cont += 1
        print('VENCESTE!')
        print('Vamos jogar de novo...')
        print('=-='*20)
    else:
        print('PERDESTE!')
        print('=-='*20)
        print(f'GAME OVER! Ganhaste {cont} vezes.')
        break
