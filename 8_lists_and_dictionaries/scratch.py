# Lists and Dictionaries

last_alpha_lst = ['x', 'y', 'z']
print(last_alpha_lst)
print(last_alpha_lst[0])
print(last_alpha_lst[1])
print(last_alpha_lst[2])

ltr_lst = list('abc')
print(ltr_lst)
print(ltr_lst[0])
print(ltr_lst[1])
print(ltr_lst[2])

my_list = ['h', 'e', 'l', 'l', 'o']
print(my_list)
my_list[len(my_list):] = [' ', 'w', 'o', 'r', 'l', 'd', '.']
print(my_list)
my_list[11] = '!'
print(my_list)
del my_list[5]
print(my_list)

# my_teams = ['Raptors', 'Heat', 'Nets']
# your_teams = my_teams  # Create a shared reference to same list
# my_teams[1] = 'Lakers'  # Modify list element

# print('My teams are:', my_teams)  # Both variables have changed
# print('Your teams are:', your_teams)  # Both variables have changed

my_teams = ['Raptors', 'Heat', 'Nets']
your_teams = my_teams[:]  # Assign your_teams with a COPY of my_teams
my_teams[1] = 'Lakers'  # Modify list element
print('My teams are:', my_teams)  # List element has changed
print('Your teams are:', your_teams)  # List element has not changed
