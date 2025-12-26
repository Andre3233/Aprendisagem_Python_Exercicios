#Percorre uma lista de palavras e imprime todas as vogais de cada palavra. Exemplo de loops aninhados, tuplas e manipulação de strings em Python.
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'programador', 'futuro')
vogais = 'aeiouAEIOU'

for p in palavras:
    print(f'\nNa palavra {p} temos ', end = ' ')
    for letra in p:
        if letra in vogais:
            print(letra, end= ' ')