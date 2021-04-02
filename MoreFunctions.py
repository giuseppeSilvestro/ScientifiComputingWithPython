# import math module to use in split_check function
import math

# define a function with one paramenter
def yell(text):
    # make praise uppercase
    text = text.upper()
    # check how many characters are in praise and store it in a new variable
    number_of_characters = len(text)
    # create a new string
    result = text + '!' * (number_of_characters //4)
    print(result)

# call the function
yell('You are doing great')
yell("Don't forget to ask for help")
yell("Don't repeat yourself. Keep things dry")

# create a function that returns a value
# this function will take the bill and split it between the number of people
def split_check(total, number_of_people):
    # use math.ceil to round up to the next integer
    cost_per_person = math.ceil(total / number_of_people)
    return cost_per_person

amount_due = split_check(84.97, 4)
print('Each person owes ${}'.format(amount_due))

total_due = float(input('What is the total? '))
number_of_people = int(input('How many people? '))
amount_due2 = split_check(total_due, number_of_people)
print('Each person owes ${}'.format(amount_due2))
