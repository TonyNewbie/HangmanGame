word = input()
result = ''
for letter in word:
    if letter.isupper():
        result += '_' + letter.lower()
    else:
        result += letter
print(result)
