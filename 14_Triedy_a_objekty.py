# ==================================
# 14. Triedy a objekty
# ==================================
# ----------------------------
# Vlastný typ
# ----------------------------
# V Pythone sú všetky typy objektové, t.j. popisujú objekty, a takýmto typom hovoríme trieda (po anglicky class).
# Všetky hodnoty (teda aj premenné) sú nejakého objektového typu, teda typu trieda, hovoríme im inštancia triedy
# (namiesto hodnota alebo premenná typu trieda).

# Zadefinujme vlastný typ, teda novú triedu:

class Student:
    pass

# Pomocou konštrukcie class Student: sme vytvorili prázdnu triedu, t.j. nový typ Student, ktorý zatiaľ nič nevie.
# Keďže je to typ, môžeme vytvoriť premennú tohto typu (teda skôr hodnotu typu Student,
# na ktorú do premennej priradíme referenciu):

fero = Student()
print(type(fero))    # <class '__main__.Student'>
print(fero)          # <__main__.Student object at 0x7f40793948d0>


# ----------------------------
# Atribúty
# ----------------------------
# O objektoch hovoríme, že sú to kontajnery na dáta. V našom prípade premenná fero je referenciou na prázdny kontajner.
# Pomocou priradenia môžeme objektu vytvárať nové súkromné premenné, tzv. atribúty. Takéto súkromné premenné nejakého
# objektu sa správajú presne rovnako ako bežné premenné, ktoré sme používali doteraz, len sa nenachádzajú v hlavnej
# pamäti (v globálnom mennom priestore) ale v „pamäti objektu“. Atribút vytvoríme tak, že za meno objektu fero
# zapíšeme meno tejto súkromnej premennej, pričom medzi nimi musíme zapísať bodku. Ak takýto atribút ešte neexistoval,
# vytvoríme ho priradením:

fero.meno = 'Frantisek'

# pre zistenie hodnoty atributu pouzijeme
print('referencia meno objektu fero = ', fero.meno)

# Pridajme do objektu fero ďalší atribút:
fero.priezvisko = 'Fyzik'

# Tento objekt teraz obsahuje dve súkromné premenné meno a priezvisko. Aby sme ich vedeli slušne vypísať,
# môžeme vytvoriť pomocnú funkciu vypis:
def vypis(st):
    print('Volam sa - ', st.meno, st.priezvisko)

vypis(fero)         # Volam sa -  Frantisek Fyzik

# ----------------------------
# Objekty sú meniteľné (mutable)
# ----------------------------


# Atribúty objektu sú súkromné premenné, ktoré sa správajú presne rovnako ako „obyčajné“ premenné.
# Premenným môžeme meniť obsah, napr.

fero.meno = 'Ferdinand'
vypis(fero)          # Volam sa -  Ferdinand Fyzik


# nami definované nové typy (triedy) sú vo všeobecnosti mutable - ak by sme chceli vytvoriť novú immutable triedu,
# treba ju definovať veľmi špeciálnym spôsobom a tiež s ňou úptpm treba pracovať veľmi opatrne

# Ukážme si to na príklade:

mato = fero
vypis(mato)        # Volam sa -  Ferdinand Fyzik

# Objekt mato nie je novým objektom ale referenciou na ten istý objekt ako fero.
# Zmenou niektorého atribútu sa zmení obsah oboch premenných:

mato.meno = 'Martin'
vypis(mato)     # Volam sa -  Martin Fyzik
vypis(fero)     # Volam sa -  Martin Fyzik

# ----------------------------
# Funkcie
# ----------------------------

print('\n')
# Zapíšme funkciu urob(), ktorá dostane dva znakové reťazce a vytvorí z nich nový objekt typy Student,
# pričom tieto dva reťazce budú obsahom dvoch atribútov meno a priezvisko:

def urob(m, p):
    """
    Pomocou tejto funkcie vieme definovať nové objekty typu Student, ktoré už budú mať vytvorené oba atribúty meno a priezvisko
    :param m: Meno
    :param p: Priezvisko
    :return: novy objekt s referenciami meno a priezvisko
    """
    novy = Student()
    novy.meno = m
    novy.priezvisko = p
    return novy

fero = urob('Ferdinand', 'Fyzik')
zuzka = urob('Zuzana', 'Matikova')
mato = urob('Martin','Fyzik')

vypis(fero)         # Volam sa -  Ferdinand Fyzik
vypis(zuzka)        # Volam sa -  Zuzana Matikova
vypis(mato)         # Volam sa -  Martin Fyzik

print('\n')
# Ani funkcia urob() nemodifikuje žiaden svoj parameter ani iné premenné, len vytvára novú inštanciu
# (a modifikuje atribúty svojej lokálnej premennej) a tú potom vracia ako výsledok funkcie.
# Funkcie, ktoré majú túto vlastnosť (nič nemodifikujú, len vytvárajú niečo nové) nazývame pravé funkcie
# (po anglicky pure function). Pravou funkciou bude aj funkcia kopia, ktorá na základe jedného objektu vyrobí nový,
# ktorý je jeho kópiou. Predpokladáme, že robíme kópiu inštancie Student, ktorá má atribúty meno a priezvisko:

def kopia(iny):
    novy = Student()
    novy.meno = iny.meno
    novy.priezvisko = iny.priezvisko
    return novy

evka = kopia(zuzka)
vypis(evka)             # Volam sa -  Zuzana Matikova
evka.meno = 'Eva'
vypis(evka)             # Volam sa -  Eva Matikova

# Obe inštancie sú teraz dva rôzne kontajnery, teda obe majú svoje vlastné súkromné premenné meno a priezvisko.

print('\n')
# Okrem pravých funkcií existujú tzv. modifikátory (po anglicky modifier). Je to funkcia, ktorá niečo zmení,
# najčastejšie atribút nejakého objektu. Funkcia nastav_hoby() nastaví danému objektu atribút hoby a vypíše o tom text:

def nastav_hoby(st, text_hoby):
    st.hoby = text_hoby
    print(st.meno, st.priezvisko, 'ma hoby', st.hoby)

nastav_hoby(fero, 'gitara')             # Ferdinand Fyzik ma hoby gitara
nastav_hoby(evka, 'cyklistika')         # Eva Matikova ma hoby cyklistika


# Keďže vlastnosť funkcie modifikátor je pre všetky mutable objekty veľmi dôležitá, pri písaní nových funkcií si vždy
# musíme uvedomiť, či je to modifikátor alebo pravá funkcia a často túto informáciu zapisujeme aj do dokumentácie.

# Všimnite si, že:

def zmen(st):
    """
    nie je modifikátor, lebo hoci funkcia mení obsah premennej meno, táto je len lokálnou premennou funkcie zmen
    a nemá žiaden vplyv ani na parameter st ani na žiadnu inú premennú.
    :param st:
    :return: vypis mena odzadu
    """
    meno = st.meno
    meno = meno[::-1]
    print(meno)

zmen(mato)          # nitraM
print(mato.meno)    # Martin

print('\n')
# ----------------------------
# Metody
# ----------------------------

# Všetky doteraz vytvárané funkcie dostávali ako jeden z parametrov objekt typu Student (inštanciu triedy)
# alebo takýto objekt vracali ako výsledok funkcie. Lenže v objektovom programovaní platí:
#
#    - objekt je kontajner údajov, ktoré sú vlastne súkromnými premennými objektu (atribúty)
#    - trieda je kontajner funkcií, ktoré vedia pracovať s objektmi (aj týmto funkciám niekedy hovoríme atribúty, ale častejšie ich voláme metódy)

# Pripomeňme si, ako vyzerá definícia triedy:
#
# class Student:
#     pass

# Príkaz pass sme tu uviedli preto, lebo sme chceli vytvoriť prázdne telo triedy (podobne ako pre def ale aj while a if).
# Namiesto pass ale môžeme zadefinovať funkcie, ktoré sa stanú súkromné pre túto triedu. Takýmto funkciám hovoríme metóda.
# Platí tu ale jedno veľmi dôležité pravidlo: prvý parameter metódy musí byť premenná, v ktorej metóda dostane inštanciu tejto triedy
# a s ňou sa bude ďalej pracovať. Zapíšme funkcie vypis() a nastav_hoby() ako metódy (t.j. funkcie definované vo vnútri triedy,
# teda sú to atribúty triedy):

class Student():

    def vypis(self):
        print('Volam sa',self.meno, self.priezvisko)

    def nastav_hoby(self,text_hoby):
        self.hoby = text_hoby
        print(self.meno, self.priezvisko, 'ma hoby', self.hoby)

# Keďže vypis() už teraz nie je globálna funkcia ale metóda, nemôžeme ju volať tak ako doteraz vypis(fero),
# ale k menu uvedieme aj meno kontajnera (meno triedy), kde sa táto funkcia nachádza, teda Student.vypis(fero):

fero = urob('Ferdinand', 'Fyzik')           # reinicializacia objektu
zuzka = urob('Zuzana', 'Matikova')          # reinicializacia objektu
mato = urob('Martin', 'Fyzik')              # reinicializacia objektu

# Takýto spôsob volania metód však nie je bežný:

Student.vypis(fero)         # Volam sa Ferdinand Fyzik
Student.vypis(zuzka)        # Volam sa Zuzana Matikova
Student.vypis(mato)         # Volam sa Martin Fyzik

print('\n')
# Namiesto neho sa používa trochu pozmenený, pričom sa vynecháva meno triedy.
# Budeme používať takéto poradie zápisu volania metódy:
fero.vypis()                # Volam sa Ferdinand Fyzik
zuzka.vypis()               # Volam sa Zuzana Matikova
mato.vypis()                # Volam sa Martin Fyzik

print('\n')
# Podobne zapíšeme priradenie hoby dvom študentom. Namiesto zápisu:
fero.nastav_hoby('gitara')                  # Ferdinand Fyzik ma hoby gitara
evka = urob('Eva', 'Matikova')              # reinicializacia objektu
evka.nastav_hoby('cyklistika')              # Eva Matikova ma hoby cyklistika


print('\n')
# ----------------------------
# Magicke metody
# ----------------------------
# Magické metódy majú definíciu úplne rovnakú ako bežné metódy. Python ich rozpozná podľa ich mena: ich meno začína
# aj končí dvojicou podčiarkovníkov __. Pre Python je tento znak bežná súčasť identifikátorov, ale využíva ich aj na
# tento špeciálny účel. Ako prvé sa zoznámime s magickou metódou __init__(), ktorá je jednou z najužitočnejších
# a najčastejšie definovaných magických metód.
# ------------------
# metóda __init__()
# ------------------
# Je magická metóda, ktorá slúži na inicializovanie atribútov daného objektu. Má tvar:
#
#    def __init__(self, parametre):
#         ...
# Metóda môže (ale nemusí) mať ďalšie parametre za self. Metóda nič nevracia, ale najčastejšie obsahuje len niekoľko priradení.

# Hovoríme, že metóda __init__() inicializuje objekt (niekedy sa hovorí aj, že konštruuje, resp. že je to konštruktor).
# Najčastejšie sa v tejto metóde priradzujú hodnoty do atribútov, napr.

class Student:
    def __init__(self, meno, priezvisko, hoby=''):      # hoby = '' - nastavenie defaultnej hodnoty, ak nie je pri volani __init__ ako 3. parameter zadefinovana
        self.meno = meno
        self.priezvisko = priezvisko
        self.hoby = hoby

    def vypis(self):
        print('Volam sa', self.meno, self.priezvisko,'a moje hoby je', self.hoby)

    def nastav_hoby(self, text):
        self.hoby = text
        print(self.meno, self.priezvisko, 'ma hoby', self.hoby)

# Vďaka tomu už nepotrebujeme funkciu urob(), ale inštanciu aj s atribútmi vyrobíme pomocou konštruktora:
Laco = Student('Ladislav', 'Zaloudek')
Laco.nastav_hoby('plavanie')                            # Ladislav Zaloudek ma hoby plavanie
Adka = Student('Adriana', 'Vargova', 'pecenie klacov')
Adka.vypis()                                            # Volam sa Adriana Vargova a moje hoby je pecenie klacov
print('\n')
# ------------------
# metóda dir()
# ------------------
# Funkcia dir() vráti postupnosť (zoznam) všetkých atribútov triedy alebo inštancie. Pozrime najprv nejakú prázdnu triedu:

class Test: pass

print(dir(Test))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
# '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
# '__str__', '__subclasshook__', '__weakref__']

# Vidíme, že napriek tomu, že sme zatiaľ pre túto triedu nič nedefinovali, v triede sa nachádza veľa rôznych atribútov.
# Jednu z nich už poznáme: __init__ je magická metóda. Vždy keď zadefinujeme nový atribút alebo metódu,
# objaví sa aj v tomto zozname dir():

t = Test()
t.x = 100
t.y = 200

print(dir(t))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
# '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
# '__str__', '__subclasshook__', '__weakref__',  'x', 'y']

print('\n')
# --------------------
# Príklad s grafikou
# --------------------
# Zadefinujeme novú triedu Kruh(r, x, y), ktorá bude mať 3 atribúty pre kruh v grafickej ploche: polomer a súradnice stredu:
class Kruh:
    def __init__(self,r,x,y):
        self.r = r
        self.x = x
        self.y = y

# Teraz, keď máme triedu, môžeme vytvárať nové inštancie (objekty), napr.
a = Kruh(70, 200, 100)
b = Kruh(10, 180, 80)
c = Kruh(10, 20, 80)
# Tieto objekty sú zatiaľ len „kontajnery“ pre atribúty.
# Do takejto triedy môžeme v inicializácii pridať aj ďalšie atribúty, ktoré nie sú v parametroch inicializácie napr.
class Kruh:
    def __init__(self,r,x,y):
        self.r = r
        self.x = x
        self.y = y
        self.farba = 'red'

# reinicializujem objekty
a = Kruh(70, 200, 100)
b = Kruh(10, 180, 80)
c = Kruh(10, 20, 80)

# Teraz zadefinujeme pomocnú funkciu kresli_kruh(kruh), ktorá očakáva parameter typu Kruh a tento kruh potom nakreslí
# do grafickej plochy (predpokladáme, že grafická plocha je už vytvorená a prístupná pomocou premennej canvas):

def kresli_kruh(kruh):
    w.create_oval(kruh.x-kruh.r, kruh.y-kruh.r, kruh.x+kruh.r, kruh.y+kruh.r, fill=kruh.farba)


# Otestujeme:

from tkinter import *

master = Tk()

w = Canvas(master, width=400, height=400)
w.pack()

# kresli_kruh(a)
# kresli_kruh(b)
# kresli_kruh(c)

# Takéto objekty kruhy môžeme uložiť aj do zoznamu a potom aj ich nakreslenie môže vyzerať takto:
zoznam = [a,b,c]
for k in zoznam:
    kresli_kruh(k)

print(zoznam)   # [<__main__.Kruh object at 0x7f5fa9e6e240>, <__main__.Kruh object at 0x7f5fa9e6e1d0>, <__main__.Kruh object at 0x7f5fa9e6e160>]
mainloop()
#vidíme len to, že zoznam obsahuje nejaké tri objekty typu Kruh. Zadefinujme preto metódu výpis(),
# ktorá vypíše detaily konkrétneho objektu. Do triedy Kruh dopíšeme túto metódu a do konštruktora pridáme aj štvrtý
# parameter farba. Tiež funkciu kresli_kruh() prepíšeme na metódu kresli():


print('\n')
from tkinter import *

class Kruh:
    def __init__(self,r,x,y,farba='red'):
        self.r = r
        self.x = x
        self.y = y
        self.farba = farba

    def vypis(self):
        return  f'Kruh({self.r}, {self.x}, {self.y}, {self.farba!r})'

    def kresli(self):
        w.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill=self.farba)


master = Tk()
w = Canvas(master, width=400, height=400)
w.pack()

# vytvorenie novych objekot
a = Kruh(70, 200, 100, 'yellow')
b = Kruh(10, 180, 80)
c = Kruh(10, 20, 80)

zoznam = [a,b,c]
for k in zoznam:
    k.kresli()
for k in zoznam:
    print(k.vypis())
    # Kruh(70, 200, 100, 'yellow')
    # Kruh(10, 180, 80, 'red')
    # Kruh(10, 20, 80, 'red')

mainloop()

# Pozrime ešte, čo nám vrátia volania funkcie dir() pre triedu Kruh aj inštanciu a:
print(dir(Kruh))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
# '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
# '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '__weakref__', 'kresli', 'vypis']
print(dir(a))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
# '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
# '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '__weakref__', 'farba', 'kresli', 'vypis', 'r', 'x', 'y']

# Všimnite si, že v triede Kruh pribudli dva atribúty, ktoré nie sú magickými metódami: kresli a vypis,
# v inštancii a okrem týchto metód pribudli 4 atribúty: farba, r, x a y.

# -----------------------
# CVICENIA - http://python.input.sk/14.html#priklad-s-grafikou
# -----------------------

print('\n')
# 1. Zadefinujte triedu Cas, ktorá bude mať dva celočíselné atribúty hodiny a minuty.
#    Aj inicializácia (metóda __init__()) bude mať dva parametre hodiny a minuty.
#    Metóda vypis() vypíše nastavený čas v tvare čas je 9:17.
# trieda Cas:
#
#       class Cas:
#           ...
#
# otestujte, napr.
#
#        >>> c = Cas(9, 17)
#        >>> c.vypis()
#            čas je 9:17
#        >>> d = Cas(10, 5)
#        >>> d.vypis()
#            čas je 10:05

class Cas():
    def __init__(self, hodiny, minuty):
        self.hodiny = hodiny
        self.minuty = minuty

    def vypis(self):
        return print('cas je ... {}:{}'.format(self.hodiny, self.minuty))

c = Cas(9, 17)
c.vypis()           # (cas je ... 9:17)
d = Cas(10, 5)
d.vypis()           # (cas je ... 10:5)
Cas.vypis(d)        # (cas je ... 10:5)

print('\n')
# 2. Do triedy Cas z úlohy (1) pridajte metódu str(), ktorá nič nevypisuje, ale namiesto toho vráti (return) znakový reťazec s hodinami a minútami v tvare '9:17'
#
#     napr.
#
#       >>> c = Cas(9, 1)
#       >>> print('teraz je', c.str())
#           teraz je 9:01

class Cas():
    def __init__(self, hodiny, minuty):
        self.hodiny = hodiny
        self.minuty = minuty

    def vypis(self):
        return print('cas je ... {}:{}' .format(self.hodiny, self.minuty))

    def str(self):
        return f'{self.hodiny}:{self.minuty}'

c = Cas(9, 1)
print('teraz je ...', c.str())      # teraz je ... 9:1

print('\n')
# 3. Do triedy Cas z (2) úlohy dopíšte metódu pridaj(), ktorá bude mať 2 parametre hodiny a minuty.
#    Metóda pridá k uloženému času zadané hodiny a minúty.
#
#     napr.
#
#        >>> cas = Cas(17, 40)
#        >>> print('teraz je', cas.str())
#            teraz je 17:40
#        >>> cas.pridaj(1, 35)
#        >>> print('neskôr', cas.str())
#            neskôr 19:15

class Cas():
    def __init__(self, hodiny, minuty):
        self.hodiny = hodiny
        self.minuty = minuty

    def vypis(self):
        return print('cas je ... {}:{}' .format(self.hodiny, self.minuty))

    def str(self):
        return f'{self.hodiny:02}:{self.minuty:02}'     # vrat string hodnot self.hodiny : self.minuty s doplneym 0 - :02 format

    def pridaj(self,hodiny, minuty):
        self.hodiny += hodiny
        if self.minuty + minuty == 60:
            print('1', end=' - ')
            self.hodiny += 1
            self.minuty = 0
            #print(' --',self.minuty)

        elif minuty == 0:
            print('2', end=' - ')
            self.minuty = 0

        elif minuty == 60:
            print('3', end=' - ')
            self.hodiny += 1
            self.minuty += 0

        elif minuty > 60:
            print('4', end=' - ')
            self.hodiny += minuty // 60
            self.minuty += minuty%60

        elif self.minuty + minuty > 60:
            print('5', end=' - ')
            self.hodiny += (self.minuty+minuty)//60
            self.minuty = (self.minuty+minuty)%60


        else:
            print('6', end=' - ')
            self.minuty += minuty


print('------ TESTUJEM ------ ')
cas = Cas(17, 40)
print('teraz je ...', cas.str())      # teraz je ... 17:40
cas.pridaj(1,35)
print('neskor bude ..', cas.str())    # 5 - neskor bude .. 19:15
print('--------------')
cas = Cas(17, 40)
print('teraz je ...', cas.str())      # teraz je ... 17:40
cas.pridaj(1,20)
print('neskor bude ..', cas.str())    # 1 - neskor bude .. 19:00
print('--------------')
cas = Cas(17, 00)
print('teraz je ...', cas.str())      # teraz je ... 17:00
cas.pridaj(1,00)
print('neskor bude ..', cas.str())    # 2 - neskor bude .. 18:00
print('--------------')
cas = Cas(17, 00)
print('teraz je ...', cas.str())      # teraz je ... 17:00
cas.pridaj(1,60)
print('neskor bude ..', cas.str())    # 1 - neskor bude .. 19:00
print('--------------')
cas = Cas(17, 00)
print('teraz je ...', cas.str())      # teraz je ... 17:00
cas.pridaj(1,65)
print('neskor bude ..', cas.str())    # 4 - neskor bude .. 19:05
print('--------------')
cas = Cas(17,5)
print('teraz je ...', cas.str())      # teraz je ... 17:00
cas.pridaj(1,60)
print('neskor bude ..', cas.str())    # 3 - neskor bude .. 19:05


print('\n')
# 4. Máme danú inštanciu c triedy Cas (z (3) úlohy). Vytvorte novú inštanciu, ktorá je od času c posunutá o
#    zadaný počet hodín a minút. Využite metódu pridaj(). Nemusíte na to vytvárať ani novú metódu ani funkciu,
#
#    napr.
#
#         >>> c = Cas(17, 40)
#         >>> d = ...          # vyrob kópiu času c
#         >>> ...              # posuň d o 2 hodiny a 55 minút
#         >>> print(c.str())
#             17:40
#         >>> print(d.str())
#             20:35

class Cas():
    def __init__(self, hodiny, minuty):
        self.hodiny = hodiny
        self.minuty = minuty

    def vypis(self):
        return print('cas je ... {}:{}' .format(self.hodiny, self.minuty))

    def str(self):
        return f'{self.hodiny:02}:{self.minuty:02}'     # vrat string hodnot self.hodiny : self.minuty s doplneym 0 - :02 format

    def pridaj(self,hodiny, minuty):
        self.hodiny += hodiny
        if self.minuty + minuty == 60:
            print('1', end=' - ')
            self.hodiny += 1
            self.minuty = 0
            #print(' --',self.minuty)

        elif minuty == 0:
            print('2', end=' - ')
            self.minuty = 0

        elif minuty == 60:
            print('3', end=' - ')
            self.hodiny += 1
            self.minuty += 0

        elif minuty > 60:
            print('4', end=' - ')
            self.hodiny += minuty // 60
            self.minuty += minuty%60

        elif self.minuty + minuty > 60:
            print('5', end=' - ')
            self.hodiny += (self.minuty+minuty)//60
            self.minuty = (self.minuty+minuty)%60


        else:
            print('6', end=' - ')
            self.minuty += minuty


print('------ TESTUJEM ------ ')
cas = Cas(17, 40)
print('cas ...', cas.str())      # cas ... 17:40
d = Cas(cas.hodiny, cas.minuty)  # vyrobim novy onjekt s parametrami hodnot objektu casu => kopia casu
print('d ...', d.str())          # d ... 17:40
print('---->')
d.pridaj(2,55)                   # volanie metody pridaj() pre posunutie casu o zadany parameter
print('cas ...', cas.str())      # cas ... 17:40
print('d ...', d.str())          # d ... 20:35


print('\n')
# 5. Vytvorte pätnásť-prvkový zoznam inštancií triedy Cas, v ktorom prvý prvok reprezentuje 8:10 a každý ďalší je
#    posunutý o 50 minút. Ďalšie časy v zozname vytvárajte v cykle, využite metódu pridaj().
#
#     napr.
#
#       >>> zoznam = [Cas(8, 10), ...]   # vyrob 15-prvkové zoznam časov
#       >>> for c in zoznam:
#             print(c.str(), end=' ')
#           8:10 9:00 9:50 ... 19:50

class Cas():
    def __init__(self, hodiny, minuty):
        self.hodiny = hodiny
        self.minuty = minuty

    def vypis(self):
        return print('cas je ... {}:{}' .format(self.hodiny, self.minuty))

    def str(self):
        return f'{self.hodiny:02}:{self.minuty:02}'     # vrat string hodnot self.hodiny : self.minuty s doplneym 0 - :02 format

    def pridaj(self,hodiny, minuty):
        self.hodiny += hodiny
        if self.minuty + minuty == 60:
            print('1', end=' - ')
            self.hodiny += 1
            self.minuty = 0
            #print(' --',self.minuty)

        elif minuty == 0:
            print('2', end=' - ')
            self.minuty = 0

        elif minuty == 60:
            print('3', end=' - ')
            self.hodiny += 1
            self.minuty += 0

        elif minuty > 60:
            print('4', end=' - ')
            self.hodiny += minuty // 60
            self.minuty += minuty%60

        elif self.minuty + minuty > 60:
            print('5', end=' - ')
            self.hodiny += (self.minuty+minuty)//60
            self.minuty = (self.minuty+minuty)%60


        else:
            print('6', end=' - ')
            self.minuty += minuty


print('------ TESTUJEM ------ ')
cas = Cas(8, 10)
# print('cas ...', cas.str())      # cas ... 08:10
zoznam = [cas]                     # prvy prvok bude cas(8,10)
pocet = 15                         # pocet prvkov

for i in range(1,pocet):
    kopia = Cas(zoznam[i-1].hodiny, zoznam[i-1].minuty) # kopia casu predosleho prvka v zozname[]
    zoznam.append(kopia)
    kopia.pridaj(0,50)                                  # posun kopiu o 50 minut

print('---->')
for c in zoznam:
    print(c.str(), end=' ')



print('\n')
# 6. Zapíšte definíciu triedy Zlomok, ktorá v inicializácii vytvorí dva atribúty citatel a menovatel.
#    Metóda vypis() pomocou print() tento zlomok vypíše v tvare zlomok je 3/8.
#
#     napr.
#
#       >>> z1 = Zlomok(3, 8)
#       >>> z2 = Zlomok(2, 4)
#       >>> z1.vypis()
#           zlomok je 3/8
#       >>> z2.vypis()
#           zlomok je 2/4


class Zlomok():
    def __init__(self, citatel, menovatel):
        self.citatel = citatel
        self.menovatel = menovatel

    def vypis(self):
        return print('Zlomok je --> {}/{}' .format(self.citatel, self.menovatel))

print('------------- TESTUJEM -------------')
z1 = Zlomok(3, 8)
z2 = Zlomok(2, 4)
z1.vypis()              # Zlomok je --> 3/8
z2.vypis()              # Zlomok je --> 2/4

print('\n')
# 7. Pridajte do triedy Zlomok z úlohy (6) dve metódy:
#
#     str() vráti (nič nevypisuje) reťazec v tvare 3/8
#
#     float() vráti (nič nevypisuje) desatinné číslo, ktoré reprezentuje daný zlomok
#
#     napr.
#
#     >>> z = Zlomok(3, 8)
#     >>> print('z je', z.str())
#         z je 3/8
#     >>> print('z je', z.float())
#         z je 0.375
#     >>> w = Zlomok(2, 4)
#     >>> print('w je', w.str())
#         w je 2/4
#     >>> print('w je', w.float())
#         w je 0.5


class Zlomok():
    def __init__(self, citatel, menovatel):
        self.citatel = citatel
        self.menovatel = menovatel

    def str(self):
        return f'{self.citatel}/{self.menovatel}'

    def float(self):
        return self.citatel / self.menovatel

print('------------- TESTUJEM -------------')
z = Zlomok(3, 8)
print('z je', z.str())          # z je 3/8
print('z je', z.float())        # z je 0.375
print('----->')
w = Zlomok(2, 4)
print('w je', w.str())          # w je 2/4
print('w je', w.float())        # w je 0.5

print('\n')
# 8. Zadefinujte triedu Body, ktorá si bude uchovávať momentálny stav bodov (napr. získané body v nejakej hre).
#    Trieda bude mať tieto metódy:
#
#     pridaj() k momentálnemu stavu pridá 1 bod
#
#     uber() od momentálneho stavu odoberie 1 bod
#
#     kolko() vráti celé číslo - momentálny bodový stav
#
#     napr.
#
#     b = Body()
#     for i in range(10):
#             b.pridaj()
#     b.uber()
#     b.uber()
#     print('body =', b.kolko())
#         body = 8


class Body():
    def __init__(self):
        self.stav = 0

    def pridaj(self):
        self.stav += 1

    def uber(self):
        self.stav -= 1

    def kolko(self):
        return self.stav

print('------------- TESTUJEM -------------')

b = Body()
print('body =', b.kolko())                      # body = 0

for i in range(10):
        b.pridaj()
print('body =', b.kolko())                      # body = 10

b.uber()
b.uber()
print('body =', b.kolko())                      # body = 8


print('\n')
# 9. Zadefinujte triedu Subor s metódami:
#
#     __init__(meno_suboru) vytvorí nový prázdny súbor
#
#     pripis(text) na koniec súboru pridá nový riadok so zadaným textom; použite open(..., 'a')
#
#     vypis() vypíše momentálny obsah súboru
#
#     napr.
#
#       >>> s = Subor('text.txt')
#       >>> s.pripis('prvy riadok')
#       >>> s.pripis('druhy riadok')
#       >>> s.vypis()
#           prvy riadok
#           druhy riadok
#       >>> s.pripis('posledny riadok')
#       >>> s.vypis()
#           prvy riadok
#           druhy riadok
#           posledny riadok


class Subor():
    def __init__(self,meno_suboru):
        self.meno_suboru = meno_suboru
        s = open(f'FILE/{self.meno_suboru}', 'w')
        s.close()

    def pripis(self, text):
        self.text = text
        s = open(f'FILE/{self.meno_suboru}', 'a')
        s.write(text + '\n')
        s.close()

    def vypis(self):
        with open(f'FILE/{self.meno_suboru}', 'r') as r:
            for i in r:
                print(i)


print('------------- TESTUJEM -------------')
s = Subor('14_9.txt')
s.pripis('prvy riadok')
s.pripis('druhy riadok')
s.vypis()
print('------ >')
s.pripis('posledny riaadok')
s.vypis()

print('\n')
# 10. Zadefinujte triedu Zoznam, pomocou ktorej si budeme vedieť udržiavať zoznam svojich záväzkov (sľubov, povinností, …).
#     Tieto budete uchovávať v atribúte zoznam typu list. Trieda obsahuje tieto metódy:
#
#     pridaj(prvok), ak sa tam takýto záväzok ešte nenachádza, pridá ho na koniec
#
#     vyhod(prvok), ak sa tam takýto záväzok nachádzal, vyhodí ho
#
#     je_v_zozname(prvok) vráti True alebo False podľa toho, či sa tam tento záväzok nachádza
#
#     vypis() vypíše všetky záväzky v tvare zoznam: záväzok, záväzok, záväzok
#
#     napr.
#
#       moj = Zoznam()
#       moj.pridaj('upratat')
#       moj.pridaj('behat')
#       moj.pridaj('ucit sa')
#       if moj.je_v_zozname('behat'):
#           print('musis behat')
#       else:
#           print('nebehaj')
#       moj.pridaj('upratat')
#       moj.vyhod('spievat')
#       moj.vypis()


class Zoznam():
    def __init__(self):
        self.zoznam = []

    def pridaj(self, prvok):
        if self.zoznam.count(prvok) != 0:
            print('Prvok sa uz nachadza v zozname')
        else:
            self.zoznam.append(prvok)

    def vyhod(self, prvok):
        if self.zoznam.count(prvok) != 0:
            self.zoznam.remove(prvok)
        else:
            print('Prvok sa nenachdza v zozname, nie je potrebne ho mazat')

    def je_v_zozname(self,prvok):
        if self.zoznam.count(prvok) != 0:
            return True
        else:
            return False

    def vypis(self):
        print(', '.join(self.zoznam))


print('------------- TESTUJEM -------------')

moj = Zoznam()
moj.pridaj('upratat')
moj.pridaj('behat')
moj.pridaj('ucit sa')
moj.vypis()                         # upratat, behat, ucit sa

if moj.je_v_zozname('behat'):
    print('musis behat')            # musis behat
else:
    print('nebehaj')
print('------->')
moj.pridaj('upratat')               # Prvok sa uz nachadza v zozname
moj.vyhod('spievat')                # Prvok sa nenachdza v zozname, nie je potrebne ho mazat
moj.vypis()                         # upratat, behat, ucit sa


print('\n')
# 11. Zadefinujte triedu TelefonnyZoznam, ktorá bude udržiavať informácie o telefónnych číslach
#     (ako zoznam list dvojíc tuple).
#     Trieda bude mať tieto metódy:
#
#       pridaj(meno, telefon) pridá do zoznamu dvojicu (meno, telefon); ak takéto meno v zozname už existovalo,
#       nepridáva novú dvojicu, ale nahradí len telefónne číslo
#
#       vypis() vypíše celý telefónny zoznam
#
#     napr.
#
#       tz = TelefonnyZoznam()
#       tz.pridaj('Jana', '0901020304')
#       tz.pridaj('Juro', '0911111111')
#       tz.pridaj('Jozo', '0212345678')
#       tz.pridaj('Jana', '0999020304')
#       tz.vypis()
#
#     vypíše
#
#     Jana 0999020304
#     Juro 0911111111
#     Jozo 0212345678


class TelefonnyZoznam():
    def __init__(self):
        self.zoznam = []

    def pridaj(self, meno, telefon):
        print('pridaj({},{}) ---->' .format(meno,telefon), end=' do ')
        print(self.zoznam)
        vyskyt = 0

        for i in self.zoznam:
            if i.count(meno) != 0:
                vyskyt += 1
                print('>>>>>> Pre meno \'{}\' nahradzujem povodny telefon \'{}\' za novvy telefon \'{}\'' .format(meno, i.pop(), telefon))
                i.append(telefon)

        if vyskyt == 0:
            self.zoznam.append([meno,telefon])



    def vypis(self):
        print('\nVypis() ---->')
        for z in self.zoznam:
            print(' '.join(z))


print('------------- TESTUJEM -------------')

tz = TelefonnyZoznam()
tz.pridaj('Jana', '0901020304')
tz.pridaj('Juro', '0911111111')
tz.pridaj('Jozo', '0212345678')
tz.pridaj('Jana', '0999020304')
tz.vypis()

# ------------- TESTUJEM -------------
# pridaj(Jana,0901020304) ----> do []
# pridaj(Juro,0911111111) ----> do [['Jana', '0901020304']]
# pridaj(Jozo,0212345678) ----> do [['Jana', '0901020304'], ['Juro', '0911111111']]
# pridaj(Jana,0999020304) ----> do [['Jana', '0901020304'], ['Juro', '0911111111'], ['Jozo', '0212345678']]
# >>>>>> Pre meno 'Jana' nahradzujem povodny telefon '0901020304' za novvy telefon '0999020304'
#
# Vypis() ---->
# Jana 0999020304
# Juro 0911111111
# Jozo 0212345678

print('\n')
# 12. Zadefinujte triedu Okno, ktorá otvorí grafické okno a do stredu vypíše zadaný text.
#     Výška otvoreného okna nech je 100. Vypísaný text nech je v strede okna fontom veľkosti 50.
#     Inicializácia (metóda __init__()) vytvorí nový canvas (výšky 100) a do jeho stredu vypíše zadaný text.
#     Zrejme si v svojich atribútoch zapamätá canvas aj identifikačný kód pre create_text().
#     Ďalšie dve metódy menia vypísaný text:
#
#       - zmen(text) zmení vypísaný text (zrejme na to použijete itemconfig())
#
#       - farba(farba) zmení farbu vypísaného textu (zrejme na to použijete itemconfig())
#
#     napr.
#
#     import tkinter
#     okno = Okno('ahoj')
#     okno.farba('red')
#     okno.zmen('Python')

from tkinter import *

class Okno():
    def __init__(self,text):
        self.master = Tk()
        self.text = text
        self.master.title(self.text)
        self.w = Canvas(self.master, width=200, height=100)
        self.w.pack()
        self.create_text = self.w.create_text(100, 50, text=self.text, font='arial 50')

    def zmen(self,text):
        self.text = text
        self.master.title(self.text)
        self.w.itemconfig(self.create_text,text=self.text)

    def farba(self,farba):
        self.w.itemconfig(self.create_text,text=self.text, fill =farba)


print('------------- TESTUJEM -------------')

okno_1 = Okno('ahoj')
okno_1.farba('red')
okno_1.zmen('Python')

okno_2 = Okno('Kukurica')
okno_2.farba('blue')
okno_2.zmen('Chlieb')

mainloop()

print('\n')
# Nedokoncene
# DZ. Napíšte pythonovský modul, ktorý bude obsahovať jedinú triedu Stvorce a žiadne iné globálne premenné:
#
#   class Stvorce:
#      def __init__(self, n):
#         ...
#
#      def urob(self, index):
#         ...
#
#      def vypis(self):
#         ...
#
# Metódy majú fungovať takto:
#
#     - inicializácia __init__(self, n) vyhradí takú dvojrozmernú tabuľku, aby sa dali deliť kvadranty do hĺbky n;
#       každý elementárny štvorček môže obsahovať 0 alebo 1, pri inicializácii budú všade 0
#
#     - metóda urob(self, index) dostáva číslo kvadrantu ako znakový reťazec (môže byť aj prázdny) a pre zadaný kvadrant
#       vyznačí všetky elementárne štvorčeky tak, že hodnoty 0 nahradí 1 a hodnoty 1 nahradí 0
#
#     - metóda vypis(self) vypíše (pomocou print()) momentálny obsah dvojrozmernej tabuľky, pričom namiesto 0 použije
#       znak '-' a namiesto 1 znak 'X'

class Stvorce:
    def __init__(self,n):
        self.n = n
        print('n = {} => {}x{}' .format(n, 2**self.n, 2**self.n))
        self.tabulka = []
        for j in range(2**self.n):      # n = 1 tabulka[[0,0][0,0]] n = 2 tabulka[[0,0,0,0][0,0,0,0],[0,0,0,0],[0,0,0,0]]
            self.tabulka.append([0]*(2**self.n))
        print('tabulka = ', self.tabulka)

    def urob(self, index):
        #r = 0
        cisla_kvadrantov = []
        cisla_kvadrantov.append(index)
        print('cisla_kvadrantov = ', cisla_kvadrantov)
        # cisla_kvadrantov[r] = [int(i) for i in cisla_kvadrantov[r]]  # premen prvky riadku v tab[] na integer



    def vypis(self):
        print('-------------------------------------\\')
        for i in self.tabulka:
            for j in i:
                if j != 0:
                    print('x', end=' ')
                else:
                    print('-', end=' ')
            print('')
        print('-------------------------------------/')

# indexi pre n = 3:

# i=1   1-4 x 1-4   i=11 1-2 x 1-2, i=12 1-2 x 3-4, i=13 3-4 x 1-2, i=14 3-4 x 3-4
# i=2   1-4 x 5-8   i=21 1-2 x 5-6, i=22 1-2 x 7-8, i=23 3-4 x 5-6, i=24 5-6 x 5-6
# i=3   5-8 x 1-4   i=31
# i=4   5-8 x 5-8

print('------------- TESTUJEM -------------')
stv = Stvorce(3)
stv.urob('3')
stv.vypis()