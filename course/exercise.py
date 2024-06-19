# temperature_degree = int(input('Enter a temp to convert in Fahrenheit : ' ))

# temperature_Fahrenheit = ((9/5) * temperature_degree + 32)
# print(f'The temperature in fahrenheit is {temperature_Fahrenheit} F')


# variable1 = int(input('First number : '))
# variable2 = int(input('second number :'))

# variable1 , variable2 = variable2 , variable1

# print(f'la variable2 est {variable2}, la variable1 est {variable1}')

first_name = input("What's you  first name? : ")
last_name = input("What's your last name? : ")

full_name = 'Your full name is' + ' ' + first_name + ' ' + last_name

print(full_name)

HT = int(input('Entrer le montant HT: ' ))
TVA = 0.1925
TTC = HT +  (HT * TVA)

print(f'Votre toutes taxes comprises est: {TTC}')