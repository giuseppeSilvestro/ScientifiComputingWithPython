# Combining strings together
first_string = "chocolate"
second_string = "marshmallow"
print(first_string + " " + second_string)
print(first_string, second_string)

# Strings are immutable. If I reassign the variable, the String will be deleted
# and replaced by the new Done

second_string = "flake"
print(first_string, second_string)

# Use operators to append more strings
new_string = first_string + ' ' + second_string
print(new_string)
new_string += '!'
print(new_string)
new_string += '!' * 20
print(new_string)

print('Some string methods\n\n')
quote = 'A person who never made a mistake never tried anything new'
print(quote)
print('How many characters are in the sentence?')
print(len(quote))
print('Print quote in upper case')
print(quote.upper())
print('Print each word in upper case')
print(quote.title())
#String formatting
#The {} are place holders
subject_template = 'Thanks for learning {} with us {}!'
print(subject_template.format('Python', 'Giuseppe'))
##Check if one string is contained in another strings
first_check = 'ham' in 'hamster'
print('Is the word "ham" contained in the word "hamster"?')
print(first_check)
