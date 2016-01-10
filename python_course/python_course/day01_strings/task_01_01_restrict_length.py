word = input('Enter your word: ')

result = (word[:10] + '..') if len(word) > 10 else word

print(result)