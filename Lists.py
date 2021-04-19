# an example of a list
friends = ['Giuseppe', 'Gennaro', 'Giovanni', 'Gustavo']
print(friends)

# A better way to print lists
for i in friends:
    print(i)

# how many elements are in the lists?
print('How many frieds do you have? {}'.format(len(friends)))

# add two lists together
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

# create an empty list and add elements to it
things = list()
things.append('coat')
things.append('computer')
things.append('shoes')
print(things)

# check if something is in the list
print('Do I have a computer? {}'.format('computer' in things))

# lists are in order and can be sorted
numbers = [2,6,8,5,4,1,7,3]
numbers.sort()
print(numbers)

# some built in functions
print('What is the lower number? {}'.format(min(numbers)))
print('What is the highest number? {}'.format(max(numbers)))
print('What is the sum of all the numbers? {}'.format(sum(numbers)))
print('What is the average? {}'.format(sum(numbers)/len(numbers)))

# Lists and strings
sentence = 'Are you ok?'
sentence_list = sentence.split()
print(sentence_list)

words = 'first;second;third'
words_list = words.split(';')
print(words_list)
