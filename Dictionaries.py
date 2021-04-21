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

# you can create lists from dictionaries. you can use keys or values
names = list(languages)
print(names)
# another way
names_1 = languages.keys()
print(names_1)

values = languages.values()
print(values)

# you can also create a tuple from dictionaries
items = languages.items()
print(items)
