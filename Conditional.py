# Check if the name inputted by the user is the your name
first_name = input('What is your first name? ')
print('Hello,', first_name)
if first_name == 'Giuseppe':
    print(first_name, 'is learning Python')
elif first_name == 'Gennaro':
    print('{} is learning Java'.format(first_name))
else:
    print("{} doesn't like software developing".format(first_name))
