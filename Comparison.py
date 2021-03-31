# check if values are equal
first_name = 'Giuseppe'
your_name = input('Please input your name: ')
print('Is Giuseppe your name?', your_name == first_name)

# Check if values are not equal
if your_name != 'Giuseppe':
    print('Your name is not Giuseppe')

# Check if one value is greater or smaller than the other
print('Is 3 smaller than 6?', 3 < 6)
print('Is 6 greater than 3?', 6 > 3)

# When you check if a string is greater than another, Python perform an
# alphabetical comparison of the first letter
print('Is Giuseppe greater than Lisa?', 'Giuseppe' > 'Lisa')
