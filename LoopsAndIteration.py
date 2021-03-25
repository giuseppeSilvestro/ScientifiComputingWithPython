n = 5
while n > 0:
    print(n)
    n = n-1
print('Blastoff!')
print(n)

print()
print('Run till input "done"')
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

#continue get you back to the beginning of the loop
print()
print('Input "#" to not print the input')
print('Run till input "done"')
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
