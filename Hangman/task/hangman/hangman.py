from random import choice
words_list = ['python', 'java', 'kotlin', 'javascript']
right_word = choice(words_list)
hidden_word = '-' * len(right_word)
guessed_letters = set()
attempts = 8
print('H A N G M A N')
while attempts and hidden_word != right_word:
    print()
    print(hidden_word)
    letter = input('Input a letter: ')
    if letter in right_word:
        if letter not in guessed_letters:
            guessed_letters.add(letter)
            for j in range(len(right_word)):
                if letter == right_word[j]:
                    hidden_word = hidden_word[:j] + letter + hidden_word[j + 1:]
        else:
            print('No improvements')
            attempts -= 1
    else:
        print('No such letter in the word')
        attempts -= 1
else:
    if attempts == 0:
        print('You are hanged!')
    else:
        print()
        print(right_word)
        print('You guessed the word!')
        print('You survived!')
