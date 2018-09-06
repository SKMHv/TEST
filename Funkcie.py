# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 16:36:16 2017

@author: michal.hvila
https://www.linuxexpres.cz/software/python-3-6-funkcie-1-cast
http://python.input.sk/05.html
"""
#============================================================================== 
# ZAKLADNE FUNKCIE
#==============================================================================
len("Helloooo")                  #Out[x]: 8 / funkcia, ktora vracia dlzku zadanej sekvencie     
type("Hello paklasa")            #Out[x]: str / funkcia, ktora vracia typ hodnoty\
print()                          #Keyword argumenty file=sys.stdout a flush=False zajišťují výstup tisku do okna konzoly.
                                 #Změnou argumentu end="\n" na end="" lze zajistit pokračování tisku na témže řádku, přičemž rozestupem uvozovek lze ovlivnit rozestup mezi jednotlivými hodnotami výstupu.
                                 #Změnou argumentu sep="" lze přikázat typ oddělovače, případně vzdálenost mezi prvky entice. 
n = input("Zadejte své jméno: ") #funkcia vklada udaje cez vstup klavesnice
range()
abs(-5)                          #Out[x]: 5 /funkcia vracia absolutnu hodnotu argumentu
max(3*11, 5**3, 512-9, 1024*0)   #Out[x]: 503 /funkcia vracia najvasci zo zadanych argumentov 
pow(2, 3)                        #Out[x]: 8 /funkcia vracia mocninu 2 na 3 (2**2*3)
math.sqrt(x)                     #funkica modulu math vrati odmocninu z x 
math.exp(x)                      #funkica modulu math vrati e**x

#==============================================================================
# DEFINICIA
#==============================================================================
def novy_riadok():      #Definicia funkcie novy_riadok
    print()

print(".....")
novy_riadok()           #Volanie funkcie novy_riadok
print(".....")
#==============================================================================
# ZLOZENA FUNKCIA
#==============================================================================
def tri_riadky():
    novy_riadok()
    novy_riadok()
    novy_riadok()

print(".....")
tri_riadky()           # Volanie funkcie tri_riadky
print(".....")



#==============================================================================
# POCIATOCNA HODNOTA PARAMETROV FUNKCIE 
#==============================================================================
# Parametrom funkcie je dočasná premenná, ktorá vzniká pri volaní funkcie a
# prostredníctvom ktorej, môžeme do funkcie poslať nejakú hodnotu.
# Parametre funkcií definujeme počas definovania funkcie v hlavičke funkcie a
# ak ich je viac, oddeľujeme ich čiarkami:
#-----------------------------------------------------------------------------
def mocnina(m, n=3):
    print(m**n)

mocnina(2)
mocnina(3,2)

# -----------------------------
def vypis_hviezdiciek(pocet):
    print("*" * pocet)

vypis_hviezdiciek(30)

print()

for i in range(1,10):
    vypis_hviezdiciek(i)

#==============================================================================
# MENNY PRIESTOR
#==============================================================================
# Aby sme lepšie pochopili ako naozaj fungujú lokálne premenné, musíme rozumieť,
# čo to je a ako funguje menný priestor (namespace). Najprv trochu ďalšej
# terminológie: všetky identifikátory v Pythone sú jedným z troch typov (Python má
#  pre identifikátory 3 rôzne tabuľky mien):
#
#    > štandardné, napr. int, print, …
#         hovorí sa tomu builtins
#    > globálne - definujeme ich na najvyššej úrovni mimo funkcií, napr. funkcia vypis_sucet
#         hovorí sa tomu main
#    > lokálne - vznikajú počas behu funkcie
#
# Keď na nejakom mieste použijeme identifikátor, Python ho najprv hľadá
# (v tzv. menných priestoroch):
#
#    > v lokálnej tabuľke mien, ak tam tento identifikátor nenájde, hľadá ho
#    > v globálnej tabuľke mien, ak tam tento identifikátor nenájde, hľadá ho
#    > v štandardnej tabuľke mien
#-----------------------------------------------------------------------------

# Príkaz (štandardná funkcia) dir() vypíše tabuľku globálnych mien. Hoci pri štarte Pythonu by táto tabuľka mala byť prázdna, obsahuje niekoľko špeciálnych mien, ktoré začínajú aj končia znakmi '__':
dir()
# ['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']

# Keď teraz vytvoríme nejaké nové globálne mená, objavia sa aj v tejto globálnej tabuľke:
premenna = 2017
def funkcia():
    pass
dir()
# ['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__',
#  'funkcia', 'premenna']

# Podobne sa vieme dostať aj k tabuľke štandardných mien (builtins):
dir(__builtins__)
# ['ArithmeticError', 'AssertionError', 'AttributeError', ...
#
# Takto sa vypíšu všetky preddefinované mená. Vidíme medzi nimi napr. 'int', 'print',
#  'range', 'str', …

#==============================================================================
# PRIKAZ del
#==============================================================================
# Príkazom del zrušíme identifikátor z tabuľky mien. Formát príkazu:
#
# del premenná
#
# Príkaz najprv zistí, v ktorej tabuľke sa identifikátor nachádza (najprv pozrie
# do lokálnej a keď tam nenájde, tak do globálnej tabuľky) a potom ho z tejto
# tabuľky vyhodí. Príkaz nefunguje pre štandardné mená.
#-----------------------------------------------------------------------------

# Ukážme to na príklade: identifikátor print je menom štandardnej funkcie (v štandardnej
# tabuľke mien). Ak v priamom režime (čo je globálna úroveň mien) do premennej print
# priradíme nejakú hodnotu, toto meno vznikne v globálnej tabuľke:

print("ahoj")    # >>> ahoj
print = ("Ahoj") # Do premennej print sme priradili nejaku hodnotu
print            # Ahoj
print("ahoj")    # TypeError: 'str' object is not callable

# Teraz už print nefunguje ako funkcia na výpis hodnôt, ale len ako obyčajná globálna
# premenná. Ale v štandardnej tabuľke mien print stále existuje, len je prekrytá
# globálnym menom. Python predsa najprv prehľadáva globálnu tabuľku a až keď sa tam
# nenájde, hľadá sa v štandardnej tabuľke. A ako môžeme vrátiť funkčnosť štandardnej
# funkcie print? Stačí vymazať identifikátor z globálnej tabuľky:
#-----------------------------------------------------------------------------
del print
print("ahoj")

# vnorene volanie
def vypis_hviezdiciek(pocet):
    print('*' * pocet)

def trojuholnik(n):
    for i in range(1, n+1):
        vypis_hviezdiciek(i)

trojuholnik(10)

# Pri ich definovaní v globálnom mennom priestore vznikli dva identifikátory: vypis_hviezdiciek a trojuholnik. Zavoláme funkciu trojuholnik:
#
#     >>> trojuholnik(5)
#
# Najprv sa pre túto funkciu vytvorí jej menný priestor (lokálna tabuľka mien) s dvomi lokálnymi premennými: n a i. Teraz pri každom (vnorenom) volaní vypis_hviezdiciek(i) sa pre túto funkciu:
#
#     > vytvorí nový menný priestor s jedinou premennou pocet
#     > vykoná sa príkaz print()
#     > nakoniec sa zruší jej menný priestor, t.j. zanikne premenná pocet




#==============================================================================
# ARGUMENTY
# a) Volne pozicne argumenty 
# b) Keyword argumenty 
# c) Pozicne argumenty entice (tuple)
# d) Keyword argumenty slovniku (dict)
#==============================================================================
def hark(alfa, pi=3.14, *tup, **lib):
     print("Volné poziční argumenty: ", alfa)
     print("Keyword argumenty: ", pi)
     print("Poziční arg. entice: ", tup)
     print("Keyword arg. slovníku: ", lib)
     
hark(5)                     
#--------
#Volné poziční argumenty:  5  //alfa
#Keyword argumenty:  3.14     //pi
#Poziční arg. entice:  ()     
#Keyword arg. slovníku:  {}   
#-------------------------------

hark(5, 25)
#--------
#Volné poziční argumenty:  5         //alfa
#Keyword argumenty:  25              //pi
#Poziční arg. entice:  ()            
#Keyword arg. slovníku:  {}         
#-------------------------------

hark(5, 4, 3, fi=8)
#--------
#Volné poziční argumenty:  5         //alfa
#Keyword argumenty:  4               //pi
#Poziční arg. entice:  (3,)          //tub
#Keyword arg. slovníku:  {'fi': 8}   //lib
#-------------------------------

hark(5, a=8, b=5)
#--------
#Volné poziční argumenty:  5                //alfa
#Keyword argumenty:  3.14                   //pi
#Poziční arg. entice:  ()                   
#Keyword arg. slovníku:  {'a': 8, 'b': 5}   //lib
#-------------------------------
#= Hvězdička (*) =============================
# - ve výčtu parametrů přikazuje, aby všechny parametry, 
# které za ní následují, přijímaly pouze argumenty ve formátu "keyword". 
# Stejnou účinnost má i parametr *args:
def foo(a, b, *, c, d):
    print(a,b,c,d)

foo(1, 2, c="zuzu", d="zizi")  #Out[x]: 1 2 zuzu zizi
#======== 
# Sběrné parametry mohou posloužit jako šikovný 'vysavač' pro nadbytečně zadané argumenty:
def eta(a, b, *c, **d):
    print(a+b)
eta (1, 5, 3, 2)                #Out[x]: 6
#-------------------------------
def eta(a, b, *c, **d):
    print(a+b,c, d)
eta (1, 5, 3, d=2, x=6)         #Out[x]: 6 (3,) {'x': 6, 'd': 2}
#-------------------------------
def eta(a, b, *c, **d):
    print(a+b,c, d)
eta (1, 5, e=3, d=2, x=6)       #Out[x]: 6 () {'x': 6, 'e': 3, 'd': 2}
#-------------------------------
def sum_not_first(a, *bs):
    temp = sum(bs)
    print("sum is = ", temp)
    
sum_not_first(1,2,3,4)          #Out[x]: sum is =  9
#-------------------------------  
def test_agre(a,b,c):
    print("Virbl: ", (b+c)*a)
slova = ("Abra","Kadabra")
test_agre(2, *slova)            #Out[x]: Virbl:  AbraKadabraAbraKadabra //rozbalovanie z entice

pairs={'b':"Hej", 'c':"Hola"}   
test_agre(2, **pairs)           #Out[x]: Virbl:  HejHolaHejHola //rozbalovanie zo slovnika 
#------------------------------- 

def foo(a, b, *,c, d):
    print(a, b, c, d)
    
foo(2,4,3,d="JAN") #TypeError: foo() takes 2 positional arguments but 3 positional arguments (and 1 keyword-only argument) were given

#==============================================================================
# VYTVARANIE A IMPORT MODULOV
#==============================================================================

from Import import mocnina        # Import modulu V ramci projektu
mocnina(5)
#-----------
import sys
sys.path.append('d:/INSTAL/WINPYTHON/WinPython-64bit-3.5.3.0Qt5/notebooks')     #Import modulu s adresou modulu
sys.path.insert(0,'d:/INSTAL/WINPYTHON/WinPython-64bit-3.5.3.0Qt5/notebooks')   #alebo 0 -po prvom prvku
from Import import mocnina        # from file import funkcia / def mocnina(m, n=3): print(m**n)
mocnina(5)                        #Out[x]: 125
#-----------
from Import import mocnina
mocnina(5,2)                      #Out[x]: 25
#-----------
from Import import *             # * - vsetke funkcie z modulu
mocnina(5,2)                     #Out[x]: 25    
print_twice("koleso")            #Out[x]: koleso koleso
#-----------
import Import                    #Import modulu // file
Import.mocnina(5)                #Out[x]: 125 //volanie funkcie mocnina
Import.print_twice("Cica")       #Out[x]: koleso koleso //volanie funkcie print_twice

#==============================================================================
# CISTE FUNKCIE / FUNKCIE S NAVRATOVOU HODNOTOU A MODIFIKATORY
#  Cista funkcia vracia hodnotu prostrednictvom prikazu return, pricom nemeni
#  hodnotu zadanych argumentov a nema vedlajsie ucinky. 
#==============================================================================

#def area(rad):
#    print(3.14*rad**2)          # area(10) -->> 314.0
#def suma(rad):
#    print(area(rad)+b)          #TypeError: NoneType + int

rad = int(input ("Zadaj uhol --->"))
b = int(input ("Zadaj dlzku --->"))
def area(rad):  
    return  3.14*rad**2           # area(10) -->> 314.0
    
def suma(rad, b):
    print(3.14*rad**2)
    print(area(rad) + b)          # suma(10,100) -->> 414.0
   
area(rad)
suma(rad, b)

#-----------------------------------------------------------------------------
# Príkazom return sa ukončí výpočet funkcie (zruší sa jej menný priestor) a uvedená
# hodnota sa stáva výsledkom funkcie, napr.

def eura_na_koruny(eura):
    koruny = round(eura * 30.126, 2)
    return koruny

print('Dostal si 100 EUR co je', eura_na_koruny(100), 'SK')
# Dostal si 100 EUR co je 3012.6 SK

#-----------------------------------------------------------------------------
# Niekedy potrebujeme návratovú hodnotu počítať nejakým cyklom,
# napr. nasledovná funkcia počíta súčet čísel od 1 do n:

def suma(n):
    vysledok = 0
    while n > 0:
        vysledok += n
        n -=1
    return vysledok

print('suma(20) = ',suma(20))  # suma(20) =  210

#-----------------------------------------------------------------------------
# VYSLEDKOM FUNKCIE JE CISLO
# Nasledovná funkcia počíta n-tú mocninu nejakého čísla a tento výsledok ešte
# zníži o 1:
def pocitaj(n):
    return 2 ** n - 1
pocitaj(5)     # Out[]: 31

for i in (1, 2, 3, 8, 10, 16, 20, 32):
    print('pocitaj({}) = {}' .format(i, pocitaj(i)))

# pocitaj(1) = 1
# pocitaj(2) = 3
# pocitaj(3) = 7
# pocitaj(8) = 255
# pocitaj(10) = 1023
# pocitaj(16) = 65535
# pocitaj(20) = 1048575
# pocitaj(32) = 4294967295

#-----------------------------------------------------------------------------
# Ďalšia funkcia zisťuje dĺžku (počet znakov) zadaného reťazca. Využíva to, že
# for-cyklus vie prejsť všetky znaky reťazca a s každým môže niečo urobiť, napr.
# zvýšiť počítadlo o 1:

def dlzka(retazec):
    pocet = 0
    for znak in (retazec):
        pocet += 1
    return(pocet)

dlzka('Python')                 #Out[]: 6
dlzka(1000 * 'aB')              #Out[]: 2000

#-----------------------------------------------------------------------------
# VYSLEDKOM FUNKCIE JE LOGICKA HODNOTA
#
# vráti True alebo False podľa toho či je n párne (zvyšok po delení 2 bol 0),
# vtedy vráti True, alebo nepárne (zvyšok po delení 2 nebol 0) a vráti False.
# Túto istú funkciu môžeme zapísať aj tak, aby bolo lepšie vidieť tieto dve
# rôzne návratové hodnoty:

def parne(n):
    if n % 2 == 0:
        return True
    else:
        return False

parne(10)               #Out[]: True
parne(11)               #Out[]: False

for i in range(20,30):
    print(i, '=', parne(i))

# 20 = True
# 21 = False
# 22 = True
# 23 = False
# 24 = True
# 25 = False
# 26 = True
# 27 = False
# 28 = True
# 29 = False

#-----------------------------------------------------------------------------
# VYSLEDKOM FUNKCIE JE RETAZEC(STRING)
#
# Napíšme funkciu, ktorá vráti nejaký reťazec v závislosti od hodnoty parametra:

def farba(ix):
    if ix == 0:
        return 'red'
    elif ix == 1:
        return 'white'
    else:
        return 'yellow'
    #------------------------
    # Alebo
    # if ix == 0:
    #     return 'red'
    # if ix == 1:
    #     return 'white'
    # return 'yellow'
    #------------------------
for i in range(5):
    print(i, ' - ', farba(i))

# 0  -  red
# 1  -  white
# 2  -  yellow
# 3  -  yellow
# 4  -  yellow


#-----------------------------------------------------------------------------
# TYP PARAMETRU A TYP VYSLEDKU
#
# Python nekontroluje typy parametrov, ale kontroluje, čo sa s nimi robí vo funkcii.
# Napr. funkcia

def pocitaj(x):
    return 2 * x + 1

pocitaj(5)               # Out[]: 11
pocitaj('a')             # Out[]: TypeError: Can't convert 'int' object to str implicitly

#  V tele funkcie sa vsak moze kontrolovat typ parametra, napriklad :
def pocitaj(x):
    if type(x) == str:
        return 2 * x + '1'
    else:
        return 2* x + 1

pocitaj(5)          # Out[]: 11
pocitaj('A')        # Out[]: AA1

#==============================================================================
# GRAFICKE FUNKCIE
#==============================================================================
#
# Zadefinujeme funkcie, pomocou ktorých sa nakreslí 5000 náhodných farebných bodiek,
# ktoré budú zafarbené podľa nejakých pravidiel:

from tkinter import *
import random
# import math

# vzd() - Funkcia vzd() počíta vzdialenosť dvoch bodov (x1, y1) a (x2, y2) v rovine -
#           tu sa použil známy vzorec z matematiky. Táto funkcia nič nevypisuje, ale vracia
#           číselnú hodnotu (desatinné číslo)
def vzd(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5
    # return math.sqrt((10 - 5) **2 +(20 - 10) **2)    # >>> musi byt importnuty modul math


# kresli_bodku() - nič nevracia, ale vykreslí v grafickej ploche malý kruh s polomerom 5,
#                   ktorý je zafarbený zadanou farbou
def kresli_bodku(x, y, farba):
    canvas.create_oval(x+5, y+5, x-5, y-5, fill = farba, outline = '')


# farebne_bodky() - dostáva ako parameter počet bodiek, ktoré má nakresliť: funkcia na
#                   náhodné pozície nakreslí príslušný počet bodiek, pričom tie, ktoré sú od
#                   bodu (150, 150) vzdialené viac ako 100, budú tmavomodré (farba 'navy'),
#                   tie, ktoré sú od bodu (230, 150) vzdialené viac ako 100, budú červené
#                   a všetku ostatné budú žlté. Všimnite si, že sme za definíciami všetkých f
#                   unkcií napísali samotný program, ktorý využíva práve zadefinované funkcie.
def farebne_bodky(pocet):
    for i in range(pocet):
        x = random.randint(10, 290)  # vyberie nahodnu suradnicu x z intervalu 10 <-> 290
        y = random.randint(10, 290)  # vyberie nahodnu suradnicu y z intervalu 10 <-> 290
        if vzd(x, y, 150, 150) > 100:
            print(i, '-> NAVY - D1 = ', vzd(x, y, 150, 150))
            kresli_bodku(x, y, 'navy')
        elif vzd(x, y, 230, 150) > 100:
            print(i, '-> RED - D2 = ', vzd(x, y, 230, 150))
            kresli_bodku(x, y, 'red')
        else:
            kresli_bodku(x, y, 'yellow')
            print(i, '-> YELLOW - D1 = ', vzd(x, y, 230, 150), '; D2 = ', vzd(x, y, 150, 150) )

root = Tk()
root.configure(bg = 'black')
root.geometry('300x300')
canvas = Canvas(root, bg = 'black', width = '300', height = '300')
canvas.pack()

farebne_bodky(5000)

print("<------------------ KONIEC --------------------->")
root.mainloop()


#==============================================================================
# NAHRADNA HODNOTA PARAMETRA
#==============================================================================
def kresli_bodku(x, y, farba = 'blue', r = 3):
    canvas.create_oval(x+r, y+r, x-r, y-r, fill = farba, outline = '')

# V hlavičke funkcie môžeme k niektorým parametrom uviesť náhradnú hodnotu
# (vyzerá to ako priradenie). V tomto prípade to označuje to, že ak tomuto
# formálnemu parametru nebude zodpovedať skutočný parameter, dosadí sa práve
# táto náhradná hodnota. Pritom musí platiť, že keď nejakému parametru v definícii
# funkcie určíte, že má náhradnú hodnotu, tak náhradnú hodnotu musíte zadať aj
# všetkým ďalším formálnym parametrom, ktoré sa nachádzajú v zozname parametrov
# za ním (ak sme zadefinovali náhradnú hodnotu pre parameter farba, musíme nejakú
# zadefinovať aj pre parameter r).

kresli_bodku(150, 150)              # fill / farba bude 'blue', r bude 3
kresli_bodku(150, 150, 'red')       # fill / farba bude 'red', r bude 3
kresli_bodku(150, 150, 'red', 5)    # fill / farba bude 'red', r bude 5

#==============================================================================
# PARAMETRE VOLANE MENOM
#==============================================================================

# Python umožňuje funkcie s viac parametrami volať tak, že skutočné parametre
# neurčujeme pozične (prvému skutočnému zodpovedá prvý formálny, druhému druhý,
# atď.) ale priamo pri volaní uvedieme meno parametra. Takto môžeme určiť hodnotu
# ľubovoľnému parametru. Napr. všetky tieto volania sú korektné:

def kresli_bodku(x, y, farba = 'blue', r = 3):
    canvas.create_oval(x+r, y+r, x-r, y-r, fill = farba, outline = '')

kresli_bodku(150, 150, r = 10)
kresli_bodku(farba = "red", x = 150, y = 200)
kresli_bodku(r = 20, x = 250, y = 250)

#==============================================================================
# FAREBNY MODEL RGB
#==============================================================================
#
# Formátovanie reťazcov sa dá využiť aj na výpis celých čísel v šestnástkovej sústave.
# Už poznáme formát '{:5}', ktorý označuje, že príslušná hodnota sa vypíše na šírku 5.
# Za dvojbodku v zátvorkách '{}' okrem šírky môžeme písať aj typ výpisu. Tu sa nám bude
# hodiť typ výpisu 'x', ktorý označuje výpis v šestnástkovej sústave, napr.

'{:x}' .format(122)   # Out[]: '7a'
'{:3x}' .format(122)  # Out[]: ' 7a'  --- 3 = sirka vypisu

# Formátovanie reťazca pomocou '{:6x}' by kratšie ako 6-ciferné čísla doplnilo medzerami
# a preto využijeme ešte jednu špecialitu tohto formátu, ktoré čísla dopĺňa nulami:
# zapíšeme to ako '{:06x}', napr.
'{:06x}' .format(122)  # Out[]: '00007a'

# Môžeme predpokladať, že všetky farby v počítači sú namiešané z troch základných farieb:
# červenej, zelenej a modrej (teda Red, Green, Blue). Farba závisí od toho, ako je v nej
# zastúpená každá z týchto troch farieb. Zastúpenie jednotlivej farby vyjadrujeme číslom
# od 0 do 255 (zmestí sa do jedného bajtu, teda ako 2-ciferné šestnástkové číslo). Napr.
# žltá farba vznikne, ak namiešame 255 červenej, 255 zelenej a 0 modrej. Ak budeme zastúpenie
# každej farby trochu meniť, napríklad 250 červenej, 240 zelenej a hoci 100 modrej, stále to
# bude žltá, ale v inom odtieni.
#
#    > pre žltú (‚yellow‘): keďže platí red=255, green=255, blue=0, šestnástkovo je to trojica ff, ff, 00, a ako farba je to '#ffff00'
#    > pre tmavozelenú (‚darkgreen‘): red=0, green=100, blue=0, šestnástkovo je to trojica 00, 64, 00, a farba je potom '#006400'
#
# Keďže už vieme vytvárať reťazce so šestnástkovým zápisom čísel (napr. '{:02x}'.format(číslo))
# zapíšme funkciu rgb(), ktorá bude vytvárať farby pomocou RGB-modelu:

from tkinter import *
import random
# import math

def rgb(r,g,b):
    return '#{:02x}{:02x}{:02x}' .format(r, g, b)

def stvorec_RGB(x, y, strana, farba = ''):
    canvas.create_rectangle(x, y, x+30, y+30, fill = farba)

root = Tk()
root.configure(bg = 'black')
root.geometry('300x200')
canvas = Canvas(root, bg = 'black', width = '300', height = '300')
canvas.pack()

for i in range(10):
    stvorec_RGB(i*30, 10, 30, rgb(100+16*i, 0, 0))
    stvorec_RGB(i*30, 50, 30, rgb(100+16*i, 0, 255-26*i))
    stvorec_RGB(i*30, 90, 30, rgb(0, 26*i, 26*i))

print("<------------------ KONIEC --------------------->")
root.mainloop()


#==============================================================================
# NAHODNE FARBY
#==============================================================================

from tkinter import *
import random

def rgb(r,g,b):
    return '#{:02x}{:02x}{:02x}' .format(r, g, b)

def nahodna_farba():
    return rgb(random.randrange(256), random.randrange(256), random.randrange(256))

def stvorec_RGB(x, y, strana, farba = ''):
    canvas.create_rectangle(x, y, x+30, y+30, fill = farba)

root = Tk()
root.configure(bg = 'black')
root.geometry('300x300')
canvas = Canvas(root, bg = 'black', width = '300', height = '300')
canvas.pack()

for y in range(0, 300, 30):
    for x in range(0, 300, 30):
        stvorec_RGB(x, y, 30, nahodna_farba())


print("<------------------ KONIEC --------------------->")
root.mainloop()



#==============================================================================
# ZLOZENE FUNKCIE
#==============================================================================
print("<--- zadaj suradnice stredu kruznice --->")
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))

print("<--- zadaj suradnice bodu kruznice --->")
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))
print("<======================================>")

import math
def vzdialenost(x1,x2, y1,y2):              #
    return math.sqrt((x2-x1)**2+(y2-y1)**2)
    
def plocha(rad):
    print(math.pi*rad**2)

polomer = vzdialenost(xc,yc, xp,yp)  
vysledok = plocha(polomer)


def plocha2(xc, yc, xp, yp):
    polomer = vzdialenost(xc, yc, xp, yp)
    vysledok = plocha(polomer)
    
#def plocha2(xc, yc, xp, yp):
#    return plocha(dlzka(xc, yc, xp, yp))

#==============================================================================
# FUNKCIE AKO ARGUMENT  
#==============================================================================    

def f(n):
    return 3*n - 6   
    
def g(n):
    return 5*n+2

def h(n):
    return -2*n+17


def doto(value, funk):
    return funk(value)

print (doto(7, f))
print (doto(7, g))
print (doto(7, h))

#==============================================================================
# LOKALNE PREMENNE A PARAMETRE FUNKCIE 
#==============================================================================

def suc_dvojic(cast1, cast2):
    suc=cast1+cast2
    print(suc)

cast1 = "Keby pes nesral, "    
cast2 = "zajaca by chytil"

suc_dvojic(cast1, cast2)        #Out[x]: Keby pes nesral, zajaca by chytil

print(suc)                      #Out[x]: NameError: name 'suc' is not defined

#==============================================================================
# FUNKCIE S DOKUMENTACNYM RETAZCOM
#==============================================================================

def mocnina(m, n=3):
    '''
    ==================================================\ 
    Funkcia rata s n-tou mocninou s pevne 
    nastavenym exponentom n=3, je mozne ho zmenit
    ==================================================/
    '''
    print(m**3)
    
    
print(mocnina.__doc__)        # tlac dokumentacneho retazca z funkcie mocnina
mocnina(2)                    # tlac 2**3 z funkcie mocnina 





























   