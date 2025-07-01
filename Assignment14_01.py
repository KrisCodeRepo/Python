class PartyAnimal:
    def __init__(self):
        self.x = 0
        print('I am a constructor')
    def party(self):
        self.x  = self.x+1
        print('So far', self.x)
        y = list
        #print(dir(y))
    def __del__(self):
        print('I am destructed', self.x)
an = PartyAnimal()

an.party()
an.party()
an =42
print('an contains', an)

print('Type', type(an))
print('Dir', dir(an))
#print('Type', type(an.x))
#print('Type', type(an.party))