# import math module to use in split_check function
import math

# this function will take the bill and split it between the number of people
def split_check(total, number_of_people):
# check the number of people input by the user. if it is less or equal to 1
# raise a ValueError exception
    if number_of_people <= 1:
        raise ValueError('More than 1 person is required to split the check')
    # use math.ceil to round up to the next integer
    return math.ceil(total / number_of_people)

try:
    total_due = float(input('What is the total? '))
    number_of_people = int(input('How many people? '))
# if the line that calls the function is in the try block, the error raise by the
# if statement at line 8 will be cought by the except block and will not cause
# the program to crash
    amount_due = split_check(total_due, number_of_people)
# 'as err' will give us the chance to print the message contained in the raise line
except ValueError as err:
    print('This is not a valid value.')
    print('({})'.format(err))
else:
    print('Each person owes ${}'.format(amount_due))
