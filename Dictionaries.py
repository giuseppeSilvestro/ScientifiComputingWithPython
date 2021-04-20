# Dictionaries have no order but each element has its own label
# create a dictionary and populate it with items
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse['candy'])

# you can also create a dictionary in this way
languages = {'Gennaro' : 2, 'Giuseppe' : 3, 'Giovanni' : 5}
print(languages)

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
