words = str(input('Enter a words : '))

def count_word(words):
    return len(words.split(' '))


result = count_word(words)
print(result)