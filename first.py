while True:    
    phrase = 'The most important thing in the world is coffee.'
    print('- ' * 35)
    letter = str(input('Digite uma letra ')).lower()[0]
    print('- ' * 35)
    number = phrase.count(letter)
    if number > 1:
        print(f'Após uma profunda análise, encontramos a letra {letter} {number} vezes na string')
    elif number == 1:
        print(f'Após uma profunda análise, encontramos a letra {letter} apenas {number} vez na string')
    elif number <= 0:
        print(f'Após uma profunda análise, NÃO encontramos a letra {letter} na string')
    print('- ' * 35)
    answer = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if answer in 'N':
        break

print('=-' * 14)
print('Foi um prazer lhe atender!')
