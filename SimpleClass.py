# Here is a simple example of Class and Object

class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

an = PartyAnimal()

an.party()
an.party()
an.party()

# check what type our variable is
print("Type", type(an))
# check what methods and attribute our variable class has
# the results with underscore are used by python and you can ignore them
print("Dir", dir(an))
