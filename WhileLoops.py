# this import will be used in the if block to exit the program
import sys
# never use this code in a final application, this is only to show while loops
# we are going to create a password checker

# the next variable is uppercase because it is a constant
MASTER_PASSWORD = 'ciaone'
# ask the user to input a password
password = input('Please eneter the password: ')
attempts = 2
# check if the passoword right, if not ask again
# give only 3 attempts
while password != MASTER_PASSWORD:
    if attempts > 0:
        password = input('Invalid password, try again: ')
        attempts -= 1
    else:
        sys.exit('Too many invalid password attempts')
print('Your password was correct! Welcome!')
