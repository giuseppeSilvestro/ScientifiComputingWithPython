# one of the most common application of dictionaries is counting
counts = dict()
names = ['Gennaro', 'Giuseppe', 'Gennaro', 'Giovanni']
for name in names :
    if name not in counts :
        counts[name] = 1
    else :
        counts[name] += 1
print(counts)

# we can simplify this loop using 'get()'
counts_2 = dict()
for name in names :
    counts_2[name] = counts_2.get(name, 0) + 1
print(counts_2)

# Ask the user to input a line of text and count the words in it, finding the most common one
counts_3 = dict()
print('Enter a line of text:')
line = input('')
words = line.split()
print(words)

print('Counting...')
for word in words:
    counts_3[word] = counts_3.get(word, 0) + 1

print('Counts', counts_3)

# you can use two iteration variables!
for name, count in counts.items():
    print(name, count)

# open a file, count the words in it and print the most common one
name = input('Entere file: ')
handle = open(name)

counts_4 = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts_4[word] = counts_4.get(word, 0) + 1

big_count = None
big_word = None
for word, count in counts_4.items():
    if big_count is None or count > big_count:
        big_word = word
        big_count = count
print(big_word, big_count)
