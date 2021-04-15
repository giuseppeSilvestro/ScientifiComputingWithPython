# Looking inside Strings
fruit = 'banana'
letter = fruit[3]
print('The fourth letter in banana is "{}"'.format(letter))

# How long a string is?
print('How many letters are in banana? {}'.format(len(fruit)))

# Looping Through Strings
index = 0
while index < len(fruit):
    print(fruit[index])
    index += 1

# Another way to do the same
# usually the for loop is more elegant
for i in fruit:
    print(i)

# Looping and Counting
count = 0
for letter in fruit:
    if letter == 'a':
        count += 1
print('How many "a" are in banana? {}'.format(count))

# Slicing Strings
s = 'Monthy Python'
print('Print the variable s starting at index 0 till index 3:', s[0:4])

# Using 'in' as a logical operator
print('Is "n" in banana? {}'.format('n' in fruit))

# Searching a Strings
print('Find me the index of the first "n" in banana: {}'.format(fruit.find('n')))
print('Find me the index of the first "c" in banana: {}'.format(fruit.find('c')))

# Search and Replace
greet = 'Hello Giuseppe'
print(greet.replace('Giuseppe', 'Genny'))
print(greet.replace('i','J'))

# Stripping whitespaces
sentence = '     Ciaone  Genny    '
print(sentence.lstrip())
print(sentence.rstrip())
print(sentence.strip())

# Parsing and extracting
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
print('Find and print the host in the variable "data"')
at_position = data.find('@')
space_after_at = data.find(' ', at_position)
host = data[at_position + 1 : space_after_at]
print(host)
