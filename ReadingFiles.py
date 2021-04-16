# To open a file you need to call the 'open' function, that return a 'file handle'
# the file handle is a variable used to perform operations on the file
file_handle = open('ForLoop.py')
# this will print the details of the file, not what is in the file itself
print(file_handle)

# we can use the for loop to print the lines in the file
print('\nWhat is in the file?\n')
for line in file_handle:
    print(line.rstrip())

# count the number of lines in the file
number_of_lines = 0
file_handle = open('ForLoop.py')
for line in file_handle:
    number_of_lines += 1
print('\nHow many lines there are in the file? {}\n'.format(number_of_lines))

# read the whole file into a single string
file_handle = open('ForLoop.py')
single_string = file_handle.read()
print('\nHow many characters are in the file? {}'.format(len(single_string)))
print('\nPrint the file as a single string\n')
print(single_string)
