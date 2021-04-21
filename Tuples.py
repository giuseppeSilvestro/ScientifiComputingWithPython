# For Tuples we use parentheses instead of square brackets as we do with lists
x = (1, 2, 3)
print(x)

# Tuples are immutable, so the next line of code will give you an error
# x[2] = 4

# Because they are immutable you cannot perform a lot of operations you can do with lists
# x.sort()
# x.append(5)
# x.reverse()

# The reason why we use tuples is that they are more efficient and require less memory

# You can use tuples for multiple assignement
(x, y) = ('Ciao', 9)
print(x)
print(y)

# We can use tuples to sort dictionaries
d = {'a':10, 'c':22, 'b':1}
print(d.items())
d_tuple = sorted(d.items())
print(d_tuple)

# Print the top ten most common words
handle = open('String.py')
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

common_words = list()
for k, v in counts.items():
    new_tuple = (v, k)
    common_words.append(new_tuple)

common_words = sorted(common_words, reverse=True)

for v, k in common_words[:10]:
    print(k, v)
