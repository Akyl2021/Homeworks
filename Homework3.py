import random
slova = ('arbuz','apelsin','grusha','vinograd','abrikos')

word = random.choice(slova)
splitted_word = list(word)
guessed = ['_' for i in splitted_word]
#
attempts = 6
while True:
    print('ягода *набери латиницей*')
    print(' '.join(guessed))
    print('жизнь: ', attempts)
    char = input('Введи букву: ').strip(' ').lower()
    if char in splitted_word:
        for i, c in enumerate(splitted_word):
            if c == char:
                guessed[i] = char
        if '_' not in guessed:
            print('ПОБЕДИЛ         жми на RUN')
            break

    else:
        attempts -= 1
    if attempts == 0:
        print('Попробуй еще раз   жми на RUN ')
        break

print(' '.join(guessed))
