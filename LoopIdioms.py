# Loop Idioms are Patterns that have to do with how we construct loops

# Looping through a Set to find the Largest Number
largest_number = -1

for i in [1,5,16,25,2,3,41,8]:
    if i > largest_number:
        largest_number = i

print('The largest number in ouse set is {}'.format(largest_number))

# Counting in a loop
count = 0
for i in [9,52,4,6,8,12,3]:
    count += 1
print('There are {} items in our set'.format(count))

# Summing in a loop
total = 0
for i in [1,2,3,4,5]:
    total += i
print('The sum of the number in our set is {}'.format(total))

# Finding the average in a loop
sum = 0
count = 0
for i in [1,2,3,4,5]:
    count += 1
    sum += i
print('The average in our set is', sum / count)

# Filtering in a Loop
for i in [1,2,52,65,45,23,16,85,13]:
    if i > 20:
        print('The number {} is larger than 20'.format(i))

# Searching using a boolean variable
found = False
for i in [1,5,6,8,10,3,55,64,123,7]:
    if i == 10:
        found = True
        break
print('Is there a 10 in our set? {}'.format(found))

# Finding the smallest Number
# We can use the same technique for finding the largest number
# 'is' is strongest than '==' but try not to use is everywhere
smallest = None
for i in [2,5,46,35,85,12,46,1]:
    if smallest is None:
        smallest = i
    elif i < smallest:
        smallest = i
print('The smallest number in our set is {}'.format(smallest))
