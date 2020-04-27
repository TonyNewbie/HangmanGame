# Write your code here
from random import choice
words_list = ['python', 'java', 'kotlin', 'javascript']
right_word = choice(words_list)
hidden_word = '-' * len(right_word)
print('H A N G M A N')
for i in range(8):
    print()
    print(hidden_word)
    letter = input('Input a letter: ')
    if letter in right_word:
        for j in range(len(right_word)):
            if letter == right_word[j]:
                hidden_word = hidden_word[:j] + letter + hidden_word[j + 1:]
    else:
        print('No such letter in the word')
print('\nThanks for playing!')
print('We\'ll see how well you did in the next stage')
