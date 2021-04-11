# Loop Idioms are Patterns that have to do with how we construct loops

# Looping through a Set to find the Largest Number
largest_number = -1

for i in [1,5,16,25,2,3,41,8]:
    if i > largest_number:
        largest_number = i

print(largest_number)
