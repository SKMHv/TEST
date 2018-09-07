# ==================================
# 14. Triedy a metody
# http://python.input.sk/15.html
# ==================================

# ------------------------------
# Magická metóda __str__
# ------------------------------

# __init__() - nicializuje atribúty - automaticky sa vyvolá hneď po vytvorení (skonštruovaní) objektu

# __str__() - vrati reťazcovú reprezentáciu objektu. Vysledkom metody je znakovy etazec

class Cas():
    def __init__(self, hodiny, minuty):
        self.hodiny = hodiny
        self.minuty = minuty

    # def vypis(self):
    #     #return print('cas je ... {}:{}'.format(self.hodiny, self.minuty))
    #     print(f'cas je {self.hodiny}:{self.minuty:02}')
    #
    # def str(self):
    #     return f'{self.hodiny}:{self.minuty:02}'

    def __str__(self):
        return  f'{self.hodiny}:{self.minuty:02}'

    def vypis(self):
        print('cas je', self)



c = Cas(9, 17)
c.vypis()                           # cas je ... 9:17
print('teraz je', c.__str__())      # teraz je 9:17
print('teraz je', c)                # teraz je 9:17
c                                   # <__main__.Cas object at 0x03220F10>
print(c)                            # 9:17
print(str(c))                       # '9:17'
print(type(str(c)))                 # <class 'str'>
print(type(c))                      # <class '__main__.Cas'>

print('-----------------')
d = Cas(10, 5)
d.vypis()                           # cas je ... 10:5
Cas.vypis(d)                        # cas je ... 10:5
# print('teraz je',d.str())
print('-----------------')
print('\n')

# ------------------------------
# Volanie metódy z inej metódy
# ------------------------------

# Zatiaľ sme v našich jednoduchých príkladoch, v ktorých sme definovali nejaké triedy, nepotrebovali riešiť situácie,
# v ktorých v jednej metóde voláme nejakú inú metódu tej istej triedy. Doplňme do triedy Cas aj metódu pridaj():

# Pridajme teraz ďalšiu metódu kopia_a_pridaj(), ktorá vyrobí kópiu objektu a zároveň v tejto kópii posunie hodiny aj minúty:

class Cas():
    def __init__(self, hodiny, minuty):
        self.hodiny = hodiny
        self.minuty = minuty

    def __str__(self):
        return  f'{self.hodiny}:{self.minuty:02}'

    def vypis(self):
        print('cas je', self)

    def kopia(self):
        return Cas(self.hodiny,self.minuty)

    def pridaj(self,hodiny, minuty):
        self.hodiny += hodiny + (self.minuty + minuty) // 60
        self.minuty = (self.minuty + minuty) % 60

    def kopia_a_pridaj(self, hodiny, minuty):
        novy = self.kopia()                            # novy = Cas(self.hodiny, self.minuty)
        novy.pridaj(hodiny, minuty)
        return novy

c = Cas(9, 17)
c.vypis()                           # cas je ... 9:17
print('teraz je', c.__str__())      # teraz je 9:17
print('teraz je', c)                # teraz je 9:17
c                                   # <__main__.Cas object at 0x03220F10>
print(c)                            # 9:17
print(str(c))                       # '9:17'
print(type(str(c)))                 # <class 'str'>
print(type(c))                      # <class '__main__.Cas'>
print(c.kopia_a_pridaj(1,2))        # 10:19

print('\n')

# ---------
# priklady
# ---------


# Vylepšíme triedu Cas: bude mať 3 atribúty: hod, min, sek (pre hodiny, minúty, sekundy). Všetky metódy vytvoríme ako
# pravé funkcie, vďaka čomu sa bude táto trieda správať ako immutable (nemeniteľný typ):

class Cas():
    def __init__(self, hodiny = 0, minuty = 0, sekundy = 0):
        self.hod = hodiny
        self.min = minuty
        self.sek = sekundy

    def __str__(self):
        return  f'{self.hod}:{self.min:02}'

    def sucet(self, iny):
        """
        Metoda vrati sucet dvoch objektov typu Cas
        :param iny: druhy objekt cas
        :return: vrati sucet dvoch casov
        """
        return  Cas(self.hod + iny.hod, self.min + iny.min, self.sek + iny.sek)

    def vacsi(self, iny):
        """
        Metoda vrati true ak je objek cas volani pred metodou vacsi ako objekt cas v parametri metody

        :param iny: sruhy objekt cas
        :return: True / False
        """
        return (self.hod > iny.hod or
                self.hod == iny.hod and self.min > iny.min or
                self.hod == iny.hod and self.min == iny.min and self.sek > iny.sek)

cas_1 = Cas(9, 17)
cas_2 = Cas(8, 17)
print('cas_1 =', cas_1)                             # cas_1 = 9:17
print('cas_2 =', cas_2)                             # cas_2 = 8:17
print('cas_1.sucet(cas_2) =', cas_1.sucet(cas_2))   # cas_1.sucet(cas_2) = 17:34
print('cas_1.vacsi(cas_2) =', cas_1.vacsi(cas_2))   # cas_1.vacsi(cas_2) = True
print('cas_2.vacsi(cas_1) =', cas_2.vacsi(cas_1))   # cas_2.vacsi(cas_1) = False

print('\n')

# Vidíme, že metóda vacsi(), ktorá porovnáva dva časy, je dosť prekomplikovaná, lebo treba porovnávať tri atribúty v jednom aj druhom objekte.

# ---------------
# POMOCNA METODA
# ---------------


#
# Predchádzajúce riešenie má viac problémov:
#
#     pomocou metódy sucet() môžeme vytvoriť čas, v ktorej minúty alebo sekundy majú hodnotu väčšiu ako 59
#     dva časy sa porovnávajú dosť komplikovane
#
# Vytvorme pomocnú funkciu (teda metódu), ktorá z daného času vypočíta celkový počet sekúnd. Zároveň opravíme aj inicializáciu __init__():


class Cas():
    def __init__(self, hodiny = 0, minuty = 0, sekundy = 0):
        cas = abs(3600*hodiny + 60*minuty + sekundy)
        self.hod = cas // 3600
        self.min = cas // 60 % 60
        self.sek = cas % 60

    def __str__(self):
        return  f'{self.hod}:{self.min:02}:{self.sek:02}'

    def sucet(self, iny):
        """
        Metoda vrati sucet dvoch objektov typu Cas
        :param iny: druhy objekt cas
        :return: vrati sucet dvoch casov
        """
        return  Cas(self.hod + iny.hod, self.min + iny.min, self.sek + iny.sek)

    def pocet_sekund(self):
        """
        Prevedie Cas na sekundy
        :return: Cas v sekundach
        """
        return 3600 * self.hod + 60 * self.min + self.sek

    def rozdiel(self,iny):
        """
        Vypocita rozdiel sekund dvoch casov
        :param iny: druhy cas
        :return: rozdiel casov
        """
        return Cas(sekundy=self.pocet_sekund() - iny.pocet_sekund())

    def vacsi(self, iny):
        """
        Vol metodu pre prevod casov na sekundy a potom ich porovna.
        :param iny: druhy objekt cas
        :return: True / False
        """
        return self.pocet_sekund() > iny.pocet_sekund()

cas_1 = Cas(9, 17,15)
cas_2 = Cas(8, 17,40)
print('cas_1 =', cas_1)                                 # cas_1 = 9:17:15
print('cas_2 =', cas_2)                                 # cas_2 = 8:17:40
print('cas_1.sucet(cas_2) =', cas_1.sucet(cas_2))       # cas_1.sucet(cas_2) = 17:34:55
print('cas_1.vacsi(cas_2) =', cas_1.vacsi(cas_2))       # cas_1.vacsi(cas_2) = True
print('cas_2.vacsi(cas_1) =', cas_2.vacsi(cas_1))       # cas_2.vacsi(cas_1) = False
print('cas_1.rozdiel(cas_2) =', cas_1.rozdiel(cas_2))   # cas_1.rozdiel(cas_2) = 0:59:35

print('\n')

# Pomocnú funkciu pocet_sekund() sme využili nielen v porovnávaní dvoch časov (metóda vacsi()) ale aj v novej
# metóde rozdiel().
#
# Celá trieda sa dá ešte viac zjednodušiť, ak by samotný objekt nemal 3 atribúty hod, min a sek, ale len jeden
# atribút sek pre celkový počet sekúnd. Vďaka tomu by sme nemuseli pri každej operácii čas prepočítavať na
# sekundy: len pri výpise by sme museli sekundy previesť na hodiny a minúty. Napr.

class Cas():
    def __init__(self, hodiny = 0, minuty = 0, sekundy = 0):
        """
        Inicializuje novy cas v sekundach
        :param hodiny:
        :param minuty:
        :param sekundy:
        """
        self.sek = abs(3600*hodiny + 60*minuty + sekundy)


    def __str__(self):
        return f'{self.sek//3600}:{self.sek//60%60:02}:{self.sek%60:02}'

    def sucet(self, iny):
        """
        Metoda vrati sucet dvoch objektov typu Cas
        :param iny: druhy objekt cas
        :return: vrati sucet dvoch casov
        """
        return  Cas(sekundy = self.sek + iny.sek)

    def rozdiel(self,iny):
        """
        Vypocita rozdiel sekund dvoch casov
        :param iny: druhy cas
        :return: rozdiel casov
        """
        return Cas(sekundy=self.sek - iny.sek)

    def vacsi(self, iny):
        """
        Vol metodu pre prevod casov na sekundy a potom ich porovna.
        :param iny: druhy objekt cas
        :return: True / False
        """
        return self.sek > iny.sek


cas_1 = Cas(9, 17,15)
cas_2 = Cas(8, 17,40)
print('cas_1 =', cas_1)                                 # cas_1 = 9:17:15
print('cas_2 =', cas_2)                                 # cas_2 = 8:17:40
print('cas_1.sucet(cas_2) =', cas_1.sucet(cas_2))       # cas_1.sucet(cas_2) = 17:34:55
print('cas_1.vacsi(cas_2) =', cas_1.vacsi(cas_2))       # cas_1.vacsi(cas_2) = True
print('cas_2.vacsi(cas_1) =', cas_2.vacsi(cas_1))       # cas_2.vacsi(cas_1) = False
print('cas_1.rozdiel(cas_2) =', cas_1.rozdiel(cas_2))   # cas_1.rozdiel(cas_2) = 0:59:35


# Ak budeme teraz potrebovať vytvoriť zoznam časov, pričom prvý z nich je 8:10 a každý ďalší j
# e o 50 minút posunutý, môžeme to zapísať napr. takto:

zoznam = [Cas(8,10)]

# Zápis zoznam[-1].sucet(Cas(0, 50)) označuje, že k času, ktorý je momentálne posledným prvkom
# v zozname pripočítame 50 minút (teda čas, ktorý je 0 hodín a 50 minút). Ak by sme vedeli
# zabezpečiť sčitovanie časov rovnakým zápisom ako je napr. sčitovanie čísel alebo zreťazovanie
# reťazcov, tento zápis by vyzeral zoznam[-1] + Cas(0, 50), čo už vyzerá zaujímavo, ale žiaľ nefunguje.
for i in range(14):
    zoznam.append(zoznam[-1].sucet(Cas(0,50)))

# 8:10:00, 9:00:00, 9:50:00, 10:40:00, 11:30:00, 12:20:00, 13:10:00, 14:00:00, 14:50:00,
# 15:40:00, 16:30:00, 17:20:00, 18:10:00, 19:00:00, 19:50:00,
for cas in zoznam:
    print(cas, end=', ')

print('\n')

# ---------------
# Triedne a inštančné atribúty
# ---------------

# Už vieme, že
#
#   - triedy sú kontajnery na súkromné funkcie (metódy)
#   - inštancie sú kontajnery na súkromné premenné (atribúty)

class Test: pass
t = Test()
t.x = 100       # novy atribut v instancii
t.y = 200
# Lenže atribúty ako premenné môžeme definovať aj v triede, vtedy sú to tzv. triedne atribúty
# (atribúty na úrovni inštancií sú inštančné atribúty). Ak teda definujeme triedny atribút:
Test.z = 300

# tak tento atribút automaticky získavajú (vidia) aj všetky inštancie tejto triedy (tak ako všetky
# inštancie vidia všetky metódy triedy):
print(t.x, t.y, t.z)   # 100 200 300

# Aj novovytvorená inštancia získava (teda vidí) tento triedny atribút:
t2 = Test()
print(t2.z)         #300

# Kým do inštancie nepriradíme tento atribút, inštancia „vidí“ hodnotu triedy, keď už vyrobíme vlastný
# atribút, tak vidí túto hodnotu. Uvedomte si, že momentálne existuje triedny atribút Test.z a s
# rovnakým menom aj inštančný atribút t2.z. Inštancia t2 teraz po zapísaní t2.z vidí už len tento svoj
# súkromný atribút.

print('\n')

# Triedne atribúty môžeme vytvoriť už pri definovaní triedy, napr.
class Test:
    z = 300

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'test {self.x},{self.y},{self.z}'


t1 = Test(100,200)
print(t1)               # test 100,200,300

t2 = Test(10,20)
t2.z = 30
print(t2)               # test 10,20,30

Test.z = 9
print(t1)               # test 100,200,9

t1.x = 1000
t1.y = 2000
t1.z = 3000
print(t1)               # test 1000,2000,3000


# Ukážme si takéto využitie triedneho atribútu:

import random
from tkinter import *

class Bodka():
    def __init__(self,x, y):
        self.id = canvas.create_oval(x-5, y-5, x+5, y+5)
        #self.canvas = canvas

    def prefarbi(self):
        if random.randrange(2):
            farba = 'red'
        else:
            farba = 'blue'
        #self.canvas.itemconfig(self.id, fill=farba)
        canvas.itemconfig(self.id, fill=farba)

master = Tk()
canvas = Canvas(master)
canvas.pack()

bodky = []

for i in range(100):
    #bodky.append(Bodka(canvas, random.randint(10, 300), random.randint(10,250)))
    bodky.append(Bodka(random.randint(10, 300), random.randint(10,250)))
for b in bodky:
    b.prefarbi()


mainloop()

# Ak by sme teraz dostali úlohu na záver vypísať počet modrých a červených, zdá sa, že bez globálnej premennej to bude veľmi ťažké.
#
# Tu nám pomôžu triedne atribúty:
#
#     canvas nemusíme posielať zvlášť každému objektu (takto v každom objekte vzniká inštančný atribút canvas, pričom všetky objekty triedy Bodka majú rovnakú hodnotu tohto atribútu), môžeme vytvoriť jediný triedny atribút, ktorý budú vidieť všetky inštancie
#     pridáme ďalšie dva triedne atribúty pre počítanie počtu modrých a červených, pričom v metóde prefarbi() budeme tieto dve počítadla zvyšovať


import random
from tkinter import *

class Bodka():
    canvas = None
    pocet_modrych = pocet_cervenych = 0
    def __init__(self,canvas, x, y):
        self.id = canvas.create_oval(x-5, y-5, x+5, y+5)
        self.canvas = canvas

    def prefarbi(self):
        # print('random.randrange(3)', random.randrange(2))
        # print('random.randint(3)', random.randrange(2))
        if random.randrange(2):
            farba = 'red'
            Bodka.pocet_cervenych += 1

        else:
            farba = 'blue'
            Bodka.pocet_modrych += 1

        self.canvas.itemconfig(self.id, fill=farba)
        #canvas.itemconfig(self.id, fill=farba)

master = Tk()
canvas = Canvas(master)
canvas.pack()

bodky = []

for i in range(100):
    bodky.append(Bodka(canvas, random.randint(10, 300), random.randint(10,250)))
    #bodky.append(Bodka(random.randint(10, 300), random.randint(10,250)))
for b in bodky:
    b.prefarbi()

print('pocet_modrych =', Bodka.pocet_modrych)
print('pocet_cervenych =', Bodka.pocet_cervenych)

mainloop()

# ---------------------------
# príklad s grafickými objektmi
# ---------------------------




# Postupne zadefinujeme niekoľko tried, ktoré pomocou tkinter pracujú s rôznymi objektmi v grafickej ploche.

# -------------
#  objekt ktuh
# -------------


from tkinter import *

class Kruh():

    def __init__(self,x, y, r, farba='red'):
        self.canvas=canvas
        self.x = x
        self.y = y
        self.r = r
        self.farba = farba
        self.id = canvas.create_oval(
            self.x-self.r, self.y-self.r,
            self.x+self.r, self.y+self.r,
            fill = self.farba)

    # - canvas.move(id, dx, dy) - posúva ľubovoľný útvar
    # - canvas.itemconfig(id, nastavenie=hodnota, ...) - zmení ľubovoľné nastavenie (napr. farbu, hrúbku, …)
    # - canvas.coords(id, x1, y1, x2, y2, ...) - zmení súradnice útvaru

    def posun(self, dx=0, dy=0):
        self.x = dx
        self.y = dy
        self.canvas.move(self.id, dx,dy)

    def zvacsi(self,r):
        self.r = r
        self.canvas.coords(self.id,
            self.x-self.r, self.y-self.r,
            self.x+self.r, self.y+self.r)

    def premiestni(self, dx=0, dy=0):
        self.x = dx
        self.y = dy
        self.canvas.coords(self.id,
            self.x - self.r, self.y - self.r,
            self.x + self.r, self.y + self.r)

    def prefarbi(self,farba):
        self.farba = farba
        self.canvas.itemconfig(self.id, fill = farba)

# --- main ---

root = Tk()
canvas = Canvas(root)
canvas.pack()

k1 = Kruh(50,50,30,'blue')
k2 = Kruh(150,100,80)

k1.posun(30,10)
k2.zvacsi(50)
k1.prefarbi('green')

mainloop()



