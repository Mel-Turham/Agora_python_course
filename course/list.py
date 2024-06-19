users = ['John', 'Marc', 'Marry', 'Junior', 'Doe', 'Sara']
lists_numbers = [ 4, 7, 7, 8 , 8 ,1 ,2 ,3]
get_first_element_at_the_list = users[0]
get_last_element_at_the_list = users[-1]

users[0] = 'William'
sub_users = users[2: 5]
users.append('January')
users.insert(3, 'Monday')

users.pop(4)

del users[2]

users.remove('Doe')
is_user_exist = 'Sara' in users



get_position_user = users.index('Sara')

count_element = users.count('Sara')

extend_list = users + ['max', 'man']

list_filter = sorted(lists_numbers)
lists_filter_reversed = sorted(lists_numbers, reverse=True)
only_reversed = list(reversed(lists_numbers))
copy_list_from_original = users.copy()

# clear the list

users.clear()

