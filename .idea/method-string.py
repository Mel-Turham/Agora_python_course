character_string = "Good day every body"

length_character = len(character_string)

one_character = character_string[2]

sub_string = character_string[2:6]

count_character = character_string.count('o')

last_character = character_string[-1]

uppercase_character = character_string.upper()
lowercase_character = character_string.lower()
move_space = character_string.strip()
string_to_array = character_string.split(' ')

capital_letter_word = character_string.title()

is_start_with = character_string.startswith('G')
is_end_with = character_string.endswith('y')

mixed_character = character_string.swapcase()

move_space_number_right = character_string.rjust(10)
move_space_number_left = character_string.ljust(20)
move_space_number_center = character_string.center(30)
position_character = character_string.find('every')
replace_character = character_string.replace('Good', 'Bad')
print(replace_character)
