"""
#------------------------------------------------------------------------------
# 16.2 DEDICNOST

#------------------------------------------------------------------------------
"""
print("------------------------------ 16.2 -------------------------------------")

# ===== ZAKLADNA TRIEDA =====
class Bod:                                     # class Bod(object):
    """Inicializuje novy objekt bod so zadanymi atributmi x,y """
    def __init__(self,x,y):
        self.x, self.y = x, y

    def __str__(self):
        return 'Bod({},{})' .format(self.x, self.y)

    def posun(self,dx=0, dy=0):
        """Tato funnkcia priopocita parametre dx, xy k hodnotam atributov x, y bodu """
        self.x += dx
        self.y += dy

bod = Bod(100, 55)
print(bod)
bod.posun(50, 100)
print(bod)

print('Objektova trieda Bod - ', Bod.__doc__) # Objektova trieda Bod -  Inicializuje novy objekt bod so zadanymi atributmi x,y
print('posun - ',Bod.posun.__doc__)           # posun -  Tato funnkcia priopocita parametre dx, xy k hodnotam atributov x, y bodu

print("------------------------------ 16.2.1 -------------------------------------")
print('===== ODVODENA TRIEDA =====')
# ===== ODVODENA TRIEDA =====
class FarebnyBod(Bod):              # Odvodena trieda zo zakladnej triedy Bod (dedi jej atributy metody)
    def __init__(self, x, y, farba='black'):   # Zdedené metódy môžeme v novej triede nielen využívať, ale aj predefinovať - napr. môžeme zmeniť inicializáciu __init__():
        # Bod.__init__(self,x,y)    # inicializácia zo základnej triedy
        super().__init__(self,x,y)  # inicializácia zo základnej triedy funkciou super()
        # Štandardná funkcia super() na tomto mieste označuje: urob tu presne to, čo by na tomto mieste urobil môj rodič (t.j. moja super trieda).
        self.farba = farba

    def zmen_farbu(self, farba):
        self.farba=farba

fbod = FarebnyBod(100,100)
fbod.zmen_farbu('red')
fbod.posun(dy=50)
print(fbod)