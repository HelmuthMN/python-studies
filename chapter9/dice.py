from random import randint

class Die:
    def __init__(self, sides = 20):
        self.sides = sides
    
    def rool_die(self):
        print(randint(1,self.sides))


die = Die()
die.rool_die()
die.rool_die()
die.rool_die()
die.rool_die()
die.rool_die()
die.rool_die()
die.rool_die()
die.rool_die()
die.rool_die()
die.rool_die()
