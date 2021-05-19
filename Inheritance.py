class PartyAnimal:
    x = 0
    name = ''

    def __init__(self, name):
        self.name = name
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)

# this class is a child class of PartyAnimal that has the same methods of the parent
# class but also a specific method (touchdown) of its own
class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, 'points', self.points)

s = PartyAnimal('Sally')
s.party()

j = FootballFan('Jim')
j.party()
j.touchdown()
