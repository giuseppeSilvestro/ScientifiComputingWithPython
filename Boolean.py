# create a variable as boolean
has_taco = 'taco' in 'catacombs'
print('Is taco contained in catacombs?', has_taco)
# any number will return True apart from 0
print('Is 1 true or false?',bool(1))
print('Is 0 true or false?',bool(0))
print('Is 35 true or false?', bool(35))
# Any object that is not empty is True
print('Is a string true or false?', bool('ciaone'))
print('Is an empty string true or false?', bool(''))
# Chain booleans
print('Can booleans be chained with "and"?', bool(True and True))
print('Can booleans be chained with "or"?', bool(True or False))
print('This is goind to be complicated...', bool((False or False or True) and
(True and True)))
