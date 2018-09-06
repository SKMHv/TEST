# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 14:29:25 2017

@author: michal.hvila
http://howto.py.cz/cap04.htm
http://howto.py.cz/cap05.htm
"""
#==============================================================================
#body < 90 	je menšie ako
#body <= 50 	je menšie alebo rovné
#body == 50 	rovná sa
#body != 77 	nerovná sa
#body > 100 	je väčšie ako
#body >= 90 	je väčšie alebo rovné
#40 < body <= 50 	je väčšie ako ... a zároveň menšie alebo rovné ...
#a < b < c 	a je menšie ako b a zároveň je b menšie ako c
#==============================================================================
#PODMIENKY
#==============================================================================
def overenie_par(x):
    if x%2==0:
        print(x," je parne cislo")
    else:
        print(x," je neparne cislo")

x=int(input("Zadaj cislo: ")) 
overenie_par(x)                             #Out[x]:x je (ne)parne cislo
#-----------------------------
#==== if ====
import math
x=int(input("Zadaj cislo: "))
if x>=0:
    print("Odmocnina z ",x ," je ", math.sqrt(x))
   #print("Odmocnina z ",x ," je ", x**0,5)
print("Nevadi ide sa dalej.....")
#-----------------------------    
#==== vnorene podmienky ====
x=int(input("Zadaj cislo: "))
if x > 0:
    if x <10:
        print(x," - je kladna jednocislica")   #Out[x]: x  - je kladna jednocislica
# TO ISTE:
if x>0 and x<10: 
    print(x," - je kladna jednocislica")       #Out[x]: x  - je kladna jednocislica
# TO ISTE:    
if 0<x<10:
    print(x," - je kladna jednocislica")       #Out[x]: x  - je kladna jednocislica

#------------------------------------------------------------------------------
# Skúsme pridať ešte jednu podmienku: všetky bodky v spodnej polovici (y > 150)
# budú zelené, takže rozdelenie na červené a modré bude len v hornej polovici. Jedno z možných riešení:

import tkinter
import random

canvas = tkinter.Canvas(bg='white', width=300, height=300)
canvas.pack()

for i in range(1000):
    x = random.randrange(300)
    y = random.randrange(300)
    if y < 150:
        if x < 150:
            farba = 'red'
        else:
            farba = 'blue'
    else:
        farba = 'green'
    canvas.create_oval(x-5, y-5, x+5, y+5, fill=farba, outline='')




#-----------------------------    
#==== if else ====    
x = int(input("Zadaj pocet bodov:  "))
if x>=90:
    print("Tvoja znamka je A")
else:
    if x>=80:
        print("Tvoja znamka je B")
    else:
        if x>=70:
            print("Tvoja znamka je C")
        else:
            if x>=50:
                print("Tvoja znamka je D")
            else:
                if x>=30:
                    print("Tvoja znamka je E")
                else:
                    print("Tvoja znamka je FX")
#-----------------------------
#==== elif ====
x = int(input("Zadaj pocet bodov:  "))
if x>=90:
    print("Tvoja znamka je A")
elif x>=80:
    print("Tvoja znamka je B")
elif x>=70:
    print("Tvoja znamka je C")
elif x>=50:
    print("Tvoja znamka je D")
elif x>=30:
    print("Tvoja znamka je E")
else:
    print("Tvoja znamka je FX")
#-----------------------------
#==== intervaly ====
x = int(input("Zadaj pocet bodov:  "))
if x>=90:
    print("Tvoja znamka je A")
if 80<=x<90: 
    print("Tvoja znamka je B")
if 70<=x<80:    
    print("Tvoja znamka je C")
if 50<=x<70:
    print("Tvoja znamka je D")
if 50<=x<30:
    print("Tvoja znamka je E")
if x<30:
    print("Tvoja znamka je FX")

#==============================================================================
#FUNKCIE S PODMIENKAMI
#==============================================================================
#-----------------------------
#==== RETURN ====
x=int(input("Zadaj x: "))

def absotutna_hodnota(x):
    if x<0:
        return print(-x)
    else:
        return print(x)

absotutna_hodnota(x)
# TO ISTE: 
def absotutna_hodnota(x):
    if x<0:
        return print(-x)
    return print(x)

# Tato funkicia nema osetrenu cestu podmineky so vstupom x==0, 
# v tomto pripade funkcia skonci bez toho aby narazila na return 
def absotutna_hodnota(x):
    if x<0:
        return print(-x)
    elif x>0:
        return print(x)

#==============================================================================
#BULOVSKE FUNKCIE
#==============================================================================

bool(1)       #Out[X]: True
bool(0)       #Out[X]: False
bool("No !")  #Out[X]: True
bool("")      #Out[X]: False
bool("3.14159")     #Out[X]: True
#-----------------------------
# Toto znamená, že v prípadoch, keď Python očakáva logickú hodnotu (napr. v príkaze if,
# alebo v operáciách and, or, not) môžeme uvádzať aj hodnoty iných typov. Napr.
pocet = int(input('zadaj:'))
if pocet:
    print('pocet je rôzny od 0')
else:
    print('pocet je 0')
meno = input('zadaj:')
if meno:
    print('meno nie je prázdny reťazec')
else:
    print('meno je prázdny reťazec')
#-----------------------------
x = int(input("X = "))
y = int(input("Y = "))
def je_delitelne(x,y):
    if x % y == 0:
        return True
    else:
        return False

if je_delitelne(x,y):
    print(">>>",x,"je delitelne", y)
else:
    print(">>>",x,"nie je delitelne", y)
#-----------------------------
# Logické operácie majú v skutočnosti trochu rozšírenú interpretáciu:
#
# operácia: prvý and druhý
#
#     ak prvý nie je False, tak
#             výsledkom je druhý
#
#     inak (teda prvý je False)
#             výsledkom je prvý
#
# operácia: prvý or druhý
#
#     ak prvý nie je False, tak
#             výsledkom je prvý
#
#     inak (teda prvý je False)
#             výsledkom je druhý
#
# operácia: not prvý
#
#     ak prvý nie je False, tak
#             výsledkom je False
#
#     inak
#             výsledkom je True
#
# Podmienený príkaz sa často používa pri náhodnom rozhodovaní.
# Napr. hádžeme mincou (náhodné hodnoty 0 a 1) a ak padne 1, kreslíme náhodnú kružnicu, inak náhodný štvorec. Toto opakujeme 10-krát:

from tkinter import *
import random
root = Tk()
canvas = Canvas(root,bg='white', width=300, height=300)
canvas.pack()

for i in range(10):
    x = random.randrange(300)
    y = random.randrange(300)
    a = random.randrange(5, 50)

    if random.randrange(2):               # t.j. random.randrange(2) != 0
        canvas.create_oval(x-a, y-a, x+a, y+a)
    else:
        canvas.create_rectangle(x-a, y-a, x+a, y+a)

mainloop()

#-----------------------------
# Túto ideu môžeme využiť aj pre
# takúto úlohu: vygenerujte 1000 farebných štvorčekov - modré a červené, pričom ich pomer je 1:50,
# t.j. na 50 červených štvorčekov pripadne približne 1 modrý:
from tkinter import *
import random

root = Tk()
canvas = Canvas(root,bg='white', width=300, height=300)
canvas.pack()
n = 0
m = 0
for i in range(1000):
    x = random.randrange(300)
    y = random.randrange(300)
    if random.randrange(50):             # t.j. random.randrange(50) != 0
        farba = 'red'
        n += 1
    else:
        farba = 'blue'
        m += 1
    canvas.create_rectangle(x-5, y-5, x+5, y+5, fill=farba, outline='')
print("n={}, m={}" .format(n, m))      # n=979, m=21
mainloop()

#-----------------------------
# Ďalší príklad zisťuje, akých deliteľov má zadané číslo:

cislo = int(input('Zadaj číslo: '))
pocet = 0
print('delitele:', end=' ')
for delitel in range(1, cislo + 1):
    if cislo % delitel == 0:
        pocet += 1
        print(delitel, end=' ')
print()
print('počet deliteľov:', pocet)

#-----------------------------
# Malou modifikáciou tejto úlohy vieme urobiť ďalšie dva programy. Prvý zisťuje, či je číslo prvočíslo:

cislo = int(input('Zadaj číslo: '))
pocet = 0
for delitel in range(1, cislo+1):
    if cislo % delitel == 0:
        pocet += 1
if pocet == 2:
    print(cislo, 'je prvočíslo')
else:
    print(cislo, 'nie je prvočíslo')

#-----------------------------
# Druhý program zisťuje, či je nejaké číslo dokonalé,
# t.j. súčet všetkých deliteľov menších ako samotné číslo sa rovná samotnému číslu. Na základe tohto
# nájde (postupne preverí) všetky dokonalé čísla do 10000:
print('dokonalé čísla do 10000 sú', end=' ')
for cislo in range(1,10001):
    sucet = 0
    for delitel in range(1, cislo):
        if cislo % delitel == 0:
            sucet += delitel
    if sucet == cislo:
        print(cislo, end=' ')
print()
print('=== viac ich už nie je ===')



    
#==============================================================================
#ROZVOJ FUNKCIE
#==============================================================================
#Priklad - vypocet vzdialenosti dvoch bodov podla suradnic (x1,y1) a (x2,y2)
#------------------------------------------------------------------------------
# Postupne skladanie 
#-------------------
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    print("x2 - x1 = ", dx)
    print("y2 - y1 = ", dy)
    suc_mocnin = dx**2 + dy**2
    print("sucet mocnin = ", suc_mocnin)
    import math
    vysledok = math.sqrt(suc_mocnin)
    print("Vysledok je = ", vysledok)

    return 0.0

distance(1,2,4,6)

# po overeni funkcnosti redukujem 
#-------------------
import math
def distance(x1, y1, x2, y2):
    vysledok = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    print("Vysledok je = ", vysledok)
    return 0.0

distance(1,2,4,6)

#==============================================================================
#SCHEMA ZASOBNIKA
#==============================================================================

def print_twice(bruce):
    print(bruce, bruce) 
#    print(cat)                      #NameError: name 'cat' is not defined

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)
    
chant1 = "Pie Jesu domine, "
chant2 = "Dona eis requim."
cat_twice(chant1, chant2)

#Traceback (innermost last):
#  File "test2.py", line 11, in <module>
#    cat_twice(chant1, chant2)
#  File "test2.py", line 7, in catTwice
#    print_twice(cat)
#  File "test2.py", line 3, in printTwice
#    print(cat)
#NameError: global name 'cat' is not defined

#==============================================================================
#TESTOVANIE S 'DOCTESTOM'
#==============================================================================

def is_divisible_by_2_or_5(n):
    """
    >>> is_divisible_by_2_or_5(8)
    True
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod()

#******************************************************************
#File "****.py", line 3, in __main__.is_divisible_by_2_or_5
#Failed example:
#    is_divisible_by_2_or_5(8)
#Expected:
#    True
#Got nothing
#******************************************************************
#1 items had failures:
#   1 of   1 in __main__.is_divisible_by_2_or_5
#***Test Failed*** 1 failures.
#==============================================================================


#==============================================================================
#PODMIENKA WHILE
#==============================================================================

def countdown(n):
    '''
    5

    16
    8
    4
    2
    1
    '''
    print(round(n))
    print("--------------------")
    while n != 1:               #podmienka pre while
       if n%2 == 0:             #ak je parna 
           n = n/2
           print(round(n))
       else:                    #ak nie je parna 
           n=n*3+1
           print(round(n))
           
countdown(5)

#==============================================================================
#POCITANIE CISLIC
#==============================================================================
def num_digits(n):
    count = 0 
    while n:                             # n != 0:
        digit = n%10                     # digit=1002%10 (2) 100%10 (0) 10%10 (0) 1%10 (1)
        if digit == 0 or digit == 5: 
            print("digit = ", digit)     # digit =  0, digit =  0                               
            print("count = ", count, "+1")
            count = count+1              #count=0+1
            print("= ", count)
        n = n//10                        # n=1002//10 (100) 100//10 (10) 10//10 (1) 1//10
        
    return print("----------------\nCOUNT => ", count)   # pocet 0 a 5 z if

num_digits(1002)                           #----------------
                                           #COUNT =>  2
#==============================================================================
#ZKRACOVANIE PRIRADENIA
#==============================================================================                                           
# Skratky +=, -=, *=, /=, a %= :
#---------------------------------

n = 2
print(n)        # 2
n += 3          # n = 2 + 3
print(n)        # 5
n *= 2          # n = 5 * 2
print(n)        # 10
n -= 4          # n = 10 - 4
print(n)        # 6
n /= 2          # n = 6 / 2
print(n)        # 3
n %= 2          # n = 3-(3/2)
print(n)

#==============================================================================
#TABELARNE DATA
#============================================================================== 

x = 1
while x < 13:
    print("2**", x, '\t', 2**x)
    x += 1 
    
#2** 1    2
#2** 2    4
#2** 3    8
#2** 4    16
#2** 5    32
#2** 6    64
#2** 7    128
#2** 8    256
#2** 9    512
#2** 10   1024
#2** 11   2048
#2** 12   4096
          
#==============================================================================
#DVOJROZMERNE TABULKY
#==============================================================================

def print_multiples(n):
    i = 1
    while i <= 6:
        print(n*i, "\t", end="")
        i += 1
    print()
    
print_multiples(3)
#3       6       9       12      15      18  


#==============================================================================
#ZAPUZDRENIE A ZOVSEOBECNENIE
#==============================================================================

def print_multiples(n):
    i = 1
    while i <= 6:
        print(n*i, "\t", end="")
        i += 1
    print()
    
print_multiples(3)
#3       6       9       12      15      18  
print("--- print_multiples(i) v v print_print_mult_tables() ----------------------")
def print_print_mult_tables():
    i = 1
    while i <= 6:
        print_multiples(i)
        i += 1

print_print_mult_tables()
    
#1       2       3       4       5       6       
#2       4       6       8       10      12      
#3       6       9       12      15      18      
#4       8       12      16      20      24      
#5       10      15      20      25      30      
#6       12      18      24      30      36  

#==============================================================================
#LOKALNE PREMENNE PODRUHE
#==============================================================================

def print_multiples(n,high):
    i = 1
    while i <= high:
        print(n*i, "\t", end="")
        i += 1
    print()
    
print("--- print_multiples(n,hight) v print_print_mult_tables(high) -----------------")
def print_print_mult_tables(high):
    i = 1
    while i <= high:
        print_multiples(i,high)
        i += 1

print_print_mult_tables(7)

#--- print_multiples(n,hight) v print_print_mult_tables(high) -----------------
#1       2       3       4       5       6       7       
#2       4       6       8       10      12      14      
#3       6       9       12      15      18      21      
#4       8       12      16      20      24      28      
#5       10      15      20      25      30      35      
#6       12      18      24      30      36      42      
#7       14      21      28      35      42      49 

print("--- zmena print_multiples(i,high) na print_multiples(i,i)--------------------")
def print_print_mult_tables(high):
    i = 1
    while i <= high:
        print_multiples(i,high)
        i += 1

print_print_mult_tables(7)

#--- zmena print_multiples(i,high) na print_multiples(i,i)--------------------
#1       
#2       4       
#3       6       9       
#4       8       12      16      
#5       10      15      20      25      
#6       12      18      24      30      36      
#7       14      21      28      35      42      49 


#==============================================================================
#NEWTONOVA METODA
#==============================================================================
def sqrt(n):                                         # n = 25
    approx = n/2.0                                   # approx = 12.5
    better = (approx + n/approx)/2.0                 # better = 7.25
    while better != approx:
        approx = better                              # approx = 7.25
        better = (approx + n/approx)/2.0             # better = 5.349137931034482
        print("approx = ", approx)         
    return approx 
           
sqrt(25)
#approx =  7.25
#approx =  5.349137931034482
#approx =  5.011394106532552
#approx =  5.000012953048684
#approx =  5.000000000016778
#approx =  5.0

#==============================================================================
#ALGORITMY
#==============================================================================
# sucin cisla n a 9 algoritmom
n = int(input("Zadaj cislo n = "))              # n = 2
def sucin_devet(n):
    prva_cast = n - 1                           # 2 - 1 = 1 
    druha_cast = 10 -n                          # 10 - 2 = 8
    sucin = str(prva_cast) + str(druha_cast)    # 18
    print(sucin)                                # >>>18

sucin_devet(n)

#==============================================================================
#REKURZIA
#==============================================================================
# volanie funkcie samej v sebe
def countDown(n):
    if n < 1:       
        return
    print(n)
    countDown(n-1)

