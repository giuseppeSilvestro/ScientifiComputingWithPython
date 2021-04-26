# to be able to use Regular Expressions we have to import the package
import re

handle = open('DictionariesAndLoops.py')

# look for a line with the word 'print' in it and print it
for line in handle:
    line = line.rstrip()
    if line.find('print') >= 0:
        print(line)
# the next lines do the same thing but using regular expressions
handle = open('DictionariesAndLoops.py')
for line in handle:
    line = line.rstrip()
    if re.search('print', line):
        print(line)

# look for lines that starts with 'print'
handle = open('DictionariesAndLoops.py')

for line in handle:
    line = line.rstrip()
    if line.startswith('print'):
        print(line)

# do the same with regular Expressions
handle = open('DictionariesAndLoops.py')
for line in handle:
    line = line.rstrip()
    if re.search('^print', line):
        print(line)

# search() returns true or false.
# findall() returns something
x = 'My 2 favourite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)
y = re.findall('[aeiou]+', x)
print(y)
