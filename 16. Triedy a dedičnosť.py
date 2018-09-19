"""
#------------------------------------------------------------------------------
# 16.2 DEDICNOST
# http://input.sk/python2016/16.html#dedicnost
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


print("------------ 16.2.2 ------------")
print('===== GRAFICKE OBJEKTY =====')

from tkinter import *

class Kruh:
    canvas = None
    typ = 'kruh'

    def __init__(self, x, y, r, farba='red'):
        self.x, self.y, self.r = x, y, r
        self.farba = farba
        self.id = canvas.create_oval(self.x+self.r, self.y+self.r,
                                     self.x-self.r, self.y-self.r,
                                     fill = self.farba)
    def __str__(self):
        return 'Kruh({},{},{},{},{})' \
            .format(self.x+self.r, self.y+self.r,self.x-self.r, self.y-self.r,repr(self.farba))

    def posun(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
        self.canvas.move(self.id, dx, dy)

    def zmen(self, r):
        self.r = r
        self.canvas.coords(self.id,
                           self.x + self.r, self.y + self.r,
                           self.x - self.r, self.y - self.r)

    def prefarbi(self, farba):
        self.farba = farba
        self.canvas.itemconfig(self.id, fill=self.farba)

class Obdlznik:
    canvas = None
    typ = 'obdlznik'

    def __init__(self, x, y, sirka, vyska, farba='red'):
        self.x, self.y, self.sirka, self.vyska = x, y, sirka, vyska
        self.farba = farba
        self.id = canvas.create_rectangle(self.x, self.y,
                                          self.x+sirka, self.y+vyska,
                                          fill=self.farba)

    def __str__(self):
        return 'Obdlznik({},{},{},{},{})' .format(self.x, self.y, self.sirka, self.vyska, self.farba)


    def posun(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
        self.canvas.move(self.id, dx, dy)

    def zmen(self, sirka, vyska):
        self.r = r
        self.canvas.coords(self.id,
                           self.x, self.y,
                           self.x+sirka, self.y+vyska)

    def prefarbi(self, farba):
        self.farba = farba
        self.canvas.itemconfig(self.id, fill=self.farba)

class Skupina:
    def __init__(self):
        self.pole = []

    def pridaj(self, utvar):
        self.pole.append(utvar)
        print('Pridal som do pola')

    def prefarbi(self, farba):
        for utvar in self.pole:
            utvar.prefarbi(farba)

    def posun(self, dx, dy):
        for utvar in self.pole:
            utvar.posun(dx, dy)

    def prefarbi_typ(self, typ, farba):
        for utvar in self.pole:
            if utvar.typ == typ:
                utvar.prefarbi(farba)

    def posun_typ(self, typ, dx, dy):
        for utvar in self.pole:
            if utvar.typ == typ:
                utvar.posun(dx, dy)

    def citaj(self, skupina):
        return 'Obsah skupiny: ({})' .format(', '.join(self.pole))

# ---------------------------------------------------- >
root = Tk()
root.configure(bg = 'white')
root.title('16.2.2 GRAFICKE OBJEKTY')
canvas = Canvas(root, bg = 'white', width = '600', height ='600')
c = Kruh.canvas = Obdlznik.canvas = canvas
c.pack()

skupina_utvarov = Skupina()
k = Kruh(50, 50, 30, 'blue')
r = Obdlznik(100, 20, 100, 50)

skupina_utvarov.pridaj(k)
skupina_utvarov.pridaj(r)
print(skupina_utvarov.citaj())

k.prefarbi('green')
r.posun(50)

root.mainloop()


# ---------------------------------------------------------------------------------------
# DEDENIE Z NDRADENEJ TRIEDY UTVAR

from tkinter import *

class Utvar:
    canvas = None

    def __init__(self, x, y, farba='red' ):
        self.x, self.y = x, y
        self.farba = farba
        self.id = None

    def posun(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
        self.canvas.move(self.id, dx, dy)

    def prefarbi(self, farba):
        self.farba = farba
        self.canvas.itemconfig(self.id, fill=self.farba)

class Kruh(Utvar):
    canvas = None

    def __init__(self, x, y, r, farba='red'):
        super().__init__(x, y, farba)
        self.r = r
        self.id = canvas.create_oval(self.x+self.r, self.y+self.r,
                                     self.x-self.r, self.y-self.r,
                                     fill = self.farba)
    def __str__(self):
        return 'Kruh({},{},{},{},{})' .format(self.x+self.r, self.y+self.r,
                                              self.x-self.r, self.y-self.r,
                                              repr(self.farba))

    def zmen(self, r):
        self.r = r
        self.canvas.coords(self.id,
                           self.x + self.r, self.y + self.r,
                           self.x - self.r, self.y - self.r)

class Obdlznik(Utvar):
    canvas = None

    def __init__(self, x, y, sirka, vyska, farba='red'):
        super().__init__(x, y, farba)
        self.sirka, self.vyska = sirka, vyska
        self.id = canvas.create_rectangle(self.x, self.y,
                                          self.x+sirka, self.y+vyska,
                                          fill=self.farba)

    def __str__(self):
        return 'Obdlznik({},{},{},{},{})' .format(self.x, self.y, self.sirka, self.vyska, self.farba)


    def zmen(self, sirka, vyska):
        self.r = r
        self.canvas.coords(self.id,
                           self.x, self.y,
                           self.x+sirka, self.y+vyska)

class Skupina:
    def __init__(self):
        self.pole = []

    def pridaj(self, utvar):
        self.pole.append(utvar)
        print('Pridal som do pola utvar - ', utvar.__str__())

    def prefarbi(self, farba):
        for utvar in self.pole:
            utvar.prefarbi(farba)

    def posun(self, dx, dy):
        for utvar in self.pole:
            utvar.posun(dx, dy)

    def prefarbi_typ(self, typ, farba):
        for utvar in self.pole:
            if isinstance(utvar, typ):
                utvar.prefarbi(farba)

    def posun_typ(self, typ, dx, dy):
        for utvar in self.pole:
            if isinstance(utvar, typ):
                utvar.posun(dx, dy)

    def citaj(self):
        skup_utvary = []
        for utvar in self.pole:
            skup_utvary.append(utvar.__str__())
        return skup_utvary

    # return 'Obsah skupiny: ({})' .format(', '.join(self.pole))


# ---------------------------------------------------- >
root = Tk()
root.configure(bg = 'white')
root.title('16.2.2 GRAFICKE OBJEKTY')
canvas = Canvas(root, bg = 'white', width = '600', height ='600')
c = Kruh.canvas = Obdlznik.canvas = canvas
c.pack()

skupina_utvarov = Skupina()
t1 = Kruh(50, 50, 30)
t2 = Obdlznik(100, 20, 100, 50)

# isinstance(i, t), ktorá zistí, či je inštancia i typu t alebo je typom niektorého jeho predka
print(isinstance(t1, Utvar))        # True
print(isinstance(t1, Kruh))         # True
print(isinstance(t1, Obdlznik))     # False
print(isinstance(t2, Obdlznik))     # True
# print(type(t1))     # <class '__main__.Kruh'>
# print(type(t2))     # <class '__main__.Obdlznik'>

t1.prefarbi('green')
t2.posun(50)

skupina_utvarov.pridaj(t1)
skupina_utvarov.pridaj(t2)
print('Obsah skupiny: [{}]' .format(', '.join(skupina_utvarov.citaj())))

skupina_utvarov.prefarbi_typ(Kruh, 'black')
skupina_utvarov.posun_typ(Obdlznik, -10, -25)

root.mainloop()



# 16.2.3 Testovanie typu inštancie
print("------------------------------ 16.2.3 -------------------------------------")
print('===== Testovanie typu inštancie =====')

from tkinter import *


class Utvar:
    canvas = None

    def __init__(self, x, y, farba='red' ):
        self.x, self.y = x, y
        self.farba = farba
        self.id = None

    def posun(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
        self.canvas.move(self.id, dx, dy)

    def prefarbi(self, farba):
        self.farba = farba
        self.canvas.itemconfig(self.id, fill=self.farba)

class Kruh(Utvar):
    canvas = None

    def __init__(self, x, y, r, farba='red'):
        super().__init__(x, y, farba)
        self.r = r
        self.id = canvas.create_oval(self.x+self.r, self.y+self.r,
                                     self.x-self.r, self.y-self.r,
                                     fill = self.farba)
    def __str__(self):
        return 'Kruh({},{},{},{},{})' .format(self.x+self.r, self.y+self.r,
                                              self.x-self.r, self.y-self.r,
                                              repr(self.farba))

    def zmen(self, r):
        self.r = r
        self.canvas.coords(self.id,
                           self.x + self.r, self.y + self.r,
                           self.x - self.r, self.y - self.r)

class Obdlznik(Utvar):
    canvas = None

    def __init__(self, x, y, sirka, vyska, farba='red'):
        super().__init__(x, y, farba)
        self.sirka, self.vyska = sirka, vyska
        self.id = canvas.create_rectangle(self.x, self.y,
                                          self.x+sirka, self.y+vyska,
                                          fill=self.farba)

    def __str__(self):
        return 'Obdlznik({},{},{},{},{})' .format(self.x, self.y, self.sirka, self.vyska, self.farba)


    def zmen(self, sirka, vyska):
        self.r = r
        self.canvas.coords(self.id,
                           self.x, self.y,
                           self.x+sirka, self.y+vyska)

class Skupina:
    def __init__(self):
        self.pole = []

    def pridaj(self, utvar):
        self.pole.append(utvar)
        print('Pridal som do pola utvar - ', utvar.__str__())

    def prefarbi(self, farba):
        for utvar in self.pole:
            utvar.prefarbi(farba)

    def posun(self, dx, dy):
        for utvar in self.pole:
            utvar.posun(dx, dy)

    def prefarbi_typ(self, typ, farba):
        for utvar in self.pole:
            if isinstance(utvar, typ):
                utvar.prefarbi(farba)

    def posun_typ(self, typ, dx, dy):
        for utvar in self.pole:
            if isinstance(utvar, typ):
                utvar.posun(dx, dy)

    def citaj(self):
        skup_utvary = []
        for utvar in self.pole:
            skup_utvary.append(utvar.__str__())
        return skup_utvary

    # return 'Obsah skupiny: ({})' .format(', '.join(self.pole))


# ---------------------------------------------------- >
root = Tk()
root.configure(bg = 'white')
root.title('16.2.2 GRAFICKE OBJEKTY')
canvas = Canvas(root, bg = 'white', width = '600', height ='600')
c = Kruh.canvas = Obdlznik.canvas = canvas
c.pack()

skupina_utvarov = Skupina()
t1 = Kruh(50, 50, 30)
t2 = Obdlznik(100, 20, 100, 50)

# isinstance(i, t), ktorá zistí, či je inštancia i typu t alebo je typom niektorého jeho predka
print(isinstance(t1, Utvar))        # True
print(isinstance(t1, Kruh))         # True
print(isinstance(t1, Obdlznik))     # False
print(isinstance(t2, Obdlznik))     # True
# print(type(t1))     # <class '__main__.Kruh'>
# print(type(t2))     # <class '__main__.Obdlznik'>

t1.prefarbi('green')
t2.posun(50)

skupina_utvarov.pridaj(t1)
skupina_utvarov.pridaj(t2)
print('Obsah skupiny: [{}]' .format(', '.join(skupina_utvarov.citaj())))

skupina_utvarov.prefarbi_typ(Kruh, 'black')
skupina_utvarov.posun_typ(Obdlznik, -10, -25)


root.mainloop()


# 16.2.3 Odvodená trieda od Turtle
print("------------------------------ 16.2.3 -------------------------------------")
print('===== Odvodená trieda od Turtle =====')

import turtle

class MojaTurtle(turtle.Turtle):
    def stvorec(self, velikost):
        for i in range(4):
            self.fd(velikost)
            self.rt(90)

t = MojaTurtle()
t.stvorec(100)
t.lt(30)
t.stvorec(200)


# Môžeme definovať aj zložitejšie metódy, napr. aj rekurzívny strom:

import turtle

class MojaTurtle(turtle.Turtle):
    def strom(self, n, d):
        self.fd(d)
        if n > 0:
            self.lt(40)
            self.strom(n - 1, d * 0.6)
            self.rt(90)
            self.strom(n  -1, d * 0.7)
            self.lt(50)
        self.bk(d)

t = MojaTurtle()
t.lt(90)
t.strom(5, 100)



# Niekedy nám môže chýbať to, že trieda Turtle neumožňuje vytvoriť korytnačku inde ako v strede plochy.
# Predefinujme inicializáciu našej novej korytnačky a zároveň sme tu zadefinujme metódu domcek(),
# ktorá nakreslí domček zadanej veľkosti:
import turtle

class MojaTurtle(turtle.Turtle):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.speed(0)
        self.pu()
        self.setpos(x, y)
        self.pd()

    def domcek(self, dlzka):
        self.speed(5)
        for uhol in 90, 90, 90, 30, 120, -60:
            self.fd(dlzka)
            self.rt(uhol)

t = MojaTurtle(-100, 100)
t.domcek(100)

# Vytvorme dve odvodené triedy od triedy MojaTurtle, v ktorých pozmeníme kreslenie rovnej čiary.
# Trieda MojaTurtle1 prepíše korytnačiu metódu fd() tak, že namiesto rovnej čiary danej dĺžky,
# nakreslí cikcakovú čiaru, pričom skončí presne v tom mieste, kde by skončila aj pôvodná rovná čiara:


class MojaTurtle1(MojaTurtle):
    def fd(self, dlzka):
        while dlzka >= 5:
            self.lt(60)
            super().fd(5)
            self.rt(120)
            super().fd(5)
            self.lt(60)
            dlzka -= 5
        super().fd(dlzka)

MojaTurtle1().domcek(100)


# Trieda MojaTurtle2 namiesto jednej rovnej čiary danej dĺžky, nakreslí tri čiary tejto dĺžky,
# pričom sa zakaždým otočí o 180 stupňov plus nejaká malá náhodná odchýlka <-3, 3> stupne.
# Vďaka tejto odchýlke môže vzniknúť efekt, že kresba domčeka vznikla kreslením od ruky:
from random import randint as ri

class MojaTurtle2(MojaTurtle):
    def fd(self, dlzka):
        super().fd(dlzka)
        self.rt(180 - ri(-3, 3))
        super().fd(dlzka)
        self.rt(180 - ri(-3, 3))
        super().fd(dlzka)

MojaTurtle2().domcek(100)


# =============================================
# CVICENIA
# =============================================
# 2.  Zadefinujte triedu Ucet s metódami:
# ---------------------------------------------
#    - __init__(meno, suma) - meno účtu a počiatočná suma, napr. Ucet('mbank', 100) alebo Ucet('jbanka')
#
#    - __str__() - reťazec v tvare 'ucet mbank -> 100 euro' alebo ucet jbanka -> 0 euro
#
#    - stav() - vráti momentálny stav účtu
#
#    - vklad(suma) - danú sumu pripočíta k účtu
#
#    - vyber(suma) - vyberie sumu z účtu (len ak je to kladné číslo), vráti vybranú sumu, ak je na účte
#      menej ako požadovaná suma, vyberie len toľko koľko sa dá
#
#    - otestujte napr.

# mbank = Ucet('mbank')
# csob = Ucet('csob', 100)
# tatra = Ucet('tatra', 17)
# sporo = Ucet('sporo', 50)
# mbank.vklad(sporo.vyber(30) + tatra.vyber(30))
# csob.vyber(-5)
# spolu = 0
# for ucet in mbank, csob, tatra, sporo:
#     print(ucet)
#     spolu += ucet.stav()
# print('spolu = ', spolu)

# Vypise:
# ucet mbank -> 47 euro
# ucet csob -> 100 euro
# ucet tatra -> 0 euro
# ucet sporo -> 20 euro
# spolu =  167

class Ucet:
    def __init__(self, meno, suma = 0):
        self.meno = meno
        self.suma = suma

    def __str__(self):
        return 'Ucet {} -> {} euro'.format(self.meno, self.suma)

    def stav(self):
        return self.suma

    def vklad(self, suma):
        self.suma += suma

    def vyber(self, suma):
        self.vyberam = 0
        if self.suma > 0:
            if self.suma < suma:
                self.vyberam = self.suma
                self.suma = 0
            elif suma < 0:
                self.vyberam = 0
            else:
                self.vyberam = suma
                self.suma = self.suma - suma
        else:
            print('Na ucte je zostatok ... ', self.suma, ', Vyber nie je mozny!')
            self.vyberam = 0

        return self.vyberam

mbank = Ucet('mbank')
csob = Ucet('csob', 100)
tatra = Ucet('tatra', 17)
sporo = Ucet('sporo', 50)

print(mbank)                             # Ucet mbank -> 0 euro
print(sporo)                             # Ucet sporo -> 50 euro
print(tatra)                             # Ucet tatra -> 17 euro

mbank.vklad(sporo.vyber(30) + tatra.vyber(30))
print(mbank)                             # Ucet mbank -> 47 euro
print(sporo)                             # Ucet sporo -> 20 euro
print(tatra)                             # Ucet tatra -> 0 euro
csob.vyber(-5)
print(csob)

spolu = 0
for ucet in mbank, csob, tatra, sporo:
    print(ucet)
    spolu += ucet.stav()
print('spolu = ', spolu)                 # spolu =  167



# 3. Zadefinujte triedu UcetHeslo, ktorá je odvodená z triedy Ucet a má takto zmenené správanie:
## ---------------------------------------------
#   -  __init__(meno, heslo, suma) - k účtu si zapamätá aj heslo
#   -  vklad(suma) - si najprv vypýta heslo a až keď je správne, zrealizuje vklad
#   -  vyber(suma) - si najprv vypýta heslo a až keď je správne, zrealizuje výber,
#      inak vráti None
#   -  pri definovaní týchto metód volajte ich pôvodné verzie z triedy Ucet
#   -  otestujte napr.


class Ucet:
    def __init__(self, meno, suma = 0):
        self.meno = meno
        self.suma = suma

    def __str__(self):
        return 'Ucet {} -> {} euro'.format(self.meno, self.suma)

    def stav(self):
        return self.suma

    def vklad(self, suma):
        self.suma += suma

    def vyber(self, suma):
        self.vyberam = 0
        if self.suma > 0:
            if self.suma < suma:
                self.vyberam = self.suma
                self.suma = 0
            elif suma < 0:
                self.vyberam = 0
            else:
                self.vyberam = suma
                self.suma = self.suma - suma
        else:
            print('Na ucte je zostatok ... ', self.suma, ', Vyber nie je mozny!')
            self.vyberam = 0

        return self.vyberam



class UcetHeslo(Ucet):
    def __init__(self, meno, heslo, suma=0):
        super().__init__(meno, suma)
        self.heslo = heslo

    def stav(self):
        self.ucet_pass = input('Zadaj heslo k uctu: ')

        if self.ucet_pass != self.heslo:
            print('Nespravne meno heslo!')
            return None
        else:
            return Ucet.stav(self)

    def vklad(self, suma):
        self.ucet_pass = input('Pre vklad zadaj heslo k uctu: ')
        if self.ucet_pass != self.heslo:
            print('Nespravne meno heslo!')
            return None
        else:
            Ucet.vklad(self,suma)

    def vyber(self, suma):
        self.ucet_pass = input('Pre vyber zadaj heslo k uctu: ')
        if self.ucet_pass != self.heslo:
            print('Nespravne meno heslo!')
            return None
        else:
            return Ucet.vyber(self,suma)

# ------------------------------------------------------------

mbank = UcetHeslo('mbank', 'gigi')
csob = Ucet('csob', 100)
tatra = UcetHeslo('tatra', 'gogo', 17)
sporo = Ucet('sporo', 50)

#print(dir(mbank))
print(mbank.stav())
mbank.vklad(20)
print(mbank.stav())
mbank.vyber(20)
print(mbank.stav())