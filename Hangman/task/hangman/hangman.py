# Write your code here
from random import choice
words_list = ['python', 'java', 'kotlin', 'javascript']
hidden_word = choice(words_list)
print('H A N G M A N')
word = input(f'Guess the word {hidden_word[:3] + "-" * (len(hidden_word) - 3)}: ')
if word == hidden_word:
    print('You survived!')
else:
    print('You are hanged!')
