
number = int(input('Enter an number : ' ))

def isEven_Odd (number):
   if number % 2 == 0 :
     return True
   else:
     return False
   
print(isEven_Odd(number))


char = str('Enter a word :')

def len_of_word(char):
  length = 0
  for item in char:
    length = length + 1
  return length 


print(len_of_word('Hello'))