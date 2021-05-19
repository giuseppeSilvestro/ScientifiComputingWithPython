class PartyAnimal:
    x = 0

#this is a constructor
    def __init__(self):
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

# this is a destructor (destructors are seldom used)
    def __del__(self):
        print('I am destructed', self.x)

# here we create a new object of the PartyAnimal class
# the constructor is automatically called by Python when we create a new object
an = PartyAnimal()
an.party()
an.party()
# the next line will assign 'an' to a new variable, destroing the old Object
# Python will call the destructor on our behalf
an = 42
print('an contains', an)
