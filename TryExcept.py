astr = 'Hello Bob'
try:
    instr = int(astr)
except :
    instr = -1

print('First', instr)

astr = '123'
try:
    instr = int(astr)
except :
    instr = -1

print('Second', instr)


rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print('You enter a number')
else:
    print('You did not enter a number')
