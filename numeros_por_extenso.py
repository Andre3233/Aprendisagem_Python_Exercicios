# Converte números de 0 a 20 em palavras em português e permite ao utilizador continuar a testar quantos números quiser.

numeros = ('zero','um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez','onze','doze','treze',
           'quatorze','quinze','dezaceis','desacete','dezoito','dezanove','vinte')
while True:
    opcao = int(input('Digite um numero entre 0 e 20: '))
    while opcao < 0 or opcao > 20:
        opcao = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
    print(f'Voce digitou o numero {numeros[opcao]}')

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    elif continuar == 'N':
        break