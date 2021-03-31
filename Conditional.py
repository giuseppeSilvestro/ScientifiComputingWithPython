# Check if the name inputted by the user is the your name
first_name = input('What is your first name? ')
print('Hello,', first_name)
if first_name == 'Giuseppe':
    print(first_name, 'is learning Python')
elif first_name == 'Gennaro':
    print('{} is learning Java'.format(first_name))
else:
    print("{} doesn't like software developing".format(first_name))


# Nested ifs
your_name = input('What is your name? ')
if your_name != 'Giuseppe':
    your_age = int(input('What is your age? '))
    if your_age >= 8:
        print('Hello {}! \nYou should learn Python!'.format(your_name))
    else:
        print('Hello {}! \nYou should learn Math first!'.format(your_name))
else:
    print('Hello {}!\nHow is your Python journey going?'.format(your_name))
