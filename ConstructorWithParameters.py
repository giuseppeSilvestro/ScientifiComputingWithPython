class PartyAnimal:
    x = 0
    name = ''

# name in line 8 will be our parameter
# it would be better if 'name' in line 8 had another name, but i used the same as in
# line 3 to show that Python will treat them as different variables
    def __init__(self, name):
        self.name = name
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)

g = PartyAnimal('Giuseppe')
g.party()
