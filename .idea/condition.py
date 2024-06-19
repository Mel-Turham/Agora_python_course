# note = float(input('Enter your note : '))

# if note < 10 :
#   print("You'r not good")
# elif note >= 12 and note < 15 :
#   print ('Passable')
# else:
#   print('Strong')
  
  
  
# user_Number = float(input('Enter one number: '))

# if user_Number % 2 == 0 :
#   print("C'est un nombre pair")
# else:
#   print("C'est un nombre impair")


# number1 = int(input('First number : '))
# number2 = int(input('second number : '))
# number3 = int(input('Their number : '))

# if number1 > number2 and number1 > number3:
#   print(number1)
# elif number2 > number1 and number2 > number3:
#   print(number2)
# elif number3 > number1 and number3 > number2:
#   print(number3)
# else:
#   print('Les nombres sont egaux')

voyelle = "aeioyu"

characters = str(input('Enter a character : ')).lower()

if characters in voyelle:
  print(f'{characters} est une voyelle')
else:
  print(f'{characters} est une consonne')
