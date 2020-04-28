# Write your code here
from random import choice
from string import ascii_lowercase

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
    if letter in guessed_letters:
        print('You already typed this letter')
    elif len(letter) != 1:
        print('You should print a single letter ')
    elif letter not in ascii_lowercase:
        print('It is not an ASCII lowercase letter ')
    elif letter in right_word:
        guessed_letters.add(letter)
        for j in range(len(right_word)):
            if letter == right_word[j]:
                hidden_word = hidden_word[:j] + letter + hidden_word[j + 1:]
    else:
        print('No such letter in the word')
        guessed_letters.add(letter)
        attempts -= 1
else:
    if attempts == 0:
        print('You are hanged!')
    else:
        print()
        print(right_word)
        print('You guessed the word!')
        print('You survived!')
