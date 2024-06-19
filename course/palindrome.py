text = input('Enter a word: ')

def palindrome(text):
  text = text.lower()
  text = ''.join(e for e in text if e.isalnum())
  print(text)
  return text == text[::-1]

if palindrome(text):
  print(f'{text} is a palindrome.')
else:
  print(f'{text} is not a palindrome.')
  
  print()