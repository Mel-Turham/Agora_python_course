# number = int(input('Enter a number : '))
# somme = 0
# while number  > 0:
#   somme += number
#   number = int(input('Enter a number : '))
#   if( number < 0):
#     break
# print(somme)
  
# num = int(input('Enter a number'))

# for i in range(0 , 11):
#   multiplication = i * num
#   print(f'{i} * {num} = {multiplication}')


full_number = str(input('Enter a number : '))
somme = 0

for item in full_number:
  convert_number = int(item)
  somme += convert_number

print(somme)
