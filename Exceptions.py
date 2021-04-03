# handle possible errors in the code that would block your program
# we use try/except/else

name = input('What is your name? ')
try:
    age = int(input('What is your age? '))
# valueError because if the user input something that cannot be converted to
# an int we will get a 'valueError'.
# the except block will run only if there is a ValueError in the code after 'try'
except ValueError:
    print('You did not input a valid value. Try again...')
# the else block will run if there is not exception
else:
    print('Hello {}! I am also {} years old!'.format(name, age))
