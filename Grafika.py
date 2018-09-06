# -*- coding: utf-8 -*-
"""
Created on Tue May 16 16:07:11 2017

@author: michal.hvila
http://python.input.sk/03.html
"""

# canvas.create_line(x1, y1, x2, y2) -  kreslenie ciary
# canvas.create_rectangle(x1, y1, x2, y2) - kreslenie obdlznika


#==============================================================================
# KRESLENIE CIAR
#==============================================================================
from tkinter import *  # Import modulu tkinter
root = Tk()                                  # Vytvorenie noveho okna
root.wm_iconbitmap('Icon\Knoppix logo.ico')  # Set ikony
root.title("Grafika ucime sa")               # Set nazov okna
root.geometry("300x300")                     # Set velikost okna
canvas = Canvas(bg = "black")                # Zadefinovanie grafickej plochy do premennej "canavas"
canvas.pack()                                # Zobrazenie grafickej plochy zadefinovanej v premennej "canavas"
canvas.create_line(10, 10, 90, 10, 10, 60, width = "4", fill ="red") # Suradnice (x1 , y1, x2, y2, ....) ucesky + sirka a farba ciary
canvas.create_line(120, 10, 70, 97, 170, 97, 120, 10, width = "4", fill = "blue")
root.mainloop()                              # Vykreslenie okna a start jeho zobrazenia
#==============================================================================
# KRESLENIE OBDLZNIKA
#==============================================================================
#
# funkcia canvas.create_rectangle()
#
# canvas.create_rectangle(x, y, x, y)
# canvas.create_rectangle(x, y, x, y, width=číslo, fill=farba, outline=farba)
#     Parametre:
#
#         x,y – dvojica súradníc jedného vrcholu obdĺžnika
#         width=číslo – nastavenie hrúbky čiary obrysu, ak parameter chýba, predpokladá sa hrúbka 1
#         fill=farba – nastavenie farby výplne, ak parameter chýba, predpokladá sa priesvitná farba, t.j. ''
#         outline=farba – nastavenie farby čiary obrysu, ak tento parameter chýba, predpokladá sa farba 'black', prázdny reťazec '' označuje obdĺžnik bez obrysu
#
# Funkcia canvas.create_rectangle() na základe dvoch bodov v ploche nakreslí obdĺžnik, ktorého strany sú rovnobežné so súradnicovými osami.
# Číselné hodnoty pre súradnice môžu byť aj desatinné čísla.
#------------------------------------------------------------------------------
from tkinter import *  # Import modulu tkinter
root = Tk()                                  # Vytvorenie noveho okna
root.wm_iconbitmap('Icon\Knoppix logo.ico')  # Set ikony
root.title("Grafika ucime sa")               # Set nazov okna
root.geometry("600x600")                     # Set velikost okna
#------------------------------------------------------------------------------
canvas = Canvas(bg = "black")                # Zadefinovanie grafickej plochy do premennej "canavas"
canvas.pack()                                # Zobrazenie grafickej plochy zadefinovanej v premennej "canavas"

# Nakreslí obdĺžnik s vrcholmi so súradnicami (50, 120) a (150, 70).
# Dĺžky strán tohto obdĺžnika sú 100 a 50. Zrejme ďalšie dva vrcholy majú súradnice (50, 70) a (150, 120).
canvas.create_rectangle(50, 120, 150, 70, fill = "white")
#------------------------------------------------------------------------------
canvas = Canvas(bg = "white")
canvas.pack()
# Nakreslí štvorec, ktorého súradnice ľavého horného vrcholu sú
# (x, y), t.j. (80, 60) a jeho strana je 35. Podobne:
x, y, a = 200, 60, 100
canvas.create_rectangle(x, y, x+a, y+a, fill = "blue") # Vykreslenie obdlznika
#------------------------------------------------------------------------------
canvas = Canvas(bg = "black")
canvas.pack()
# Nakreslí obdĺžnik, ktorého súradnice stredu sú (x, y), t.j. (150, 90) a jeho
# strany sú 60 a 100. Všimnite si, že súradnice vrcholov sme tu zadali ako desatinné čísla (typ float).
x, y, a, b = 150, 90, 60, 100
canvas.create_rectangle(x-a/2, y-b/2, x+a/2, y+b/2, fill = "red")
#------------------------------------------------------------------------------
# A opacne zadanie canvas hodnot obdlznika
canvas = Canvas(bg = "white")
canvas.pack()
x, y, a, b = 150, 90, 60, 100
canvas.create_rectangle(x+a/2, y+b/2, x-a/2, y-b/2, width = 5)  # Vyplne je ziadna a obrys je cierny hrubky 5

root.mainloop()           # Vykreslenie okna s jednotlivymi grafickymi plochami a start jeho zobrazenia

#==============================================================================
# KRESLENIE ELIPSY
#==============================================================================
#
# funkcia canvas.create_oval()
#
# canvas.create_oval(x, y, x, y)
# canvas.create_oval(x, y, x, y, width=číslo, fill=farba, outline=farba)
#     Parametre:
#
#         x,y – dvojica súradníc jedného vrcholu „opísaného obdĺžnika“ elipsy
#         width=číslo – nastavenie hrúbky čiary obrysu, ak parameter chýba, predpokladá sa hrúbka 1
#         fill=farba – nastavenie farby výplne, ak parameter chýba, predpokladá sa priesvitná farba, t.j. ''
#         outline=farba – nastavenie farby čiary obrysu, ak tento parameter chýba, predpokladá sa farba 'black', prázdny reťazec '' označuje elipsu bez obrysu
#
# Funkcia canvas.create_oval() na základe dvoch bodov „opísaného obdĺžnika“ nakreslí elipsu. Strany takéhoto mysleného obdĺžnika sú rovnobežné sú súradnicovými osami.
#------------------------------------------------------------------------------
from tkinter import *
root = Tk()
root.configure(background = "black")
root.title("KRESLENIE ELIPSY")
#------------------------------------------------------------------------------
canvas = Canvas(bg = "lack",)
canvas.pack()
canvas.create_rectangle(100, 240, 300, 140, fill = "blue") # obdlznik
canvas.create_oval(100, 240, 300, 140, outline = "red")          # elipsa dotykajuca sa stran obdlznika

#------------------------------------------------------------------------------
# Tento program nakreslí 10 sústredných kruhov (so spoločným stredom (150, 120))
# a s polomermi 100, 90, 80, …, 20, 10. Kruhy sú vyplnené červenou farbou a preto ich kreslíme od
# najväčšieho po najmenší, inak by väčšie kruhy zakryli menšie a menšie by nebolo vidieť.
# Ak by sme chceli tieto kruhy striedavo zafarbovať dvomi rôznymi farbami, môžeme využiť vymieňanie obsahov
# dvoch premenných:
canvas = Canvas(bg = "white")
canvas.pack()
x, y = 150, 120
farba, farba_1 = "black", "red"

for r in range(100, 0, -10):
    if r != 10:
        canvas.create_oval(x + r, y + r, x - r, y - r, outline = farba, width = 5)
    else:
        canvas.create_oval(x + r, y + r, x - r, y - r, fill = farba)
    farba, farba_1 = farba_1, farba

root.mainloop()


#==============================================================================
# KRESLENIE POLYGONU
#==============================================================================
#
# funkcia canvas.create_polygon()
#
# > canvas.create_polygon(x, y, x, y, …)
# > canvas.create_polygon(x, y, x, y, …, width=číslo, fill=farba, outline=farba)
#     Parametre:
#
#        - x,y – dvojica súradníc jedného vrcholu obrysu n-uholníka
#        - width=číslo – nastavenie hrúbky čiary obrysu, ak parameter chýba, predpokladá sa hrúbka 1
#        - fill=farba – nastavenie farby výplne, ak parameter chýba, predpokladá sa čierna, t.j. 'black', prázdny reťazec '' označuje n-uholníka bez výplne
#        - outline=farba – nastavenie farby čiary obrysu, ak tento parameter chýba, predpokladá sa priesvitná farba ''
#
# Funkcia canvas.create_polygon() na základe postupnosti bodov nakreslí n-uholník. Do príkazu musíme zadať minimálne 3 vrcholy.
#------------------------------------------------------------------------------
from tkinter import *
root = Tk()
root.configure(background = "black")
root.title("KRESLENIE POLYGONU")
#------------------------------------------------------------------------------
canvas = Canvas(bg = "black",)
canvas.pack()
# Spojí tromi úsečkami tri body (50, 120), (150, 70) a (200, 200)
# a potom tento trojuholník vyfarbí farbou výplne. Keďže sme nenastavili
# ani farbu obrysu ani farbu výplne, útvar sa vyplní čiernou farbou a obrys je
# vypnutý (ako keby bolo nastavené outline='' a fill='black').
canvas.create_polygon(50, 120, 150, 70, 200, 200, outline = "", fill = 'red')
#------------------------------------------------------------------------------
canvas = Canvas(bg = 'red')
canvas.pack()
canvas.create_polygon(20, 80, 120, 80, 40, 150, 70, 30, 100, 150, fill='yellow', outline='yellow')
#------------------------------------------------------------------------------
# definicia suradnic bodov v premennych
canvas = Canvas(bg = 'white')
canvas.pack()
b1 = (50, 20)
b2 = (150, 20)
b3 = (150, 80)
b4 = (50, 80)
canvas.create_polygon(b1, b2, b3, b4, fill = 'gray', outline = 'blue')
# to iste ako >>>
canvas.create_polygon(b1, b2, b4, b3, fill='red')
canvas.create_polygon(b1, b3, b2, b4, fill='green')
root.mainloop()

#------------------------------------------------------------------------------
# DALSIE OKNO
root = Tk()
root.configure(background = "black")
root.title("KRESLENIE POLYGONU")
#------------------------------------------------------------------------------
canvas = Canvas(bg = "black",)
canvas = Canvas(bg = 'black')
canvas.pack()
# Prvý for-cyklus nakreslí tri obdĺžniky, ktoré majú jeden vrchol (175, 75)
# spoločný a druhý je jeden z (130, 30), (150, 60), (200, 90).
for bod in (130, 30), (150, 60), (200, 160):
    canvas.create_rectangle(bod, 175,75, outline = "white")
#------------------------------------------------------------------------------
canvas = Canvas(bg = 'white')
canvas.pack()
# Druhý for-cyklus nakreslí 3 kružnice všetky s polomerom 20, pričom poznáme
# stredy týchto kružníc: (100, 100), (150, 150), (200, 160). Všimnite si, že
# tento cyklus má dve premenné cyklu x a y a paralelne sa do nich priradzujú dvojice zadaných čísel.
for x, y in (100, 100),(150, 150),(200, 160):
    canvas.create_oval(x-20, y-20, x+20, y+2, width = 5)
root.mainloop()

#==============================================================================
# PISANIE TEXTU
#==============================================================================
#
# funkcia canvas.create_text()
#
# canvas.create_text(x, y, text=‘text‘)
# canvas.create_text(x, y, text=‘text‘, font=‘písmo‘, fill=farba, angle=číslo)
#     Parametre:
#
#         x,y – dvojica súradníc stredu vypisovaného textu
#         text=‘text‘ – zadaný text
#         fill=farba – nastavenie farby textu
#         font=‘písmo‘ – nastavenie typu písma a aj jeho veľkosti
#         angle=číslo – otočenie výpisu o zadaný uhol v stupňoch (tento parameter nemusí fungovať na počítačoch Mac)
#
# Funkcia canvas.create_text() na zadanú súradnicu stredu vypíše text.
#------------------------------------------------------------------------------
from tkinter import *
root = Tk()
root.configure()
root.title("PISANIE TEXTU")
#------------------------------------------------------------------------------
canvas = Canvas()
canvas.pack()
canvas.create_text(150, 50, text='Python', fill='blue', font='arial 30 bold')
root.mainloop()

#==============================================================================
# KRESLENIE OBRAZKA
#==============================================================================
#
# funkcia canvas.create_image()
#
# canvas.create_image(x, y, image=premenná)
#     Parametre:
#
#         x,y – dvojica súradníc stredu vykresľovaného obrázka
#         image=premenná – nastaví obrázok, ktorý sa vykreslí (premenná musí byť obrázkový objekt,
#                          ktorý vznikol pomocou tkinter.PhotoImage(file='meno suboru'))
#
# Funkcia canvas.create_image() na zadanú súradnicu stredu nakreslí zadaný obrázok.
#------------------------------------------------------------------------------

from tkinter import *
root = Tk()
root.geometry("600x300")
root.configure(bg = "black")
root.title("KRESLENIE OBRAZKA")
#------------------------------------------------------------------------------
canvas = Canvas(bg = "black")
canvas.pack()
obr = PhotoImage(file = 'Image\cf.png')
canvas.create_image(180, 150, image = obr)
root.mainloop()

#==============================================================================
# PARAMETRE GRAFICKEJ PLOCHY
#==============================================================================
#
# > Pri vytváraní grafickej plochy (pomocou tkinter.Canvas()) môžeme nastaviť veľkosť plochy ale aj farbu pozadia grafickej plochy. Môžeme uviesť tieto parametre:
#
#     bg= nastavuje farbu pozadia (z anglického „background“)
#     width= nastavuje šírku grafickej plochy
#     height= výšku plochy
#------------------------------------------------------------------------------

from tkinter import *
root = Tk()
root.configure(bg = "black")
root.title("PARAMETRE GRAFICKEJ PLOCHY")
#------------------------------------------------------------------------------
canvas = Canvas(root, bg = "black", width = '600', height = '300') # defaultne nastavenie plochy
canvas.pack()                           # vykresli garficku plochu
bg_default = str(canvas['bg'])          # zapamataj si aktualne bg do premennej "bg_default"
sirka_default = int(canvas['width'])    # zapamataj si aktualnu sirku do premennej "sirka_default"
vyska_default = int(canvas['height'])   # zapamataj si aktualnu sirku do premennej "vyska_default"
canvas['bg'] = 'red'                    # zmena grafickeho parametru bg
canvas['width'] = '300'                 # zmena grafickeho parametru width
canvas['height'] = '150'                # zmena grafickeho parametru heignt
obr = PhotoImage(file = 'Image\cf.png')         # nacitanie obrazka (cesta k file)
canvas.create_image(150, 75, image = obr)       # vykreslenie obrazka do plochy
#------------------------------------------------------------------------------
canvas = Canvas(root, bg = bg_default, width = sirka_default, height = vyska_default)  # nastavenie ulozenych grafickych parametrov
canvas.pack()                           # vykresli garficku plochu
canvas.create_image(sirka_default / 2, vyska_default / 2, image = obr) # vykreslenie obrazka do plochy
root.mainloop()

#==============================================================================
# ZMAZANIE NAKRESLENEHO TVARU
#==============================================================================
#
# funkcia canvas.delete()
#
#    > slúži na zmazanie ľubovoľného nakresleného útvaru
#    > jeho tvar je canvas.delete(identifikátor)
#        - kde identifikátor je návratová hodnota príkazu kreslenia útvaru
#    > ak ako identifikátor použijeme reťazec 'all', príkaz zmaže všetky doteraz nakreslené útvary
#------------------------------------------------------------------------------
from tkinter import *
root = Tk()
root.configure(bg = "black")
root.title("ZMAZANIE NAKRESLENEHO TVARU")
#------------------------------------------------------------------------------
canvas = Canvas(root, bg = "black", width = '600', height = '300') # defaultne nastavenie plochy
canvas.pack()                           # vykresli garficku plochu
id1 = canvas.create_line(25, 52, 120, 55, fill = "red")     # zadefinovanie ciary premennej
id2 = canvas.create_line(60, 14, 100, 20, fill = "blue")    # zadefinovanie ciary premennej
canvas.delete(id1)                      # zmazanie ciary ako premenna id1
root.mainloop()

#==============================================================================
# POSUNUTIE NAKRESLENEHO TVARU
#==============================================================================
#
# funkcia canvas.move()
#
#    > slúži na posúvanie ľubovoľného nakresleného útvaru
#    > jeho tvar je canvas.move(identifikátor, dx, dy)
#        - kde identifikátor je návratová hodnota príkazu kreslenia útvaru
#        - dx a dy označujú číselné hodnoty zmeny súradníc útvaru
#    > posúvaný útvar môže byť ľubovoľne komplikovaný (môže sa skladať aj z väčšieho počtu bodov), príkaz canvas.move() posunie všetky vrcholy útvaru
#    > ak ako identifikátor použijeme reťazec 'all', príkaz posunie všetky doteraz nakreslené útvary
#------------------------------------------------------------------------------
from tkinter import *
root = Tk()
root.configure(bg = "black")
root.title("POSUNUTIE NAKRESLENEHO TVARU")
#------------------------------------------------------------------------------
canvas = Canvas(root, bg = "black", width = '600', height = '300') # defaultne nastavenie plochy
canvas.pack()                           # vykresli garficku plochu
id1 = canvas.create_line(25, 52, 120, 200, fill = "red")
id2 = canvas.create_line(60, 14, 100, 300, fill = "blue")
#------------------------------------------------------------------------------
canvas = Canvas(root, bg = "black", width = '600', height = '300') # defaultne nastavenie plochy
canvas.pack()
id1 = canvas.create_line(25, 52, 120, 200, fill = "red")
id2 = canvas.create_line(60, 14, 100, 300, fill = "blue")
canvas.move(id1, 200, 60)     # namiesto id1 ak sa pouzije 'all', tak sa premiestna vsetke tvary grafickej plochy
root.mainloop()

#==============================================================================
# ZMENA PARAMETROV TVARU
#==============================================================================
#
# funkcia canvas.itemconfig()
#
#    > slúži na zmenu ľubovoľných doplnkových parametrov nakresleného útvaru
#    > má tvar canvas.itemconfig(identifikátor, parametre)
#         - kde identifikátor je návratová hodnota príkazu kreslenia útvaru
#         - parametre sú ľubovoľné doplnkové parametre pre daný útvar
#------------------------------------------------------------------------------
# canvas.create_line()
#   	width= hrúbka obrysu
#   	fill= farba obrysu
# canvas.create_rectangle()
#   	width= hrúbka obrysu
#   	outline= farba obrysu
#   	fill= farba výplne
# canvas.create_oval()
#   	width= hrúbka obrysu
#   	outline= farba obrysu
#   	fill= farba výplne
# canvas.create_text()
#   	text= vypisovaný text
#   	font= písmo a veľkosť
#   	fill= farba textu
#   	angle= uhol otočenia
# canvas.create_polygon()
#   	width= hrúbka obrysu
#   	outline= farba obrysu
#   	fill= farba výplne
# canvas.create_image()
#   	image= obrázkový objekt
#------------------------------------------------------------------------------
from tkinter import *
root = Tk()
root.configure(bg = "black")
root.title("KRESLENIE TEXTU")
#------------------------------------------------------------------------------
canvas = Canvas(root, bg = "black", width = '600', height = '300') # defaultne nastavenie plochy
canvas.pack()                           # vykresli garficku plochu
id1 = canvas.create_line(25, 52, 120, 200, fill = "red")
id2 = canvas.create_line(60, 14, 100, 300, fill = "blue")
#------------------------------------------------------------------------------
canvas = Canvas(root, bg = "black", width = '600', height = '300') # defaultne nastavenie plochy
canvas.pack()
id1 = canvas.create_line(25, 52, 120, 200, fill = "red")
id2 = canvas.create_line(60, 14, 100, 300, fill = "blue")
canvas.itemconfig(id1, fill = "blue")  # zmena parametru farby ciary id1
canvas.itemconfig(id2, fill = "red")   # zmena parametru farby ciary id2
root.mainloop()

#==============================================================================
# ZMENA SURADNIC TVARU
#==============================================================================
# funkcia canvas.coords()
#
#     > slúži na zmenu všetkých súradníc nakresleného útvaru
#     > má tvar canvas.coords(identifikátor, postupnosť)
#         - kde identifikátor je návratová hodnota príkazu kreslenia útvaru
#         - postupnosť je ľubovoľná postupnosť súradníc, ktorá je vhodná pre daný útvar - táto postupnosť musí obsahovať párny počet čísel (celých alebo desatinných)
#------------------------------------------------------------------------------
from tkinter import *
root = Tk()
root.configure(bg = "black")
root.geometry("200x200")
root.title("ZMENA SURADNIC TVARU")
#------------------------------------------------------------------------------
canvas = Canvas(root, bg = "black", width = "200", height = "200" )
canvas.pack()
il1 = canvas.create_line(50, 120, 160, 124, fill = "blue")
canvas.itemconfig(il1, fill = "red")            # Zmena farby ciary
canvas.coords(il1, 80, 80, 40, 64, 65, 20)      # Zmena suradnic ciary
root.mainloop()

#==============================================================================#==============================================================================
# GENERATOR NAHODNYCH CISEL
#==============================================================================
#
# funkcia random.randint()
#
#     funkcia má dva parametre: hranice intervalu čísel
#     vyberie náhodnú hodnotu z tohto intervalu, pričom sa do výberu počítajú aj hraničné body intervalu
#------------------------------------------------------------------------------
# funkcia random.randrange()
#
#    > funkcia má 1, 2 alebo 3 parametre s rovnakým významom ako range()
#    > vyberie náhodnú hodnotu z tohto rozsahu
#    > napr. random.randrange(100), random.randrange(10, 100), random.randrange(10, 100, 5)
#------------------------------------------------------------------------------
# funkcia random.choice()
#
#    > funkcia má jeden parameter: ľubovoľnú postupnosť hodnôt
#    > vyberie náhodnú hodnotu z tejto postupnosti
#    > napr. random.choice(('red', 'blue', 'green'))
#------------------------------------------------------------------------------
import random
from tkinter import *
root = Tk()
root.configure(bg = "black")
root.geometry("600x600")
root.title("NAHODNE GENEROVANIE POLOZIEK/HODNOT")
#------------------------------------------------------------------------------
canvas = Canvas(root, bg = "black", width = "600", height = "600" )
canvas.pack()

for i in range(random.randint(10, 20)):                       # vyber nahodneho range z interval 10 <-> 20
    x = random.randrange(300)                                 # vyber nahodnej suradnice x v intervale 0 <-> 300
    y = random.randrange(400)                                 # vyber nahodnej suradnice y v intervale 0 <-> 400
    r = 10
    farba = random.choice(("red", "blue", "white"))           # vyber nahodnej polozky farby
    canvas.create_oval(x+r, y+r, x-r, y-r, fill = farba)      # vykreslenie kruznice a jej vyfarbenie
    print("i={} x={} y={}" .format(i, x, y))                  # vypis aktualnych hodnout v cykle
print("Pocet kruhov / i = ", i+1)
root.mainloop()


#==============================================================================
# PODRZANIE VYPOCTU
#==============================================================================
#
# funkcia canvas.after()
#
#    > funkcia má jeden číselný parameter: počet tisícin sekundy, na ktorý sa výpočet na tomto mieste pozdrží
#    > napr. canvas.after(500) pozdrží výpočet o 0,5 sekundy
#------------------------------------------------------------------------------
#
#   funkkcia canvas.update()
#         > zabezpecuje zobrazenie zmeny
#------------------------------------------------------------------------------
import random
from tkinter import *
root = Tk()
root.configure(bg = "black")
root.geometry("600x600")
root.title("NAHODNE GENEROVANIE POLOZIEK/HODNOT")
#------------------------------------------------------------------------------
canvas = Canvas(root, bg = "black", width = "600", height = "600" )
canvas.pack()
# obr = PhotoImage(file='Image\cf.png')
# canvas.create_image(800, 300, image = obr)
#
# for i in range(100):
#     canvas.move(1, -5, 0)
#     canvas.update()
#     canvas.after(100)


for i in range(random.randint(10, 20)):                       # vyber nahodneho range z interval 10 <-> 20
    x = random.randrange(300)                                 # vyber nahodnej suradnice x v intervale 0 <-> 300
    y = random.randrange(400)                                 # vyber nahodnej suradnice y v intervale 0 <-> 400
    r = 10
    obr = PhotoImage(file='Image\cf.png')                     # import obrazka
    canvas.create_image(x+r, y+r, image = obr)                # vykreslenie obrazka
    canvas.update()
    canvas.after(1000)                                        # podrzanie o cas 1000 = 1 sekunda
    print("i={} x={} y={}" .format(i, x, y))                  # vypis aktualnych hodnout v cykle

print("Pocet opakovani / i = ", i+1)
root.mainloop()

#==============================================================================
# MATEMATICKE FUNKCIE
#==============================================================================
# Modul math obsahuje množstvo užitočných matematických funkcií. Aby ste ich mohli používať,
# musíte najprv zadať príkaz:
#
#     import math
#
# Vymenujme niekoľko funkcií, ktoré asi využijeme v mnohých našich programoch:
#
#     math.sin() - goniometrická funkcia sin, pracuje v radiánoch a nie v stupňoch
#     math.cos() - goniometrická funkcia cos, pracuje v radiánoch a nie v stupňoch
#     math.tan() - goniometrická funkcia tangens, pracuje v radiánoch a nie v stupňoch
#     math.sqrt() - druhá odmocnina čísla
#     math.exp() - exponenciálna funkcia
#     math.log() - prirodzený logaritmus čísla
#
# Okrem týchto funkcií sú v tomto module definované aj dve užitočné konštanty:
#
#     math.pi - Ludolfovo číslo
#     math.e - základ prirodzených logaritmov
#------------------------------------------------------------------------------






















