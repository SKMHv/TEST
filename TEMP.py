# =============================================
# CVICENIA
# =============================================
# 4. Zadefinujte dve triedy Turtle1 a Turtle2, obidve odvodené od Turtle,
#    pričom obe majú zadefinovanú metódu otoc()
#
#
#    - metóda otoc(uhol) v triede Turtle1 otočí korytnačku o zadaný uhol vľavo,
#      v triede Turtle2 ju otočí vpravo
#
#     from turtle import Turtle
#     from random import randrange as rr
#
#     class Turtle1(Turtle):
#         ...
#
#     class Turtle2(Turtle):
#
# - teraz naprogramujte takýto test týchto dvoch tried:
#
#     na x-ovej osi rozložte 20 korytnačiek s rozostupmi 20 krokov, všetky budú otočené na východ -
#     náhodným generátorom rozhodnite, ktorá z nich bude Turtle1 a ktorá Turtle2 - korytnačky uložte do poľa
#     teraz postupne prejdete všetky korytnačky z tohto poľa a zmeníte im farbu pera na červenú (pre Turtle1)
#     alebo na modrú (pre Turtle2)
#     na záver štyrikrát zopakujete: každá korytnačka prejde 20 krokov a otočí sa pomocou otoc() o 90 stupňov


import turtle
from random import randint as ri


class Turtle1(turtle.Turtle):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.speed(0)
        self.pu()
        self.setpos(x, y)
        self.pd()
    def otoc(self, uhol):
        self.lt(uhol)

class Turtle2(turtle.Turtle):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.speed(0)
        self.pu()
        self.setpos(x, y)
        self.pd()
    def otoc(self, uhol):
        self.rt(uhol)

pocet = 20
pole = []
for i in range(pocet):
    if ri(0,1):
        pole.append(Turtle1((-200)+20*i,0))
    else:
        pole.append(Turtle2((-200)+20*i,0))

for koryt in pole:
    if isinstance(koryt, Turtle1):
        koryt.color('red')
    else:
        koryt.color('blue')








