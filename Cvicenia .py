# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 10:22:30 2017

@author: michal.hvila
"""
"""
#------------------------------------------------------------------------------
#==============================================================================
#2.14
#==============================================================================
#------------------------------------------------------------------------------
"""
print(7+1)                      #Out[x]: 8
print(7.1,"totok",7/2.0,5+4)    #Out[x]: print(7.1,"totok",7/2.0,5+4)
# 2 - All work and no play makes Jack a dull boy
a = 'All' 
b = 'work' 
c = 'and' 
d = 'play'
e = 'makes'
f = 'jack'
g = 'a' 
h = 'dull'
i = 'boy'
print(a,b,c,d,e,f,g,h,i)
#4 - (jméno 'houby není definováno') Jménu houbeles přiřaďte takovou hodnotu, aby houby + 4 bylo 10.
#------------------------------------------------------------------------------ 
houbeles = 10
houby = houbeles - 4  
print(houby + 4)
#5 - program pro výpočet výsledné hodnoty A počátečního vkladu P //a = 22196.4
#------------------------------------------------------------------------------
p = 1000
r = 0.08 # 8%
n = 12
t = 10

a = float(p*(1+r/n)**(n*t))
b = float(p*((1+r/n)**(n*t)))
print(a," = ",b)               #Out[x]: 2219.640234544711 = 2219.640234544711

"""
#------------------------------------------------------------------------------
#6 - Odjíždíte na báječnou dovolenou ve středu, to je ve 3. dnu v týdnu. 
#    Vrátíte se po 137 nocích. Napište program, který se zeptá na pořadové číslo dne vašeho odjezdu
#    ,délku pobytu a vrátí vám pořadové číslo dne, kdy se vrátíte. Bude to neděle? 
#------------------------------------------------------------------------------
"""

den_odchod = int(input("Zadaj poradovy den v tydni pre odchod  = "))
dlzka = int(input("Zadaj dlzku pobytu = "))
n = dlzka % 7 + den_odchod
if n==7: print("Den navratu je - Nedela")
elif n==6: print("Den navratu je - Sobota")
elif n==5: print("Den navratu je - Piatok")
elif n==4: print("Den navratu je - Stvrtok")
elif n==3: print("Den navratu je - Streda")
elif n==2: print("Den navratu je - Utorok")
else: print("Den navratu je - Pondelok")

"""
#==============================================================================
#3.13
#==============================================================================
#1.Zabalte následující kód do funkce:  compare(x,y):
#   if x < y :
#     print(x, "je menší než", y)
#   elif x > y :
#     print(x, "je větší než", y)
#   else: 
#     print(x, "a", y "jsou stejné")
#
# Importujte si ji do IPP a volejte ji třikrát, s prvním argumentem menším, 
# větším a stejným než / jako druhý argument. 
#------------------------------------------------------------------------------
"""
import sys
sys.path.append('d:/INSTAL/WINPYTHON/WinPython-64bit-3.5.3.0Qt5/notebooks')

import Import
Import.compare(1, 2)     #Out[x]: 1 je menší než 2
Import.compare(2, 1)     #Out[x]: 2 je větší než 1
Import.compare(1, 1)     #Out[x]: 1 a 1 jsou stejné

"""
#------------------------------------------------------------------------------
#2. S použitím textového editoru vytvořte skript test3.py  (Import.py)
# Napište funkci jménem nine_lines, která použije funkci tri_riadky 
# k vytištění devíti prázdných řádek. Nyní přidejte fci clear_screen,
# která vytiskne 25 prázdných řádek. Poslední řádkou skriptu by mělo být
# volání fce clear_screen.
#------------------------------------------------------------------------------
"""
def one_riadok():
    print()
    
def tri_riadky():
    one_riadok()
    one_riadok()
    one_riadok()
                      
def devet_riadky():
    tri_riadky()
    tri_riadky()
    tri_riadky()
def clear_screen():
    devet_riadky()
    tri_riadky()
    tri_riadky()
    devet_riadky()
    one_riadok()
    
one_riadok()
print("1...")
tri_riadky()
print("3...")
devet_riadky()
print("9...")
clear_screen()
print("25..")  

"""
#------------------------------------------------------------------------------
#3. Poslední řádek programu test3.py přesuňte úplně nahoru,
# takže se volání funkcíe clear_screen dostane před jeji definici.
# Spusťte program a sledujte, jaké chybové hlášení dostanete.
# Jaké z toho plyne pravidlo? 
#>>> Ako prve sa vytlaci 25 riadkov a dalej to postupuje podla poradia volani funkcii
#------------------------------------------------------------------------------
"""
clear_screen()
print("25..")  

def one_riadok():
    print()
    
def tri_riadky():
    one_riadok()
    one_riadok()
    one_riadok()
                         
def devet_riadky():
    tri_riadky()
    tri_riadky()
    tri_riadky()
def clear_screen():
    devet_riadky()
    tri_riadky()
    tri_riadky()
    devet_riadky()
    one_riadok()   

one_riadok()
print("1...")
tri_riadky()
print("3...")
devet_riadky()
print("9...")

"""
#------------------------------------------------------------------------------
#4. V chodící verzi test3.py přesuňte definici novy_riadok za definici tri_riadky.
# Sledujte chování spuštěného programu. Nyní přesuňte definici novy_riadok za volání fce tri_riadky.
# Posuďte souvislost s pravidlem z předchozího cvičení. 
#>>> Nezmeni to tlacovy vystup
#------------------------------------------------------------------------------
"""
def tri_riadky():
    one_riadok()
    one_riadok()
    one_riadok()

def one_riadok():
    print()
    
                      
def devet_riadky():
    tri_riadky()
    tri_riadky()
    tri_riadky()
def clear_screen():
    devet_riadky()
    tri_riadky()
    tri_riadky()
    devet_riadky()
    one_riadok()
    
one_riadok()
print("1...")
tri_riadky()
print("3...")
devet_riadky()
print("9...")
clear_screen()
print("25..")     

"""
#------------------------------------------------------------------------------
#5. Doplňte tělo definované funkce cat_n_times tak, aby n krát vytiskla řetězec s
#  def cat_n_times(s,n):
#     <zde zapište svůj kód>
#------------------------------------------------------------------------------
"""
import sys
sys.path.append('d:/INSTAL/WINPYTHON/WinPython-64bit-3.5.3.0Qt5/notebooks')

import Import
Import.cat_n_times('Spam', 7)     #Out[x]: SpamSpamSpamSpamSpamSpamSpam

"""
#==============================================================================
#4.10
#==============================================================================
# Všechna cvičení budou postupně přidávána do souboru se jménem ch05.py. 
# Na konec totoho skriptu se umístí následující kód:
#
#  if __name__ == '__main__':
#      import doctest
#      doctest.testmod()
#
# Po zapsání každého cvičení spustíme skipt, abychom se přesvědčili,
# že naše nová funkce projde testem.
#------------------------------------------------------------------------------
#1. Napište funkci compare, která vrací 1 pro a>b, 0 pro a==b a -1 pro a<b. 
#------------------------------------------------------------------------------
"""
print()
print(">>>(1).----------------------------------------------------------------")
print()
def compare(a,b):
    """
    >>> compare(5,4)
    1
    >>> compare(7,7)
    0
    >>> compare(2,3)
    -1
    """ 
    if a>b:
        print(1)
    elif a==b:
        print(0)
    else:
        print(-1)
        
#a = int(input("a ="))
#b = int(input("b ="))
compare(5,4)      # 1       
compare(7,7)      # 0
compare(2,3)      # -1

"""
#------------------------------------------------------------------------------
#2. Použijte přírůstkový rozvoj k vytvoření funkce hypotenuse, 
#   která vrací délku přepony pravoúhlého trojúhelníka pro zadané délky odvěsen.
#------------------------------------------------------------------------------
"""
print()
print(">>>(2).----------------------------------------------------------------")
print()
def hypotenuse (a,b):
    """
    >>> hypotenuse(3,4)
    5.0
    >>> hypotenuse(12,5)
    13.0
    >>> hypotenuse(7,24)
    25.0
    """
    import math
    c = math.sqrt(a**2 + b**2)
    print(c)

hypotenuse(3,4)
hypotenuse(12,5)
hypotenuse(7,24)

"""
#------------------------------------------------------------------------------
#3. Napište funkci slope(x1,y1,x2,y2), která vrací úhel sklonu přímky
#   procházející body (x1,y1) a (x2,y2). Funkce musí vyhovět následujícím testům: 
#    
#------------------------------------------------------------------------------
"""
print()
print(">>>(3).----------------------------------------------------------------")
print()
def slope (x1,y1,x2,y2):
    """
    >>> slope(5,3,4,2)
    1.0
    >>> slope(1,2,3,2)
    0.0
    >>> slope(1,4,1,2)
    kolmica k ose 'x'           
    >>> slope(2,4,1,2)
    2.0
    """
    import math
    dx = x2 - x1
    dy = y2 - y1
    if dx != 0:        
        uhol_rad = math.atan((dy)/(dx))   # uhol priamky
        smernica = (dy)/(dx)   # smernica
        uhol_stup = uhol_rad * 57,296 #uhol(radian) * 57,296
        print(">> Smernica priamky ((y2-y1)/(x2-x1)) = ",smernica)
        print(">> Uhol smernice-priamky k osi x ((y2-y1)/(x2-x1)) = ",uhol_stup ,"st.")        
    else:
        print("(x2-x1) = 0 => Kolmica k ose 'x'")                                  
    print()


    
slope(5,3,4,2)
slope(1,2,3,2)
slope(1,4,1,2)
slope(2,4,1,2)

"""
#------------------------------------------------------------------------------
#4. Napište funkci is_even(n), která přijme celé číslo jako argument
# a vrací True, je-li číslo sudé a False, je-li liché. Vytvořte vlastní doctesty.
#    
#------------------------------------------------------------------------------
"""

def is_even(n):
#    """
#    >>> Zadaj cislo n = 5
#    >>> 5 - Je neparne cislo
#    """
    
    if n % 2 == 0:
        return False
    else:
        return True
    

n = int(input("Zadaj cislo n = "))
print()
if is_even(n):
    print(n, "- Je neparne cislo")
else:
    print(n, "- je parne cislo")
    
"""
#------------------------------------------------------------------------------
#5. NNyní napište funkci is_odd(n), která vrací True, je-li n liché a False, 
# je-li liché. Upravte fci tak, že k určení sudosti / lichosti volá fci is_even. 
# Vytvořte vlastní doctesty.
# 
#------------------------------------------------------------------------------
"""

n = 0
while True:                                   # Overenie vstupu chybovou hlaskou 
    try:
        n = int(input("Zadaj cislo n = "))
    except ValueError:
        print(">>> n -> NOK = Nie je integer")
        continue
    
    else:
        print(">>> n -> OK = Je integer")
        break
    
print("<------------------------------------>")
print("<------------ is_even(n) ------------>")  
def is_even(n):                         
        if n % 2 == 0:
            return False
        else:
            return True
        
if is_even(n):
    print(">>> ", n, "- Je neparne cislo")
else:
    print(">>> ", n, "- je parne cislo")
    
print("<-----------NOT is_even(n)----------->")

def is_odd(n):                                #funkcia pre negovanie funkcie is_even(n)
        if is_even(n) == False:
            return True
        else:
            return False

if is_odd(n):
    print(">>> ", n, "- Je parne cislo")
else:
    print(">>> ", n, "- je neparne cislo")
    
    
"""
#------------------------------------------------------------------------------
#6. Napište funkci is_factor(f,n) se dvěma parametry f a n, 
# která vrátí True, je-li f dělitelem n a False, není-li.   
# 
#------------------------------------------------------------------------------    
"""
def is_factor(f,n):
    """
    >>> is_factor(3,12)
    True = 3 je delitelom 12
    >>> is_factor(5,12)
    False = 5 nieje delitelom 12
    >>> is_factor(2,14)
    True = 2 je delitelom 14
    """ 
    if n % f == 0:
        return True
    else:
        return False
    

if is_factor(3,12):
    print("True = 3 je delitelom 12")
else:
    print("False = 3 nieje delitelom 12")
    
if is_factor(5,12):
    print("True = 5 je delitelom 12")
else:
    print("False = 5 nieje delitelom 12")

if is_factor(2,14):
    print("True = 2 je delitelom 14")
else:
    print("False = 2 nieje delitelom 14")

"""
#------------------------------------------------------------------------------
#7. Napište funkci is_multiple(m,n) se dvěma parametry m a n, která vrátí True,
# je-li m násobkem n a False, není-li. 
#
#------------------------------------------------------------------------------
"""
def is_multiple(m,n):
    """
    >>> is_multiple(12,3)
    True
    >>> is_multiple(12,4)
    True
    >>> is_multiple(12,5)
    False
    """
    if m % n == 0:
        return True
    else:
        return False

if is_multiple(12,3):
    print("True")
else:
        print("False")
if is_multiple(12,4):
    print("True")
else:
    print("False")
if is_multiple(12,5):
    print("True")
else:
    print("False")
    
"""
#------------------------------------------------------------------------------
#8. Napište tělo funkce f2c(t), která převede teplotu ve stupních Fahenheitových
# na stupně Celsiovy a vrátí ji jako celé číslo. Použijete vestavěnou fci 
#round(n). 
#Informaci o této funkci získáte zadáním >>> round.__doc__ v konzole Pythonu. 
#
#------------------------------------------------------------------------------
"""
t = 0
while True:                                                     #Fahrenheit iba integer
    try:
        t = int(input("Zadaj teplotu vo fahrenheitoch -->"))
    except ValueError:
        print("NOK - Teplota nie je INTEGER")
        continue
    else:
        break
        
    
def f2c(t):
        stupen = (t - 32) / 1.8000
        print(t, "F" "=" ,stupen ,"℃ (" ,round(stupen,3), "℃) (" ,round(stupen), "℃)")  #round(n,x)


f2c(t)  

"""
#------------------------------------------------------------------------------
#9. Napište funkci c2f(t), která převede teplotu ve stupních Celsiových na 
# stupně Fahrenheitovy. 
#
#------------------------------------------------------------------------------
"""
t = 0
while True:
    try:
        t = float(input("Zadaj teplotu v ℃ -->"))
    except ValueError:
        print("NOK - Teplota nie je FLOAT")
        continue
    else:
        break
def c2f(t):
    fahrenheit =  t * 1.8000 + 32
    print(t, "℃" "=" ,fahrenheit ,"F (" ,round(fahrenheit,3), "F) (" ,round(fahrenheit), "F)")  #round(n,x)
       
c2f(t)

#if __name__ == '__main__':
#    import doctest
#    doctest.testmod()

"""
#==============================================================================
#5.15
#==============================================================================
# 1.  Napište jediný řetězec, který  
# stvori
# tento 
# vystup
#------------------------------------------------------------------------------
"""
print("------------------------------ 1 -------------------------------------")
print("stvori \ntent \nvystup")

"""
#------------------------------------------------------------------------------
# 2. Přidejte volání funkce print k fci sqrt definované v odstavci 6.11 tak, 
# že vytiskne better ve smyčce po každé aproximaci. Volejte upravenou funkci
# pro argument 25 a zapište výsledky.
#------------------------------------------------------------------------------
"""
print("------------------------------ 2 -------------------------------------")
def sqrt(n):                                         # n = 25
    approx = n/2.0                                   # approx = 12.5
    better = (approx + n/approx)/2.0                 # better = 7.25
    while better != approx:
        print("better = ", better)
        approx = better                              # approx = 7.25
        better = (approx + n/approx)/2.0             # better = 5.349137931034482
        print("approx = ", approx)         
    return approx 
           
sqrt(25)

"""
#------------------------------------------------------------------------------
# 4. Napište funkci print_triangular_numbers(n), která vytiskne součet 
# prvních n členů aritmetické posloupnosti 1, 3, 6, 10, ... (triangular numbers). 
# Voláním fce dostaneme následující výstup:
#     1     1
#     2     3
#     3     6
#     4     10
#     5     15
#------------------------------------------------------------------------------
"""
print("------------------------------ 4 -------------------------------------")
# clen_n = n*(n+1) / 2

n = int(input("Zadaj pocet prvych n clenov --> "))

def print_triangular_numbers(n):
    i = 1
    clen = 0 
    while i<=n:
        clen= i + clen 
        print(i, "\t", clen)
        i+=1
    print()

print_triangular_numbers(n)

"""
#------------------------------------------------------------------------------
# 5.Napište funkci is_prime, která vyhodnotí zadané celé číslo a vrátí True pro
# argument, který je prvočíslem a False pro argument, který provočíslem není. 
# Při vývoji funkce používejte "doctesty". 
#------------------------------------------------------------------------------
"""
print("------------------------------ 5 -------------------------------------")

n=0
while True:                                                     #Fahrenheit iba integer
    try:
        n = int(input("Zadaj cele cislo -->"))
    except ValueError:
        print("Zadane cislo nie je INTEGER")
        continue
    else:
        break
        
def is_prime(n):
   """

   Vrati hodnotu True ak je argument prvocislom.

   """

   n = abs(n)                                       # n = abs(6)

   for i in range(2,n-1):                            
      if n % i == 0:                                # 6%2 == 0,
          return False
   return True


if is_prime(4):
    print("True - je prvocislo")
else:
    print("False - nie je prvocislo")

"""
#------------------------------------------------------------------------------
# 6.
# Co vrátí fce num_digits(0) (viz 6.3)? Upravte ji tak, aby pro tento případ 
# vrátila 1. Proč volání num_digits(-24) skončí nekonečnou smyčkou? (Nápověda: -1/10 
# se vyhodnotí jako -1. ) Upravte num_digits tak, aby pracovala správně pro 
# jakoukoli celočíselnou hodnotu.
#------------------------------------------------------------------------------
"""
print("------------------------------ 6 -------------------------------------")

def num_digits(n):
    count = 0 
    while n:        # totéž jako while n != 0:
        count = count+1
        n = n//10    # celočíselné dělení
    return count

"""
#------------------------------------------------------------------------------
# 9.
# Napište funkci sum_of_squares_of_digits, která spočítá součet čtverců číslic 
# zadaného celého čísla. Například, sum_of_squares_of_digits(72) by mělo 
# vrátit 53, protože 7** + 2** == 49 + 4 == 53. 
#------------------------------------------------------------------------------
"""
print("------------------------------ 9 -------------------------------------")
n = 0
while True:
    try: 
        n = int(input("Zadaj cele cislo ---> "))
    except ValueError:
        print("Cislo nie je INT a preto ...")
        continue
    else:
        break


def sum_of_squares_of_digits(n):
    """
      >>> sum_of_squares_of_digits(72)
      53

    """
    sum = 0
    while n:
        digit = n % 10    # digit = 72%10 == 2, 7%10 == 7
        sum += digit**2   # sum = 0+2**2 == 4, 4+7**2 == 53
        n //= 10           # n = 72//10 = 7, 7//10 == 0
        
    return print(int(sum))

sum_of_squares_of_digits(n)
"""
#==============================================================================
# ********** http://python.input.sk/02.html#znakove-retazce
# ********** 2.3. Cvičenie
#==============================================================================
# 1. 
# Napíšte skript, ktorý prečíta rozmery bazénu v metroch a vypočíta množstvo 
# vody v litroch, ktoré potrebujeme na zaplnenie tohto bazéna
#------------------------------------------------------------------------------
"""
print("------------------------------ 1 -------------------------------------")
while True:
    try:
        a = float(input("Zadaj 1. rozmer bazena v (m):"))  
        b = float(input("Zadaj 2. rozmer bazena v (m):"))     
        c = float(input("Zadaj 2. rozmer bazena v (m):"))
    except ValueError:
        print("ZADAL SI NESPRAVNY ROZMER \n   ***ZADAJ NANOVO***")
        continue
    else:
        break
    
v = round(a * b * c * 1000)
print("\n POCET LITROV = ", v)

"""
#------------------------------------------------------------------------------
# 2. 
# Napíšte skript, ktorý prečíta celé číslo n a reťazec a vytvorí nový reťazec,
# ktorý po vypísaní vytvorí tabuľku n riadkov po n reťazcov. Využite znaky '\n'
# a ' '. Nepoužite cyklus.
#------------------------------------------------------------------------------
"""
print("------------------------------ 2 -------------------------------------")
n = 5
retazec = "ahoj" + " "
riadok = 5 * retazec + "\n"
print(5 * riadok)

"""
#------------------------------------------------------------------------------
# 3. 
# Napíšte skript, ktorý prečíta znakový reťazec a potom postupne z tohto 
# reťazca vypíše do každého riadka jedno písmeno a to toľkokrát, 
# koľké je to písmeno.
#------------------------------------------------------------------------------
"""
print("------------------------------ 3 -------------------------------------")
while True:
    try:        
        slovo = input("zadaj slovo .... ")
    except ValueError:
        continue
    else:
        break
    
n = 1
for i in slovo:
    print(i * n)
    n += 1
"""
#------------------------------------------------------------------------------
# 4. 
# pre čísla od 11 do 20 vypísať ich druhé aj tretie mocniny
# v tvare (11,121,1331) = každé do jedného riadka. Použite metódu format().
# (11,121,1331)
# (12,144,1728)
#------------------------------------------------------------------------------
"""
print("------------------------------ 4 -------------------------------------")

i = 0
for i in range(int(input("Zadaj cislo od ...: ")) , int(input("Zadaj cislo do ...: ")) + 1):  
    print("{:2} {:3} {:4}" .format(i, i*i , i*i*i))    
print()    
"""
#------------------------------------------------------------------------------
# 5. Napíšte skript, ktorý prečíta jedno celé číslo n a dva rôzne znakové 
# reťazce. Potom do n riadkov postupne strieda vypisovanie týchto dvoch reťazcov.
# Dajte pozor na nepárne n. Možno využijete priraďovací príkaz, ktorý vymieňa 
# obsah dvoch premenných.
#
#    zadaj pocet: 5
#    prvy text: programujem v Pythone
#    druhy text: som na matfyze
#    
#    programujem v Pythone
#    som na matfyze
#    programujem v Pythone
#    som na matfyze
#    programujem v Pythone  
#------------------------------------------------------------------------------
"""
print("------------------------------ 5 -------------------------------------")
n = 0
while True:
    try:
        n = int(input("Zadaj pocet .... "))
        print("*")
    except ValueError:
        print("Zadane cislo nie je hodnoty int(). ZADAJ NANOVO >>>")
        continue
    else:
        break

a = "programujem v Pythone"
b = "som na matfyze"
print("Prvy text: ",a)
print("Druhy text: ",b)
print("=======================")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(b)
    else: 
        print(a)
print()
"""
#------------------------------------------------------------------------------
# 6. Napíšte skript, ktorý najprv prečíta jedno celé číslo n a potom prečíta n 
# ďalších desatinných čísel. Na záver vypíše súčet týchto čísel aj ich priemer.
# 
#        napr.
#
#        zadaj pocet: 4
#        zadaj cislo: 14.2
#        zadaj cislo: 1
#        zadaj cislo: 5.7
#        zadaj cislo: 22
#
#        sucet je 42.9
#        priemer je 10.725
#------------------------------------------------------------------------------
"""
print("------------------------------ 6 -------------------------------------")
sucet = 0
n = 0
while True:
    try:
        n = int(input("Zadaj pocet: "))
    except ValueError:
        print("ZADANY POCET NIE JE FORMATU INT()")
        continue
    else:
        break

print()
 
for i in range(n):
    while True:
        try:
            cislo = float(input("Zadaj cislo: "))
            print(i + 1, ". zadane cislo = ", cislo)
        except ValueError:
            print("Nespravny format cisla zadaj nanovo ", i + 1 ,". cislo nanovo ...")
            continue
        else:
            break

    sucet += cislo

print("===================================================")
print("Sucet je: {} \nPriemer je: {} " .format(sucet ,  (sucet / n)))

"""
#------------------------------------------------------------------------------
# 7. Napíšte skript, ktorý prečíta dve celé čísla a zo znakov '+', '-' a '|' 
# vypíše obdĺžnik veľkosti podľa zadaných čísel.
#  PRIKLAD:    
#    zadaj 1. cislo: 5
#    zadaj 2. cislo: 2
#    
#    +-----+
#    |     |
#    |     |
#    +-----+
#------------------------------------------------------------------------------
"""
print("------------------------------ 7 -------------------------------------")

prve = 0
druhe = 0
while True:
    try:
        prve = int(input("Zadaj 1. cislo: "))
        druhe = int(input("Zadaj 2. cislo: "))
    except ValueError:
        print("ZADANE CISLO NIE JE FORMATU INT()")
        continue
    else:
        break


for i in range(druhe + 2):
    if i == 0 or i == (druhe + 1):
        print("+" + (prve * "-") + "+")
    else:
        print("|" + (prve * "-") + "|")
        
print()
"""
#------------------------------------------------------------------------------
# 8. Napíšte skript, ktorý prečíta celé číslo n a vypíše tabuľku n x n čísel 
# od 1 do n**2, ktoré sú usporiadané do stĺpcov.
#
# PRIKLAD: 
#
# zadaj n: 5
#        
#        1 6 11 16 21
#        2 7 12 17 22
#        3 8 13 18 23
#        4 9 14 19 24
#        5 10 15 20 25
#------------------------------------------------------------------------------
"""
print("------------------------------ 8 -------------------------------------")

n = 0
while True:
    try:
        n = int(input("Zadaj cele cislo n = "))
    except ValueError:
        print(" Nespravny zadany format cisla!!!! ")
        continue
    else:
        break

for r in range(1, n+ 1):
    for s in range(1, n + 1):
        print(r, end=" ")
        r+=5
    print()
    
"""
#------------------------------------------------------------------------------
# 9. NNapíšte skript, ktorý prečíta celé číslo n a vypíše tabuľku čísel s n 
# riadkami, pričom v prvom sú čísla od 1 do n, každý ďalší riadok je o 1 kratší
# (bez posledného čísla), v poslednom je 1.
#    
#        napr.
#
#        zadaj pocet: 5
#
#        1 2 3 4 5
#        1 2 3 4
#        1 2 3
#        1 2
#        1
#------------------------------------------------------------------------------
"""
print("------------------------------ 9 -------------------------------------")

n = 0
while True:
    try:
        n = int(input("Zadaj cele cislo n = "))
    except ValueError:
        print(" Nespravny zadany format cisla!!!! ")
        continue
    else:
        break

for r in range(1, n + 1):       
    for s in range(1, 2 + n - r):   
        print(s, end=" ")       
    print()
"""
#------------------------------------------------------------------------------
# 10.  Upravte riešenie predchádzajúceho príkladu tak, že výpis každého riadku
# (okrem prvého) bude o 1 posunutý vpravo oproti predchádzajúcemu.
#
#        napr.
#
#        zadaj pocet: 5
#
#        1 2 3 4 5
#         1 2 3 4
#          1 2 3
#           1 2
#            1
#------------------------------------------------------------------------------
"""
print("------------------------------ 10 -------------------------------------")
    
n = 5
while True:
    try:
        n = int(input("Zadaj cele cislo n = "))
        print()
    except ValueError:
        print(" Nespravny zadany format cisla!!!! ")
        continue
    else:
        break

for r in range(1, n + 1):
    if r != 1:
        print((r - 2) * " ", end = " ")
          
    for s in range(1, 2 + n - r):
        print(s, end=" ")       
    print()
  
"""
#------------------------------------------------------------------------------
# 11. Napíšte skript, ktorý prečíta celé číslo n a vypíše výpočet faktoriálu 
# tohto čísla v tvare n! = 1*2*...*n = číslo.   
#
#        napr.
#
#        zadaj n: 5
#
#        5! = 1*2*3*4*5 = 120
#------------------------------------------------------------------------------
"""
print("------------------------------ 11 -------------------------------------")

n = 0
while True:
    try:
        n = int(input("Zadaj cele cislo n = "))
        print()
    except ValueError:
        print(" Nespravny zadany format cisla!!!! ")
        continue
    else:
        break  

faktorial = 1
print("{}!" .format(n), end = " = ")
for i in range(1 , n+1):
    if i == 1:
        znak = ""
    else:
        znak = "*"
    faktorial = faktorial * i 
    print("{}{}" .format(znak , i), end = "")
print(" = ", faktorial)

"""
#------------------------------------------------------------------------------
# 12. Napíšte skript, ktorý vypíše tabuľku výpočtu prvých 10 faktoriálov 
# (vo formáte z predchádzajúceho príkladu). Použite vnorené cykly.
#
#        výpis by mal byť v tomto tvare
#
#        1! = 1 = 1
#        2! = 1*2 = 2
#        3! = 1*2*3 = 6
#        4! = 1*2*3*4 = 24
#        ...
#------------------------------------------------------------------------------
"""
print("------------------------------ 12 -------------------------------------")
 
for r in range(1 , 11):
    print("{}!" .format(r), end = " = ")
    faktorial = 1
    for s in range(1 , r+1):
        if s == 1:
            znak = ""
        else:
            znak = "*"
        faktorial = faktorial * s 
        print("{}{}" .format(znak , s), end = "")
    print(" =", faktorial)


"""
===============================================================================
# ********** http://python.input.sk/03.html#matematicke-funkcie
# ********** 3.4. Cvičenie
#==============================================================================
# 1. Napíšte program, ktorý nakreslí pyramídu: tvoria ju 3 na sebe položené obdĺžniky
#    veľkosti 100x20, 60x20, 20x20, tieto obdĺžniky sú vycentrované.
#------------------------------------------------------------------------------
"""
print("------------------------------ 1 -------------------------------------")

from tkinter import *
root = Tk()
root.configure(bg = 'black')
root.title('1. pyramida')

#------------------------------------------------------------------------------
canvas = Canvas(root, bg = 'black', width = '600', height ='600')
canvas.pack()
canvas.create_rectangle(200, 300, 300, 320, outline = 'white')
canvas.create_rectangle(220, 300, 280, 280, outline = 'white')
canvas.create_rectangle(240, 280, 260, 260, outline = 'white')

root.mainloop()

"""
#------------------------------------------------------------------------------
# 2. Napíšte program, ktorý nakreslí podobnú pyramídu z predchádzajúceho príkladu,
#    pričom všetky obdĺžniky majú výšku 10 a ich šírky sú postupne 200, 180, 160, … 60, 40, 20.
#    +  vysklada po y suracdnici smerom dole // zmena suradnic pyramidy
#------------------------------------------------------------------------------
"""
print("------------------------------ 2 -------------------------------------")
import random
from tkinter import *
root = Tk()
root.configure(bg = 'black')
root.title('1. pyramida')
#------------------------------------------------------------------------------
canvas = Canvas(root, bg = 'black', width = '400', height = '400')
canvas.pack()
farba = 'white'
retazec = "!!!!! POPAPALO!!!!!"
textik = canvas.create_text(200, 250, text = retazec, fill = farba ,font='arial 30 bold'  )
canvas.update()
canvas.after(3000)

x = 100
y = 200
j = 1
for i in range(200,0, -20):
    rad_j = str(j)
    print("{}.riadok x1={} y1={} x2={} y2={} ".format(rad_j, x, y, (x + i), (y - 10)))
    rad_j = canvas.create_rectangle(x, y, (x+i), (y-10), outline = 'white')
    j = j + 1
    x = x + 10
    y = y - 10
    farba = random.choice(('red', 'blue', 'white', 'yellow', 'green'))
    canvas.itemconfig(textik, fill = farba, font='arial 30 bold')
    canvas.update()
    canvas.after(200)

print("<<<<<< POPAPALO >>>>>>>")

x = 100
y += 10
for i in range(200, 0, -20):
    rad_j = str(j)
    print("{}.riadok x1={} y1={} x2={} y2={} ".format((j-1), x, y, (x + i), (y - 10)))
    canvas.coords(rad_j, x, y, (x+i), (y-10))
    j = j - 1
    x = x + 10
    y = y + 10
    farba = random.choice(('red', 'blue', 'white', 'yellow', 'green'))
    canvas.itemconfig(textik, fill = farba)
    canvas.update()
    canvas.after(200)

root.mainloop()

"""
#------------------------------------------------------------------------------
# 3. Napíšte program, ktorý nakreslí rad n modrých kruhov: všetky sú tesne vedla
#    seba a majú polomer 20. Napr. pre n = int(input('zadaj pocet: ')).
#------------------------------------------------------------------------------
"""
print("------------------------------ 3 -------------------------------------")

print("<------------ nacitaj n = ------------>")
n = 0
while True:  # Overenie vstupu chybovou hlaskou
    try:
        n = int(input("Zadaj cislo n = "))
    except ValueError:
        print(">>> n -> NOK = Nie je integer")
        continue

    else:
        print(">>> n -> OK = Je integer")
        break

print("<------------- kresli ---------------->")
x = 20
y = 150
r = 20

okno_width = n * (2 * r)
okno_height = 2 * y
print("Nastavena velikost okna {}x{}" .format(okno_width, okno_height))

from tkinter import *
root = Tk()
root.configure(bg = 'black', )
root.geometry("{}x{}" .format(okno_width, okno_height))
#------------------------------------------------------------------------------
canvas = Canvas(root, bg = 'black', width = okno_width, height = okno_height)
canvas.pack()

for i in range(n):
    canvas.create_oval(x+r, y+r, x-r , y-r, outline = 'white')
    x = x + 2 * r        # dotykaju sa
    #x = x + 2 + * r      # nedotykaju sa
    print('x{}={} ' .format(i+1, x))
    canvas.update()
    canvas.after(1000)
print("<-------------------------------------------->")
root.mainloop()

"""
#------------------------------------------------------------------------------
# 4. Podobný príklad ako (3), ale výplne kruhov sú troch rôznych farieb: postupne sa striedajú
#    'red', 'yellow', 'blue'. Kreslenie kruhov zapíšte tak, aby sa nekreslil ich čierny obrys.
#------------------------------------------------------------------------------
"""
print("------------------------------ 4 -------------------------------------")
print("<------------ nacitaj n = ------------>")
n = 0
while True:  # Overenie vstupu chybovou hlaskou
    try:
        n = int(input("Zadaj cislo n = "))
    except ValueError:
        print(">>> n -> NOK = Nie je integer")
        continue

    else:
        print(">>> n -> OK = Je integer")
        break

print("<------------- kresli ---------------->")

x = 20
y = 150
r = 20

okno_width = n * (2 * r)
okno_height = 2 * y
print("Nastavena velikost okna {}x{}" .format(okno_width, okno_height))
import random
from tkinter import *
root = Tk()
root.configure(bg = 'black', )
root.geometry("{}x{}" .format(okno_width, okno_height))
#------------------------------------------------------------------------------
canvas = Canvas(root, bg = 'black', width = okno_width, height = okno_height)
canvas.pack()

for i in range(n):
    farba = random.choice(('red', 'yellow', 'blue'))
    canvas.create_oval(x+r, y+r, x-r , y-r, outline = 'white', fill = farba)
    x = x + 2 * r        # dotykaju sa
    #x = x + 2 + * r      # nedotykaju sa
    print('x{}={} ' .format(i+1, x))
    canvas.update()
    canvas.after(1000)
print("<-------------------------------------------->")
root.mainloop()

"""
#------------------------------------------------------------------------------
# 5. Napíšte program, ktorý najprv prečíta polomer kružnice (input('polomer: '))
#    potom ju nakreslí do stredu grafickej plochy a do neho pomocou
#    canvas.create_rectangle() nakreslí vpísaný štvorec
#    (jeho vrcholy ležia na obvode kružnice).
#------------------------------------------------------------------------------
"""
print("------------------------------ 3 -------------------------------------")

print("<------------ nacitaj r = ------------>")
r = 0
while True:  # Overenie vstupu chybovou hlaskou
    try:
        r = int(input("Zadaj celecislo pre POLOMER -> r = "))
    except ValueError:
        print(">>> r -> NOK = Nie je integer")
        continue

    else:
        print(">>> r -> OK = Je integer")
        break

print("<------------- kresli ---------------->")

import math
from tkinter import *

width_okno = 2 * r + 50
height_okno = 2 * r + 50

root = Tk()
root.configure(bg = 'black', )
root.geometry('{}x{}' .format(width_okno, height_okno))
#------------------------------------------------------------------------------

canvas = Canvas(root, bg = 'black', width = width_okno, height = height_okno)
canvas.pack()

y1 = x1 = width_okno / 2 + r
y2 = x2 = height_okno / 2 - r
canvas.create_oval(x1, y1, x2 , y2, fill = 'white')          # kruzinica
canvas.update()
canvas.after(1000)
#------------------------------------------------------------------------------
canvas.create_rectangle(x1, y1, x2 , y2, outline = 'red')    # stvorec nad kruznicou
canvas.update()
canvas.after(1000)

#------------------------------------------------------------------------------
y1 = x1 = width_okno / 2 + r / math.sqrt(2)
y2 = x2 = height_okno / 2 - r / math.sqrt(2)
canvas.create_rectangle(x1, y1, x2, y2, fill = 'blue')        # stvorec v kruznici
canvas.update()
canvas.after(1000)

print("<------------------ KONIEC --------------------->")
root.mainloop()

"""
#------------------------------------------------------------------------------
# 6. V priečinku, v ktorom je nainštalovaný Python, nájdite súbor 'rgb.txt'.
#    Zvoľte si z neho nejakých 5 zaujímavých farieb a ich mená vypíšte pod sebou
#    nejakým hrubým fontom, napr. canvas.create_text(x, y, text=meno_farby, font=..., fill=meno_farby).
#------------------------------------------------------------------------------
"""
print("------------------------------ 6 -------------------------------------")

from tkinter import *
root = Tk()
root.configure(bg = 'black')
root.geometry('400x400')
#------------------------------------------------------------------------------
canvas = Canvas(root, bg = 'black', width = '400', height = '400')
canvas.pack()
x = 400 / 2
y = 400 / 7
meno_farby = "DarkGoldenrod4"
canvas.create_text(x, y, text = meno_farby, font = 'Magneto 20 bold', fill = 'DarkGoldenrod4')
canvas.update()
canvas.after(500)
meno_farby = "BlanchedAlmond"
canvas.create_text(x, y + 40, text = meno_farby, font = 'Magneto 20 bold', fill = meno_farby)
canvas.update()
canvas.after(500)
meno_farby = "LemonChiffon3"
canvas.create_text(x, y + 80, text = meno_farby, font = 'Magneto 20 bold', fill = meno_farby)
canvas.update()
canvas.after(500)
meno_farby = "LightGoldenrod1"
canvas.create_text(x, y + 120, text = meno_farby, font = 'Magneto 20 bold', fill = meno_farby)
canvas.update()
canvas.after(500)
meno_farby = "LightYellow1"
canvas.create_text(x, y + 160, text = meno_farby, font = 'Magneto 20 bold', fill = meno_farby)
canvas.update()
canvas.after(500)
meno_farby = "snow"
canvas.create_text(x, y + 200, text = meno_farby, font = 'Magneto 20 bold', fill = meno_farby)
canvas.update()
canvas.after(500)
print("<------------------ KONIEC --------------------->")
root.mainloop()

"""
#------------------------------------------------------------------------------
# 10. Využite predchádzajúci príklad (9) a nakreslite n domčekov vedľa seba
#     (s malou medzerou medzi nimi). n prečítate zo vstupu (input()).
#------------------------------------------------------------------------------
"""
print("------------------------------ 9 -------------------------------------")

n = 20
# while True:  # Overenie vstupu chybovou hlaskou
#     try:
#         n = int(input("Zadaj celecislo pre POLOMER -> r = "))
#     except ValueError:
#         print(">>> r -> NOK = Nie je integer")
#         continue
#
#     else:
#         print(">>> n -> OK = Je integer")
#         break
x, y = 10, 80
a = 50
width_okno = n / 2 * (4 * x + a)
height_okno = width_okno / 2
print("{}x{}" .format(round(width_okno), round(height_okno)))
print("<------------- kresli ---------------->")
from tkinter import *
root = Tk()
root.configure(bg = 'CadetBlue1')
root.geometry("{}x{}" .format(round(width_okno), round(height_okno)))
#------------------------------------------------------------------------------

canvas = Canvas(root, bg = 'CadetBlue1', width = width_okno, height = height_okno)
canvas.pack()

for i in range(1,n+1):
    print("n=",i)
    print("x={} y={} x+a={} y+a={}" .format(x, y, x+a, y+a))
    canvas.create_rectangle(x, y, x+a, y+a, fill = 'blue', outline = 'black', width = '2')
    print("x={} y={} x+a={} y={} ((x+a)-(x/2))={} y-a={}" .format(x, y, x+a, y, ((x+a)-(x/2)), y-a))
    canvas.create_polygon(x, y, (x+a), y, (x+a/2), (y-a), fill = 'red', outline = 'black', width = '2')
    print("****************************************************************")
    canvas.update()
    canvas.after(500)
    x += a + 10
    while x >= (width_okno - a/2):
        x, y = 10, (y + 2 * a + 10)

print("<------------------ KONIEC --------------------->")
root.mainloop()

"""
#------------------------------------------------------------------------------
# 14. Body na kružnici so stredom (x0, y0) a polomerom r sa dajú vyjadriť vzorcom:
#
#     x = x0 + r * cos(uhol)
#     y = y0 + r * sin(uhol)
#
#    kde uhol je číslo od 0 do 360 stupňov (pozor na radiány).
#    Ak budete takto vypočítané body postupne spájať úsečkami
#    (napr. pomocou canvas.create_line()), dostanete kružnicu.
#    Nakreslite týmto postupom kružnicu, pričom otestujte kreslenie pre rôznu
#    hustotu bodov na kružnici (pre rôzne hodnoty zväčšovania uhla,
#    napr. s krokom 30, alebo 10 alebo 2, …).
#
#------------------------------------------------------------------------------
"""
print("------------------------------ 9 -------------------------------------")

width_okno = height_okno = 500
print("{}x{}" .format(round(width_okno), round(height_okno)))

print("<------------- kresli ---------------->")
import math
from tkinter import *
root = Tk()
root.configure(bg = 'black')
root.geometry("{}x{}" .format(round(width_okno), round(height_okno)))
#------------------------------------------------------------------------------

while True:  # Overenie vstupu chybovou hlaskou
    try:
        r = float(input("Zadaj float pre POLOMER > ako 400 -> r = "))
        while r > width_okno - 100:
            print("Polomer je vacsi ako velikost okna")
            r = float(input("Zadaj float pre POLOMER este raz -> r = "))
            continue
        else:
            d = int(input("Zadaj integerkrokovanie uhla od 0º do 360º -> d = "))
    except ValueError:
        print(">>> r -> NOK = Nie je integer")
        continue

    else:
        print(">>> INPUT -> OK ")
        break

canvas = Canvas(root, bg = 'black', width = width_okno, height = height_okno)
canvas.pack()
x0 = width_okno / 2
y0 = height_okno / 2
#pocet_luc = 0              # tyka sa zadania 15.
for uhol_st in range(0, 360 + 1, d):
    uhol_rad = (uhol_st * math.pi) / 180
    print("uhol={}º == {}RAD" .format(uhol_st, uhol_rad))
    x = x0 + r * math.sin(uhol_rad)
    y = y0 + r * math.cos(uhol_rad)
    #canvas.create_line(x0, y0, x, y, fill='white', width ='2') # usecka stred a bod uhla //tyka sa zadania 15
    if uhol_st > 0:
        canvas.create_line(x_old, y_old, x, y, fill='red', width='2')  # usecka bodu uhla
    print("****************************************************************")
    x_old = x
    y_old = y
   #pocet_luc+=1  # tyka sa zadania 15.
    canvas.update()
    canvas.after(500)
#print("pocet lucov:", pocet_luc - 1)   # -1 kol uhol_st 360 + 1 # tyka sa zadania 15.
print("")

print("<------------------ KONIEC --------------------->")
root.mainloop()

"""
#------------------------------------------------------------------------------
# 15. Ak v programe z predchádzajúcej úlohy (14) nebudeme spájať susedné vrcholy,
#     ktoré ležia na obvode kružnice, ale budeme spájať tieto vrcholy so stredom
#     kružnice (zvoľte žlté hrubé pero) a na koniec nakreslíme žltý kruh
#     (canvas.create_oval()) s rovnakým stredom ako naša kružnica ale s menším polomerom,
#     dostaneme slnko s lúčmi. Napíšte program:
#
#     pocet lucov: 10
#     dlzka lucov od stredu: 150
#     velkost slnka: 80
#     # nakreslí žlté slnko
#
#
#
#------------------------------------------------------------------------------
"""
print("------------------------------ 9 -------------------------------------")

width_okno = 600
height_okno = 600
print("{}x{}" .format(round(width_okno), round(height_okno)))

print("<------------- kresli ---------------->")
import math
from tkinter import *
root = Tk()
root.configure(bg = 'black')
root.geometry("{}x{}" .format(round(width_okno), round(height_okno)))
#------------------------------------------------------------------------------

while True:  # Overenie vstupu chybovou hlaskou
    try:
        r = float(input("Zadaj float pre vzdialenost lucov od stredu (<400) -> r = "))
        while r >= width_okno - 200 :
            if r > width_okno:
                print("Dlzka lucov je vacsia ako velikost okna")
            else:
                print("Dlzka lucov musi byt mensia ako 400")
            r = float(input("Zadaj float pre POLOMER este raz -> r = "))
            continue
        else:
            d = int(input("Zadaj integer krokovania uhla od 0º do 360 + 1º -> d = "))
    except ValueError:
        print(">>> r -> NOK = Nie je integer")
        continue

    else:
        print(">>> INPUT -> OK ")
        break

canvas = Canvas(root, bg = 'black', width = width_okno, height = height_okno)
canvas.pack()
x0 = width_okno / 2
y0 = height_okno / 2
pocet_luc = 0
r_oval = r / 3
canvas.create_oval(x0-r_oval, y0-r_oval, x0+r_oval, y0+r_oval, fill = 'yellow') # kruh
for uhol_st in range(0, 360 + 1, d):
    uhol_rad = (uhol_st * math.pi) / 180
    print("uhol={}º == {}RAD" .format(uhol_st, uhol_rad))
    x = x0 + r * math.sin(uhol_rad)
    y = y0 + r * math.cos(uhol_rad)
    canvas.create_line(x0, y0, x, y, fill='yellow', width ='2') # usecka stred kruh a koncovi bod luca
    print("****************************************************************")
    x_old = x
    y_old = y
    pocet_luc+=1
    canvas.update()
    canvas.after(200)
#------------------------------------------------------------------------------
x1_retangle = width_okno - 200
y1_retangle = height_okno - 100
x2_retangle = width_okno
y2_retangle = height_okno
canvas.create_rectangle(x1_retangle,y1_retangle, x2_retangle,y2_retangle, fill = 'grey25', outline = 'white', width = '2')


print("pocet lucov:", pocet_luc - 1)   # -1 kol uhol_st 360 + 1
print("dlzka lucov od stredu:", r)
print("velikost slnka (r_oval):",r_oval)

print("<------------------ KONIEC --------------------->")
root.mainloop()


"""
===============================================================================
# ********** http://python.input.sk/04.html
# ********** 4.2.2 Cvičenie
#==============================================================================
# 1. Zistite, akú hodnotu True alebo False (alebo inú) majú tieto výrazy:
#      > najprv to skúste bez počítača, potom to skontrolujte v Pythone
#
#         x, y = 7, 'ab'
#         8 < x <= 7
#         x <= 3 + x // 2
#         y != 2 * x or 2 * y == 'abab'
#         x < x + 1 < 2 * x
#         x // 8 or x * y
#         x or y
#         x and y
#         not y
#         not x % 2
#------------------------------------------------------------------------------
"""

x, y = 7, 'ab'
bool(x)                                   # True
bool(y)                                   # True
bool(8 < x <= 7)                          # False
bool(x <= 3 + x // 2)                     # False
bool(y != 2 * x or 2 * y == 'abab')       # False
bool(x < x + 1 < 2 * x)                   # True
bool(x // 8 or x * y)                     # True
bool(x or y)                              # True
bool(x and y)                             # True
bool(not y)                               # False
bool(not x % 2)                           # False

"""
#------------------------------------------------------------------------------
# 2. Napíšte program, ktorý najprv prečíta 3 desatinné čísla a, b, c a potom vypíše,
#    koľko reálnych ale rôznych koreňov má kvadratická rovnica so zadanými koeficientami
#    (zrejme výsledkom bude 0, alebo 1, alebo 2)
#
#    napr.:
#         zadaj a: 1
#         zadaj b: 2
#         zadaj c: 1
#         kvadraticka rovnica ma jeden koren
#------------------------------------------------------------------------------
"""
while True:  # Overenie vstupu chybovou hlaskou
    try:
        a = float(input("Zadaj cislo a = "))
        b = float(input("Zadaj cislo b = "))
        c = float(input("Zadaj cislo c = "))
    except ValueError:
        print(">>> -> cislo = Nie je float")
        continue

    else:
        print(">>> cisla -> OK = su float")
        break

D = b**2 - (4*a*c)              # Diskriminant

if D > 0:                       # D > 0
    print("D =",D,">0 Kvadraticka rovnica ma 2 rozne korene")
elif D == 0:                    # D == 0
    print("D =",D, "=0 Kvadraticka rovnica ma dva rovnake realne korene, cize tzv. dvojnasobny realny koren")
else:                           # D < 0
    print("D =",D,"<0 Kvadraticka rovnica nema riesenie v obore realnych cisiel(samozrejme ma dva imaginarne komplexne zdruzene korene)")

"""
#------------------------------------------------------------------------------
# 3. Máme daný tento program.
#
#     ručne bez počítača zistite, čo vypočíta pre vstupnú hodnotu 11:
#
#     cislo1 = 0
#     cislo2 = int(input('? '))
#     while cislo2 > 0:
#         if cislo2 % 2 == 0:
#             cislo2 //= 2
#         else:
#             cislo2 -= 1
#         cislo1 += 1
#     print(cislo1)
#
#     Vedeli by ste matematikovi, ktorý nevie programovať ale pozná dvojkovú sústavu, vysvetliť, čo tento program vypočíta?
#
#------------------------------------------------------------------------------
"""
print("------------------------------ 3 -------------------------------------")

cislo1 = 0                  # false
cislo2 = int(input('? '))   # cislo2 = 11 => True
while cislo2 > 0:           # 11 > 0  => False
    if cislo2 % 2 == 0:
        cislo2 //= 2
    else:                   # 11 % 2 = 1  => True
        cislo2 -= 1         # 11 - 1 = 10, ....
    cislo1 += 1             # cislo1 = 0 + 1 = 1, ....
    print("Cislo1 =",cislo1)
print(cislo1)               # cislo1 = 6

"""
#------------------------------------------------------------------------------
# 4. Napíšte program, ktorý najprv prečíta 3 desatinné čísla a, b, c a potom vypíše,
#    koľko reálnych ale rôznych koreňov má kvadratická rovnica so zadanými koeficientami
#    (zrejme výsledkom bude 0, alebo 1, alebo 2)
#
#    napr.:
#         zadaj a: 1
#         zadaj b: 2
#         zadaj c: 1
#         kvadraticka rovnica ma jeden koren
#------------------------------------------------------------------------------
# while True:  # Overenie vstupu chybovou hlaskou
#     try:
#         cislo1 = int(input("Zadaj cislo a = "))
#     except ValueError:
#         print(">>> -> cislo = Nie je int")
#         continue
#
#     else:
#         print(">>> cisla -> OK = su int")
#         break
#------------------------------------------------------------------------------
"""
cislo1 = 50273
while cislo1 > 0:
    zvysok = cislo1 % 10
    cislo1 = (cislo1 - zvysok) / 10
    print(int(zvysok))
print()

"""
#------------------------------------------------------------------------------
#   5.  Prerobte riešenie predchádzajúceho príkladu (4) tak, že cifry sa nebudú
#       vypisovať, ale sčitovať. Takto by ste mali dostať ciferný súčet daného čísla
#
#         napr.
#         zadaj cislo: 50273
#         ciferny sucet je 17
#
#------------------------------------------------------------------------------
# while True:  # Overenie vstupu chybovou hlaskou
#     try:
#         cislo1 = int(input("Zadaj cislo a = "))
#     except ValueError:
#         print(">>> -> cislo = Nie je int")
#         continue
#
#     else:
#         print(">>> cisla -> OK = su int")
#         break
#------------------------------------------------------------------------------
"""
sum_zvysok = 0
cislo1 = 50273
while cislo1 > 0:
    zvysok = cislo1 % 10
    cislo1 = (cislo1 - zvysok) / 10
    sum_zvysok += zvysok
print(int(sum_zvysok))

"""
#------------------------------------------------------------------------------
#   6. Využite ideu riešenia predchádzajúceho príkladu a vyriešte: program zistí, koľkokrát sa v zadanom čísle objaví nejaká konkrétna cifra
#
#         napr.
#
#         zadaj cislo: 123456789123456781234567
#         zadaj cifru: 8
#         cifra 8 sa vyskytla 2 krat
#
#         zadaj cislo: 123456789123456781234567
#         zadaj cifru: 0
#         cifra 0 sa vyskytla 0 krat
#
#
#
#------------------------------------------------------------------------------
# while True:  # Overenie vstupu chybovou hlaskou
#     try:
#         cislo1 = int(input("Zadaj cislo cislo1 = "))
#           cifra = int(input("Zadaj cislo cifra = "))
#     except ValueError:
#         print(">>> -> cislo, alebo cifra = Nie je int")
#         continue
#
#     else:
#         print(">>> cisla -> OK = su int")
#         break
#------------------------------------------------------------------------------
"""
cislo1 = 123456789123456781234567
cislo_zaloha = cislo1
cifra = 123
cifra_zaloha = cifra
pocet = 0

desatinna = 1
while cifra > 0:
    cifra //= 10
    desatinna *= 10
print(desatinna)

while cislo1 > 0:
    print("cislo1 pred -- ", cislo1)
    zvysok = int(cislo1 % desatinna)
    print("zvysok: ", zvysok)
    if zvysok == cifra_zaloha:
        pocet += 1
    cislo1 = int((cislo1 - zvysok) // desatinna)
    print("cislo1 po -- ", cislo1)
    print("****************************************")
print("Cifra:'{}' sa v cisle:'{}' vyskytla {} krat" .format(cifra_zaloha, cislo_zaloha, pocet))

"""
#------------------------------------------------------------------------------
#   7. Napíšte program, ktorý najprv prečíta celé číslo a vypíše jeho rozklad na prvočinitele.
#
#     snažte sa vyrobiť výpis v takomto tvare:
#
#     zadaj cislo: 24
#     24 = 2 * 2 * 2 * 3
#
#     zadaj cislo: 31
#     31 = 31
#
#     zadaj cislo: 65536
#     65536 = 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2
#
#------------------------------------------------------------------------------
# while True:  # Overenie vstupu chybovou hlaskou
#     try:
#         cislo = int(input("Zadaj cislo cislo1 = "))
#
#     except ValueError:
#         print(">>> -> cislo, alebo cifra = Nie je int")
#         continue
#
#     else:
#         print(">>> cisla -> OK = su int")
#         break
#------------------------------------------------------------------------------
"""
cislo = 12
cislo_zaloha = cislo
prv = 0
n = 0
print(cislo, "=", end = " ")
for prv in range(2, cislo + 1):
    while cislo % prv == 0:
        if n * 2 * prv == cislo_zaloha:
            print(prv)
        else:
            print(prv, "*", end=" ")
        cislo //= prv
        n += 1
print()

print("****************************************")

"""
#------------------------------------------------------------------------------
#  9. Fibonacciho postupnosť sa skladá z čísel 0,1,1,2,3,5,8,13,21, …, teda každé
#     ďalšie v postupnosti je súčtom dvoch predchádzajúcich. Napíšte program, ktorý
#     zistí najväčšie fibonacciho číslo, ktoré nie je väčšie ako 1000000.
#
#          použite while-cyklus
#------------------------------------------------------------------------------
"""

F0 = 0
F1 = 1
max_cislo = 32
vysl_a = 0
vysl_b = 0
f = 0

#------------------------------------------
# Vypis Fibonacciho postupnosti max_cisla
#------------------------------------------
print("F{}" .format(max_cislo), "=", end=" ")
for fx in range(0, max_cislo+1):
        print(F0, end=" ")
        F0, F1 = F1, F0 + F1
        if fx == max_cislo:
            print("", end="")
        else:
            print("+", end=" ")

print("=", F1 - F0)
print("****************************************")
#------------------------------------------------
# Vypise najvacsie Fibonacciho cislo < 1000000
#------------------------------------------------
F0 = 0
F1 = 1
while F0 < 1000000:
    F0, F1 = F1, F0 + F1
    print("Postupnost:", F0, end="")

print()
print("Najvacsie Fionacciho cislo < 1000000: ", F1 - F0)
print("****************************************")

"""
#------------------------------------------------------------------------------
#  10.  Máme daný tento program.
#         - najprv bez počítača odhadnite čo urobí
#         - uvažujte nad tým, čo nové ste sa na tomto príklade naučili
#------------------------------------------------------------------------------
"""
import random

i = 0
for i in range(10):                # Cyklus opakujuci sa 10 krat
    while random.randrange(10):    # podmieneny cyklus - opakuj kym nahodne nepadne 4 od 0 do 4
        print(end='x')
    print()
"""
#------------------------------------------------------------------------------
# 11. Grafická plocha má veľkosť vel x vel (vel je konštanta, napr. vel = 500).
#     Generujeme do nej n náhodných bodiek (malé krúžky s polomerom 3), pričom
#     súradnice x a y sú z intervalu <0, vel). Ak vzdialenosť vygenerovanej bodky
#     od bodu (0, 0) je menšia ako vel, bodka bude červená, inak bude modrá.
#     Počet bodiek n prečítajte zo vstupu. Počas generovania bodiek spočítajte,
#     koľko z nich je červených. Na záver program vypíše pomer počtu červených
#     bodiek ku všetkým vygenerovaným krát 4.
#
# vedeli by ste zdôvodniť, prečo sa tento pomer pre veľké n blíži k číslu pi?
#------------------------------------------------------------------------------
"""
print("------------------------------ 11 -------------------------------------")

import tkinter as tk
import random
import math


while True:  # Overenie vstupu chybovou hlaskou
    try:
        n = int(input("Zadaj pocet nahodnych zobrazeni"))
    except ValueError:
        print(">>> n -> NOK = Nie je integer")
        continue

    else:
        print(">>> INPUT -> OK ")
        break

vel = 500
r = 3

root = tk.Tk()
root.configure(bg = 'black')
width_okno = height_okno = vel
root.geometry("{}x{}" .format(round(width_okno), round(height_okno)))

canvas = tk.Canvas(bg = 'black', width = width_okno, height = height_okno)
canvas.pack()

x1, y1 = 0, 0                                             # suradnica x bodu A(0,0)
d, c, m = 0, 0, 0

for i in range(0, n):                                     # pocet opkaovania n kruhov
    x = random.randrange(vel)                             # vyber nahodnej suradnice x v intervale 0 <-> vel                                 # vyber nahodnej suradnice y v intervale 0 <-> 400
    y = random.randrange(vel)
    d = math.sqrt((x - x1)**2 + (y - y1)**2)              # vzdialenost medzi dvoma bodmi A(0,0) a B(x,y)
    print("d = ", d)
    if d >= vel:                                          # ak je vzdialenost >= ako vel(500), tak farba bodky bude modra
        farba = 'blue'
        m += 1
    else:                                                 # ak je vzdialenost < ako vel(500), tak farba bodky bude cervena
        farba = 'red'
        c += 1
    canvas.create_oval(x+r, y+r, x-r, y-r, fill = farba)      # vykreslenie kruznice a jej vyfarbenie
    print("i={} x={} y={}" .format(i, x, y))                  # vypis aktualnych hodnout v cykle
print("-------------------------------------------------------------------------------------")
print("Pocet cervenych modiek / c = {} \nPocet modrych bodiek / m = {}" .format(c, m))
print("Pocet kruhov / i = ", i + 1)

pomer_c = c
pomer_m = m
spol_delitel = 0
pomer = 0
x = 0

print("> Pomer cervenych k celkovemu poctu bodiek * 4 je: {}:{}" .format(pomer_c, (4*n)))                                                          # pomer cervenych k celkovemu poctu * 4
print("> pomer cervenych a modrich je = {}:{}" .format(pomer_c, pomer_m))

while pomer_m != 0 :                                      # Najmensi spolocny delitel
    x = int(pomer_c % pomer_m)
    pomer_c = pomer_m
    pomer_m = x

print("Splocny najvyssi delitel je = {}" .format(pomer_c))
print("> pomer cervenych a modrich je = {}:{}" .format(int(c / pomer_c), int(m / pomer_c)))

print("<------------------ KONIEC --------------------->")
root.mainloop()

"""
#------------------------------------------------------------------------------
# 12. Grafická plocha má veľkosť 300x200 a generujeme do nej náhodné bodky
#     (malé krúžky s polomerom 3), pričom súradnica x je z intervalu <0,300)
#     a y <0, 200). Ak vzdialenosť vygenerovanej bodky od bodu (100, 100) je
#     menšia ako 80, bodka bude červená, inak ak vzdialenosť od bodu (180, 100)
#     je menšia ako 90, bodka bude modrá, inak bodka bude čierna. Vygenerujte n takýchto bodiek.
#
#        n prečítajte zo vstupu
#------------------------------------------------------------------------------
"""
print("------------------------------ 12 -------------------------------------")

import tkinter as tk
import random
import math


while True:                                             # Overenie vstupu chybovou hlaskou
    try:
        n = int(input("Zadaj pocet nahodnych bodiek: "))
    except ValueError:
        print(">>> n -> NOK = Nie je integer")
        continue

    else:
        print(">>> INPUT -> OK ")
        break


r = 3
root = tk.Tk()
root.configure(bg = 'black')
width_okno = 300
height_okno = 200
root.geometry("{}x{}" .format(round(width_okno), round(height_okno)))

canvas = tk.Canvas(bg = 'black', width = width_okno, height = height_okno)
canvas.pack()

x1, y1 = 100, 100                                         # suradnica x bodu A(100,100)
x2, y2 = 180, 100                                         # suradnica x bodu B(180,100)
d1 = d2 = c = m = z = 0

for i in range(0, n):                                     # pocet opkaovania n kruhov
    x = random.randrange(width_okno)                      # vyber nahodnej suradnice x v intervale 0 <-> vel                                 # vyber nahodnej suradnice y v intervale 0 <-> 400
    y = random.randrange(height_okno)

    d1 = math.sqrt((x - x1)**2 + (y - y1)**2)             # vzdialenost medzi dvoma bodmi A(100,100) a B(x,y)
    d2 = math.sqrt((x - x2)**2 + (y - y2)**2)             # vzdialenost medzi dvoma bodmi B(180,100) a B(x,y)
    print("d1 = {} * d2 = {} " .format(d1, d2))

    if d1 < 80:                                   # ak je vzdialenost od bodu A(100,100) < ako 80, tak farba bodky bude cervena
        farba = 'red'
        c += 1
    elif d2 < 90:                                 # ak je vzdialenost od bodu B(180,100) < ako 80, tak farba bodky bude modra
        farba = 'blue'
        m += 1
    else:                                         # ostatne bodky budu mat zltu farbu
        farba = 'yellow'
        z += 1

    print(farba)
    canvas.create_oval(x+r, y+r, x-r, y-r, fill = farba)      # vykreslenie kruznice a jej vyfarbenie
    print("i={} x={} y={}" .format(i, x, y))                  # vypis aktualnych hodnout v cykle
print("-------------------------------------------------------------------------------------")
print("Pocet cervenych modiek / c = {} \nPocet modrych bodiek / m = {} \nPocet zltych bodiek / z = {}" .format(c, m, z))
print("Pocet kruhov / i = ", i + 1)


print("<------------------ KONIEC --------------------->")
root.mainloop()

"""
#------------------------------------------------------------------------------
# 13. Nastavte grafickú plochu na veľkosť sirka, vyska = 250, 250. Nakreslite
#     do nej šachovnicu 8x8 štvorčekov každý bude veľkosti 30x30, pričom ľavý
#     horný štvorček má ľavý horný roh na súradniciach (5, 5). Pri kreslení striedavo
#     zafarbujte políčka šachovnice dvomi farbami, napr. červenou a modrou
#     (dajte pozor na rozostavenie farieb ako na šachovnici).
#
#         > riešte dvomi vnorenými for-cyklami
#------------------------------------------------------------------------------
"""
print("------------------------------ 13 -------------------------------------")

import tkinter as tk

width_okno = 250
height_okno = 250
x, y, a = 5, 5, 30
farba_1 = 'black'
farba_2 = 'white'
root = tk.Tk()

root.configure(bg = 'white')
root.geometry("{}x{}" .format(round(width_okno), round(height_okno)))
canvas = tk.Canvas(bg = 'white', width = width_okno, height = height_okno)
canvas.pack()

for i in range(8):
    for j in range(1, 8):
        if i % 2 == 0:
            farba = farba_1
        else:
            farba = farba_2
        canvas.create_rectangle(x, y, x + a, y + a, fill = farba, outline='black')
        canvas.update()
        canvas.after(100)
        i += 1
        y = j*a + 5
    x += a
    y = 5



print("-------------------------------------------------------------------------------------")


print("<------------------ KONIEC --------------------->")
root.mainloop()

"""
#------------------------------------------------------------------------------
# 14. Predchádzajúci príklad (13) riešte tak, že sa nenakreslí šachovnica veľkosti 8x8,
#     ale šachovnica, v ktorej je len toľko štvorčekov v riadku, resp. v stĺpci,
#     aby sa každý z nich zmestil do grafickej plochy. Napr. pre sirka, vyska = 200, 150
#     bude mať šachovnica v každom riadku len 6 štvorčekov a riadky budú len 4.
#
#         namiesto dvoch vnorených for-cyklov použite while-cykly
#------------------------------------------------------------------------------
"""
print("------------------------------ 14 -------------------------------------")


"""
=====================================================================================
# ********** http://python.input.sk/05.html
# ********** 5.3. Cvičenie
#==============================================================================
# 1. Napíšte funkciu vypis_delitele(cislo), ktorá vypíše do jedného riadka
#    všetky delitele daného čísla.
#
#         napr.
#
#         >>> vypis_delitele(24)
#         1 2 3 4 6 8 12 24
#
#------------------------------------------------------------------------------
"""

def vypis_delitele(cislo):
    for i in range(1, cislo + 1):
        if cislo % i == 0:
            print(i, end=" ")


vypis_delitele(24)

"""
#------------------------------------------------------------------------------
# 2. Napíšte funkciu sucet_delitelov(cislo), ktorá vráti súčet všetkých deliteľov
#    daného čísla. Funkcia nič nevypisuje, funkcia vracia (pomocou return) nejakú hodnotu.
#
#         napr.
#
#         >>> x = sucet_delitelov(24)
#         >>> x
#         60
#------------------------------------------------------------------------------
"""
def sucet_delitelov(cislo):
    sucet = 0
    for i in range(1, cislo + 1):
        if cislo % i == 0:
            sucet += i
    return sucet

x = sucet_delitelov(24)
print(x)
"""
#------------------------------------------------------------------------------
# 3. Napíšte funkciu je_dokonale(cislo), ktorá pomocou funkcie sucet_delitelov()
#    zistí, či je dané číslo dokonalé, t.j. že súčet všetkých menších deliteľov
#    ako samotné číslo sa rovná samotnému číslu. Napr. delitele čísla 6 (menšie ako 6)
#    sú 1, 2, 3. Ich súčet je 6. Preto je číslo 6 dokonalé. Funkcia nič nevypisuje,
#    funkcia vracia (pomocou return) nejakú hodnotu.
#
#         napr.
#
#         >>> je_dokonale(6)
#         True
#         >>> je_dokonale(24)
#         False
#------------------------------------------------------------------------------
"""
def sucet_delitelov(cislo):
    sucet = 0
    for i in range(1, cislo + 1):
        if cislo % i == 0:
            sucet += i
    return sucet


def je_dokonale(cislo):
    if sucet_delitelov(cislo) - cislo == cislo:
        return True
    else:
        return  False

cislo = 6
print('Cislo -> {} \nJeho sucet mensich delitelov ako samotne cislo je = {} \nDokonale cislo = {}' .format(cislo, (sucet_delitelov(cislo) - cislo), je_dokonale(cislo)))

"""
#------------------------------------------------------------------------------
# 4. Napíšte funkciu vsetky_dokonale(od, do), ktorá vypíše dokonalé čísla v danom intervale.
#
#         napr.
#
#         >>> vsetky_dokonale(1, 30)
#         6 je dokonale
#         28 je dokonale
#------------------------------------------------------------------------------
"""
def sucet_delitelov(cislo):
    sucet = 0
    for i in range(1, cislo + 1):
        if cislo % i == 0:
            sucet += i
    return sucet

def je_dokonale(cislo):
    if sucet_delitelov(cislo) - cislo == cislo:
        return True
    else:
        return  False

def vsetky_dokonale(od, do):
    for cislo in range(od, do):
        if je_dokonale(cislo) == True:
            print(cislo,' -> je dokonale')


vsetky_dokonale(1, 30)

"""
#------------------------------------------------------------------------------
# 5. Napíšte funkciu nsd(a, b), ktorá počíta najväčší spoločný deliteľ dvoch čísel.
#    Funkcia nič nevypisuje, funkcia vracia (pomocou return) nejakú hodnotu.
#
#         napr.
#
#         >>> nsd(21, 15)
#         3
#         >>> nsd(1000000, 17)
#         1
#
#         odkrokujte vaše riešenie pomocou stránky http://www.pythontutor.com/visualize.html#mode=edit
#------------------------------------------------------------------------------
"""
def nsd(a, b):
    a = abs(a)
    while b > 0:
        b, a = a % b, b
    return a

x = nsd(15, 21)
print(x)

"""
#------------------------------------------------------------------------------
# 6. Napíšte funkciu pocet_delitelov(cislo), ktorá pre dané číslo zistí počet
#    všetkých deliteľov. Napr. delitele čísla 6 sú 1, 2, 3, 6, preto funkcia
#    vráti 4. Funkcia nič nevypisuje, funkcia vracia (pomocou return) nejakú hodnotu.
#
#         napr.
#
#         >>> pocet_delitelov(6)
#         4
#         >>> pocet_delitelov(17)
#         2
#    Zmena -> vytvorenie dvoch samostatnych funkcii 'pocet_delitelov_for(cislo)'
#    a 'pocet_delitelov_for(cislo)' kazda bude mat samostatne sledovanie cas behu
#    kodu 'elapse_time'.
#------------------------------------------------------------------------------
"""
from datetime import datetime
start_time = datetime.now()

#--------------------------------------------------------\
def millis():                   # vrati hodnotu casu v ms uplinutia od
   dt = datetime.now() - start_time
   ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
   return ms

def pocet_delitelov_while(cislo):
    start_time = datetime.now()
    cislo = abs(cislo)
    pocet = 0
    print('START time *_while >> {}s'.format(start_time))
    # >>> cez while podmienku <<<
    n = cislo
    while n > 0:
        if cislo % n == 0:
            pocet += 1
        n -= 1
    print('END time >> {}s'.format(datetime.now()))
    elapse_time = millis()
    print('ELAPSE time: {}s ={}ms'.format((start_time - datetime.now()), elapse_time))
    return pocet

def pocet_delitelov_for(cislo):
    start_time = datetime.now()
    cislo = abs(cislo)
    pocet = 0
    print('START time *_for >> {}s'.format(start_time))
    for i in range(1, cislo + 1):
        if cislo % i == 0:
            pocet += 1
    print('END time >> {}s'.format(datetime.now()))
    elapse_time = millis()
    print('ELAPSE time: {}s = {}ms'.format((start_time - datetime.now()), elapse_time))
    return pocet
#--------------------------------------------------------/

print('****************** WHILE ******************')
sum_while = pocet_delitelov_while(1000)
print('SUM = ', sum_while)

print('****************** FOR ******************')
sum_for = pocet_delitelov_for(1000)
print('SUM = ', sum_for)

"""
#------------------------------------------------------------------------------
# 7. Napíšte funkciu je_prvocislo(cislo), ktorá pomocou funkcie pocet_delitelov()
#    zistí (vráti True alebo False), či je to prvočíslo (je deliteľné len 1 a samým
#    sebou).
#
#     > napr.
#
#         >>> je_prvocislo(6)
#         False
#         >>> je_prvocislo(17)
#         True
#
#------------------------------------------------------------------------------
"""
from datetime import datetime
start_time = datetime.now()

#--------------------------------------------------------\
def millis():                   # vrati hodnotu casu v ms uplinutia od
   dt = datetime.now() - start_time
   ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
   return ms

def pocet_delitelov_while(cislo):
    start_time = datetime.now()
    cislo = abs(cislo)
    pocet = 0
    print('START time *_while >> {}s'.format(start_time))
    # >>> cez while podmienku <<<
    n = cislo
    while n > 0:
        if cislo % n == 0:
            pocet += 1
        n -= 1
    print('END time >> {}s'.format(datetime.now()))
    elapse_time = millis()
    print('ELAPSE time: {}s ={}ms'.format((start_time - datetime.now()), elapse_time))
    return pocet

# def pocet_delitelov_for(cislo):
#     start_time = datetime.now()
#     cislo = abs(cislo)
#     pocet = 0
#     print('START time *_for >> {}s'.format(start_time))
#     for i in range(1, cislo + 1):
#         if cislo % i == 0:
#             pocet += 1
#     print('END time >> {}s'.format(datetime.now()))
#     elapse_time = millis()
#     print('ELAPSE time: {}s = {}ms'.format((start_time - datetime.now()), elapse_time))
#     return pocet

def je_prvocislo(cislo):
    if pocet_delitelov_while(cislo) == 2:
        return True
    else:
        return False

#--------------------------------------------------------/

print('****************** WHILE ******************')
prvocislo_while = je_prvocislo(-6)
print('Prvocislo = ', prvocislo_while)

"""
#------------------------------------------------------------------------------
# 8. Napíšte funkciu vsetky_prvocisla(od, do), ktorá vypíše všetky prvočísla v
#    danom intervale do jedného riadka.
#
#       > napr.
#
#         >>> vsetky_prvocisla(1, 30)
#         2 3 5 7 11 13 17 19 23 29
#
#         odkrokujte vaše riešenie pomocou stránky
#               http://www.pythontutor.com/visualize.html#mode=edit
#
#------------------------------------------------------------------------------
"""
#--------------------------------------------------------\
def vsetky_prvocisla(od, do):
    od = abs(od)
    do = abs(do)
    cislo = 0
    if od < do:
        for i in range(od + 1, do):
            cislo = i
            if pocet_delitelov_while(cislo) == 2:
                print(cislo, end = " ")
    elif od > do:
        for i in range(do + 1, od):
            cislo = i
            if pocet_delitelov_while(cislo) == 2:
                print(cislo, end = " ")
    elif od == do:
        cislo = od
        if pocet_delitelov_while(cislo) == 2:
            print('od[{}] = do[{}] = nie je urceny spravny interval, ale cislo {} je prvocislo!' .format(od, do, od))
        else:
            print('od[{}] = do[{}] = nie je urceny spravny interval, ale cislo {} nie je prvocislo!'.format(od, do, od))


def pocet_delitelov_while(cislo):
    cislo = abs(cislo)
    pocet = 0
    n = cislo
    while n > 0:
        if cislo % n == 0:
            pocet += 1
        n -= 1
    return pocet
#--------------------------------------------------------/
print('--------------------------------')
vsetky_prvocisla(1, 30)
print('\n--------------------------------')
vsetky_prvocisla(30, 1)
print('\n--------------------------------')
vsetky_prvocisla(-1, 30)
print('\n--------------------------------')
vsetky_prvocisla(-1, 1)
print('--------------------------------')
vsetky_prvocisla(-2, 2)
print('--------------------------------')

"""
#------------------------------------------------------------------------------
# 9. Napíšte funkciu sucet_mocnin2(n), ktorá vráti súčet mocnín dvojky s exponentmi
#    menšími ako n. Napr. sucet_mocnin2(5), vráti hodnotu 1+2+4+8+16, t.j. hodnotu 31.
#
#      >otestujte
#
#         >>> for i in range(7):
#                 print(i, sucet_mocnin2(i))
#
#         0 0
#         1 1
#         2 3
#         3 7
#         4 15
#         5 31
#         6 63
#
#   > pokúste sa odhadnúť, aký vzorec by vedel vypočítať rovnaký výsledok ako dáva
#     funkcia sucet_mocnin2() ale bez cyklu.
#------------------------------------------------------------------------------
"""
#--------------------------------------------------------\
def sucet_mocnin2(n):
    sucet = 0
    for m in range(0, n):
        sucet += 2 ** m
    return sucet

#--------------------------------------------------------/

print('--------------------------------')
for i in range(7):
    print(i, sucet_mocnin2(i))
"""
#------------------------------------------------------------------------------
# 10. Napíšte funkciu sucet_mocnin2a(n), ktorá vráti súčet prevrátených mocnín
#     dvojky s exponentmi menšími ako n. Napr. sucet_mocnin2a(5), vráti hodnotu
#     1/1+1/2+1/4+1/8+1/16, t.j. hodnotu 1.9375.
#
#      >otestujte
#
#         >>> for i in range(7):
#                 print(i, sucet_mocnin2a(i))
#
#         0 0
#         1 1.0
#         2 1.5
#         3 1.75
#         4 1.875
#         5 1.9375
#         6 1.96875
#
#         všimnite si, že výsledok sa pre väčšie n blíži k nejakej konštante
#------------------------------------------------------------------------------
"""
#--------------------------------------------------------\
def sucet_mocnin2a(n):
    sucet = 0
    for m in range(0, n):
        sucet += 1 / 2 ** m
    return sucet

#--------------------------------------------------------/
print('--------------------------------')
for i in range(7):
    print(i, sucet_mocnin2a(i))
"""
#------------------------------------------------------------------------------
# 11. Napíšte funkciu kocka() bez parametrov, ktorá pri každom zavolaní vráti
#     náhodné číslo z intervalu od 1 do 6.
#
#     otestujte
#
#         >>> for i in range(20):
#                 print(kocka(), end=' ')
#         ...
#
#         opravte tento testovací cyklus tak, že v postupnosti vypisovaných
#         čísel za každé, ktoré je rovnaké ako predchádzajúce, vypíšete aj znak '*', napr.
#
#         >>> ... for i in range(20): ...
#         6 4 4 * 4 * 3 5 4 3 5 5 * 1 2 1 1 * 1 * 1 * 2 2 * 6 1
#------------------------------------------------------------------------------
"""
import random
last = 0
k = 0

#--------------------------------------------------------\
def kocka():
    return random.randint(1, 6)


#--------------------------------------------------------/
print('--------------------------------')
for i in range(20):
    k = kocka()
    print(k, end = ' ')
    if last == k:
        print('*', end = ' ')
    last = k
"""
#------------------------------------------------------------------------------
# 12. Napíšte funkciu pocet_samohlasok(text), ktorá pre zadaný znakový reťazec
#     zistí počet samohlások, ktoré obsahuje.
#
#         napr.
#
#         >>> pocet_samohlasok('python')
#         2
#         >>> pocet_samohlasok('strc prst skrz krk')
#         0
#
#------------------------------------------------------------------------------
"""
#--------------------------------------------------------\
def pocet_samohlasok(text):
    pocet = 0
    for i in text:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'ä' or i == 'á' or i == 'é' or i == 'í' or i == 'ó' or i == 'ú':
            pocet += 1
        else:
            pocet += 0
    print(pocet)
#--------------------------------------------------------/
print('------------- VYSLEDOK ----------------')

pocet_samohlasok('python')              # 1
pocet_samohlasok('strc prst skrz krk')  # 0
pocet_samohlasok('á, é, í, ó, ú')       # 5

"""
#------------------------------------------------------------------------------
# 13. Napíšte funkcie gula(x, y, r) a snehuliak(x, y, r). Funkcia gula() nakreslí
#     biely kruh so stredom (x, y) a s polomerom r. Funkcia snehuliak() pomocou troch \
#     volaní gula() nakreslí snehuliaka, v ktorom spodná najväčšia guľa má stred (x, y)
#     a polomer r. Stredná má polomer 2/3 veľkej a najmenšia je polovičná strednej.
#     Otestujte na bledomodrom pozadí.
#
#       > napr.
#
#         >>> snehuliak(200, 400, 90)
#         >>> snehuliak(400, 300, 45)
#         >>> snehuliak(100, 200, 30)
#
#------------------------------------------------------------------------------
"""
from tkinter import *
root = Tk()
root.configure(bg = 'black')
root.title('Snehuliak')

#--------------------------------------------------------\
def gula(x, y, r):
    canvas.create_oval(x-r, y-r, x+r, y+r, outline = 'white')

def snehuliak(x, y, r):
    i = 0
    for i in range(3):
        r_old = r
        print("{}... x:{} y:{} r:{}" .format(i,x,y,r))
        gula(x, y, r)
        if i == 0:
            r = r_old * 2/3
        else:
            r *=  1/2
        y -= r_old + r

#--------------------------------------------------------/

print('------------- VYSLEDOK ----------------')

canvas = Canvas(root, bg = 'black', width = '600', height ='600')
canvas.pack()

snehuliak(200, 400, 90)
snehuliak(400, 300, 45)
snehuliak(100, 200, 30)

root.mainloop()
"""
#------------------------------------------------------------------------------
# 14. Napíšte funkciu karticka(x, y, text), ktorá do grafickej plochy nakreslí
#     bledošedý obdĺžnik a do jeho stredu vypíše zadaný text. Stred kartičky má
#     súradnice (x, y) a jej strany majú dĺžky 100 a 40. Font písma nech je napr.
#     'arial 14'.
#
#        > otestujte náhodným vygenerovaním 10 kartičiek, napr. s textom 'Python'
#        > otestujte náhodným vygenerovaním 10 kartičiek s textom súradníc kartičky,
#          napr. v tvare '(354,211)'
#
#------------------------------------------------------------------------------
"""
import random
from tkinter import *
root = Tk()
root.configure(bg = 'black')
root.title('Karticka')

#--------------------------------------------------------\
def karticka(x, y):
    x_karta = x - 100 / 2
    y_karta = y + 40 / 2
    text = '(' + str(round(x_karta)) + ', ' + str(round(y_karta)) + ')'
    canvas.create_rectangle(x_karta , y_karta, (x_karta + 100), (y_karta - 40), fill = '#47476b', outline = 'white', width = '2' )
    canvas.create_text(x, y, text = text, fill = 'white' ,font='arial 8 bold')
#--------------------------------------------------------/

print('------------- VYSLEDOK ----------------')

canvas = Canvas(root, bg = 'black', width = '600', height ='600')
canvas.pack()

for i in range(10):
    x = random.randrange(0 + 100/2, 600 - 100/2)                             # vyber nahodnej suradnice x v intervale 0 <-> vel                                 # vyber nahodnej suradnice y v intervale 0 <-> 400
    y = random.randrange(0 + 40/2, 600 -40/2)
    karticka(x, y)


root.mainloop()
"""
#------------------------------------------------------------------------------
# 15. Napíšte funkcie stvorec(x, y, a, farba), trojuholnik(x, y, a, farba) a
#     domcek(x, y, a=50, farba1='blue', farba2='red'). Funkcia stvorec() nakreslí
#     farebný štvorec s ľavým horným vrcholom na (x, y) a stranou a. Funkcia
#     trojuholnik() nakreslí rovnoramenný trojuholník s ľavým dolným vrcholom v (x, y)
#     so stranou aj výškou a. Funkcia domcek() nakreslí domček pomocou štvorca a trojuholníka.
#
#       > otestujte vykreslením 10 domčekov na náhodných pozíciách
#
#------------------------------------------------------------------------------
"""
import random
from tkinter import *
root = Tk()
root.configure(bg = 'black')
root.title('Karticka')
a = 50

#--------------------------------------------------------\

def stvorec(x, y, a, farba):
    canvas.create_rectangle(x, y, x+a, y+a, fill = farba)

def trojuholnik(x, y, a, farba):
    canvas.create_polygon(x, y, x+a, y, x+a/2, y-a, fill = farba )

def domcek(x, y, a, farba1='blue', farba2='red'):
    stvorec(x, y, a, farba1)
    trojuholnik(x, y, a, farba2)

#--------------------------------------------------------/

print('------------- VYSLEDOK ----------------')

canvas = Canvas(root, bg = 'black', width = '600', height ='600')
canvas.pack()


for i in range(10):
    x = random.randrange(0, 600 - a)                             # vyber nahodnej suradnice x v intervale 0 <-> vel                                 # vyber nahodnej suradnice y v intervale 0 <-> 400
    y = random.randrange(0 + a, 600 - 2*a)
    domcek(x, y, a)


root.mainloop()
"""
#------------------------------------------------------------------------------
# 16. Napíšte funkcie kruh(x, y, r) a sustredne(n, x, y). Funkcia kruh()
#     nakreslí na zadané súradnice kruh daného polomeru a vyplní ho náhodnou farbou.
#     Funkcia sustredne() pomocou kruh() nakreslí n sústredných farebných kruhov s
#     polomermi 5, 10, 15, 20, … Použite funkciu nahodna_farba() z prednášky.
#------------------------------------------------------------------------------
"""
import random
from tkinter import *
root = Tk()
root.configure(bg = 'black')
root.title('Sustredene')
farba = ''

#--------------------------------------------------------\
def kruh(x, y, r):
    farba = '#{:02x}{:02x}{:02x}'.format(random.randrange(256), random.randrange(256), random.randrange(256))
    canvas.create_oval(x-r, y-r, x+r, y+r, outline = farba)
    print('x:{} , y:{} , r:{} , farba:{}'.format(x, y, r, farba))


def sustredne(n, x, y):
    r_old = r = 20            # POLOMER
    size_font = round(r/2)
    pismo = 'arial ' + str(size_font) + ' bold'
    print(pismo)
    for i in range(1, n+1):
        if i == 1:
            x_t, y_t = x, y
        x_t, y_t = x , (y-r)+size_font
        canvas.create_text(x_t, y_t, text = i, fill = 'white', font = pismo)
        print(i, end=':  ')
        kruh(x, y, r)
        r += r_old


#--------------------------------------------------------/

print('------------- VYSLEDOK ----------------')

canvas = Canvas(root, bg = 'black', width = '600', height ='600')
canvas.pack()

sustredne(10, 300, 300)

root.mainloop()

"""
#------------------------------------------------------------------------------
# 17. Napíšte funkcie: kocka(x, y, a, farba), ktorá nakreslí farebný štvorec s
#     daným stredom a danou stranou; funkcia rad(n, x, y, a) nakreslí vedľa seba
#     n štvorcov (prvý ľavý z nich na zadaných súradniciach), pričom sú zafarbené
#     rovnakou náhodnou farbou; funkcia pyramida(n, x, y, a) pomocou funkcie rad()
#     nakreslí pyramídu výšky n, t.j. zloženú z n radov dĺžky 1, 2, 3, … n.
#     Najvyššia kocka pyramídy je na zadaných súradniciach. Každý nižší rad kociek
#     sa nakreslí o a nižšie a o a/2 odsunutý vľavo.
#
#       > otestujte v ploche veľkosti 500x500 napr.
#
#         >>> pyramida(10, 250, 50, 40)
#------------------------------------------------------------------------------
"""
import random
from tkinter import *
root = Tk()
root.configure(bg = 'black')
root.title('Sustredene')
farba_outline = 'white'
farba = ''
width_okno = 500
height_okno = 500

#--------------------------------------------------------\
# funkcie: kocka(x, y, a, farba), ktorá nakreslí farebný štvorec s
# daným stredom a danou stranou
def kocka(x, y, a, farba):
    canvas.create_rectangle(x, y, x+a, y+a, outline = farba_outline, fill = farba)
    print('x:{} , y:{} , a:{} , farba:{}'.format(x, y, a, farba))

# funkcia rad(n, x, y, a) nakreslí vedľa seba
# n štvorcov (prvý ľavý z nich na zadaných súradniciach), pričom sú zafarbené
# rovnakou náhodnou farbou
def rad(n, x, y, a):
    print('n:', n )
    farba = '#{:02x}{:02x}{:02x}'.format(random.randrange(256), random.randrange(256), random.randrange(256))
    while n != 0:
        kocka(x, y, a, farba)
        x += a
        n -= 1
# funkcia pyramida(n, x, y, a) pomocou funkcie rad()
# nakreslí pyramídu výšky n, t.j. zloženú z n radov dĺžky 1, 2, 3, … n.
# Najvyššia kocka pyramídy je na zadaných súradniciach. Každý nižší rad kociek
# sa nakreslí o a nižšie a o a/2 odsunutý vľavo.
def pyramida(n, x, y, a):
    #x = width_okno / 2 - a/2
    #y = a/2
    for i in range(1, n+1):
        rad(i, x, y, a)
        y += a
        x -= a/2

#--------------------------------------------------------/

print('------------- VYSLEDOK ----------------')

canvas = Canvas(root, bg = 'black', width = str(width_okno), height = str(height_okno))
canvas.pack()

#kocka(300, 50, 50, farba)
#rad(5, 300, 50, 50)

pyramida(10, 250, 50, 40)


root.mainloop()


# -------------------------------------------------------------------------------
# Cvicenia 6
# -------------------------------------------------------------------------------
"""
#------------------------------------------------------------------------------
# 6. Znakový reťazec vieme prevrátiť pomocou zápisu retazec[::-1]. Napíšte funkciu
#    prevrat(retazc), ktorá len pomocou cyklu a zreťazovania prevráti zadaný reťazec.
#    Funkcia nič nevypisuje, jej výsledkom (return) je znakový reťazec.
#
#         napr.
#
#         >>> prevrat('tseb eht si nohtyP')
#         'Python is the best'
#
#------------------------------------------------------------------------------
"""
def prevrat(retazec):
    opacny_retazec = ''
    for i in range(len(retazec)):
        opacny_retazec = retazec[::-1]
    return opacny_retazec

print(prevrat('tseb eht si nohtyP'))

"""
#------------------------------------------------------------------------------
# 7. Napíšte funkciu bez_medzier(text), ktorá z daného textu vyhodí všetky medzery.
#    Funkcia nič nevypisuje, jej výsledkom (return) je znakový reťazec.
#
#         napr.
#
#         >>> bez_medzier('  Mon  tyPy thon   ')
#         'MontyPython'
#
#------------------------------------------------------------------------------
"""

def bez_medzier(text):
    n = 0
    while ' ' in text:
        return text.replace(' ', '')


print(bez_medzier('  Mon  tyPy thon   '))

"""
#------------------------------------------------------------------------------
# 8. Napíšte funkciu dopln(text, znaky), ktorá postupne v zadanom texte hľadá
#    všetky výskyty znaku '.' nahradzuje ich znakmi z parametra znaky
#    (predpokladáme, že je ich tam dosť). T.j. prvý výskyt '.' sa nahradí prvým
#    znakom z znaky, druhý výskyt druhým znakom, atď.
#
#         napr.
#
#         >>> dopln('.on.. P.t.on', 'Mtyyh')
#         'Monty Python'
#
#------------------------------------------------------------------------------
"""
def dopln(text, znaky):
    n = 0
    while '.' in text:
        i = text.find('.')
        if i == 0:
            text = text[i].replace('.', znaky[n]) + text[i+1:]
            n += 1
        else:
            text = text[0:i] + text[i].replace('.', znaky[n]) + text[i+1:]
            n += 1
    return text

print(dopln('.on.. P.t.on', 'Mtyyh'))


"""
#------------------------------------------------------------------------------
# 9. Napíšte funkciu nahrad_samo(text, znak), ktorá v zadanom texte nahradí všetky
#      samohlásky ('aeiouy') zadaným znakom.
#
#         napr.
#
#         >>> nahrad_samo('sedi mucha na stene', 'i')
#         'sidi michi ni stini'
#         >>> nahrad_samo('sedi mucha na stene', '*')
#         's*d* m*ch* n* st*n*'
#
#------------------------------------------------------------------------------
"""

# -------------------------------------------------------------------------------
# Cvicenia 7
# -------------------------------------------------------------------------------

"""
#------------------------------------------------------------------------------
# 1. Napíšte program, ktorý si vypýta meno súboru a potom vypíše prvé 3 znaky z prvého riadka tohto súboru.
#
#    napr. ak súbor 'text1.txt' obsahuje
#
#         programujem v Pythone
#
#         spustenie programu:
#
#         meno suboru: text1.txt
#         prve 3 znaky: 'pro'
#
#------------------------------------------------------------------------------
"""
print("------------------------------ 1 -------------------------------------")

prve_tri = ''

print('Spustenie programu:')
vstup_subor = input("Zadaj meno suboru v pracovnej zlozke: ")
cesta_subor = 'WORK_FILES/'+vstup_subor
with open(cesta_subor, 'r', encoding = 'utf-8') as f:
    riadok = f.readline()
    print(riadok[:3])

"""
#------------------------------------------------------------------------------
# 2. Napíšte program, ktorý si vypýta meno súboru a potom vypíše počet riadkov
a    dĺžku najdlhšieho riadka tohto súboru.
#
#         napr.
#
#         meno suboru: text2.txt
#         pocet riadkov suboru: 13
#         najdlhsi ma 40 znakov
#
#   Zadanie doplnene o vytvorenie suboru s obsahom...
#------------------------------------------------------------------------------
"""
print("------------------------------ 2 -------------------------------------")
print('--------- VYTVOR / VYMAZ SUBORU ---------')
i, znak = 0, 0
retazec = ''
with open('WORK_FILES/text2.txt', 'w', encoding='utf-8') as w:# Otvor subor na zapis
    print('Subor WORK_FILES/text2.txt je vytvoreny / vycisteny !!!')

print('--------- VYGENERUJ RIADKY SUBORU ---------')
with open('WORK_FILES/text2.txt', 'a', encoding='utf-8') as a:      # Otvor subor na doplnenie
    for i in range(15):
        if i == 10:                                                 # ak je 10 riadok v subore
            retazec = str(i) + '. riadok = '
            for znak in range(40 - len(retazec)):                   # vytvor retaze dlhy 40 znakov
                retazec += '*'
            a.write(retazec + '\n')                                 # zapis vytvoreny retazec do riadku
        else:
            a.write(str(i) + '. riadok\n')                          # zapis riadok

print('--------- HLADAJ NAJDLHSI RIADOK ---------')
with open('WORK_FILES/text2.txt', 'r', encoding='utf-8') as r:      # Otvor subor na citanie
    najdlhsi_riadok = 0                                             # inicializacia najdlhsieho riadku od 0
    znaky_riadku = 0                                                # inicializacia poctu znakov riadku od 0
    i = 0
    riadok = r.readline()
    while riadok != '':                                             # ak nie je riadok bez znaku
        print(i,'. riadok ', end='')
        znaky_riadku = len(riadok)                                  # znaky_riadku = pocet znakov v riadku
        if znaky_riadku > najdlhsi_riadok:                          # ak je pocet znakov riadku vacsi nez doposial najdlhsi riadok
            print(' ---> ', znaky_riadku, ' > ', najdlhsi_riadok)
            najdlhsi_riadok = znaky_riadku                          # priudel pocet znakov riadku do premennej najdlhsi_riadok
        else:
            print(' ---> ', znaky_riadku, ' <= ', najdlhsi_riadok)
        i += 1
        riadok = r.readline()

print('------------------------------------------\nNajdlhsi riadok ma ...', najdlhsi_riadok, ' znakov' )



# -------------------------------------------------------------------------------
# Cvicenia 10
# -------------------------------------------------------------------------------

"""
#------------------------------------------------------------------------------
# 19. Naprogramujte takúto hru na postreh:
#
#   - každých interval milisekúnd sa farebný kruh s polomerom r presunie na náhodnú pozíciu v ploche
#   -  keď klikneme do plochy a trafíme do vnútra kruhu, ku nášmu skóre sa pripočíta 1
#   -  keď klikneme do plochy, ale netrafíme do kruhu, skóre sa zníži o 1
#   -  aktuálne skóre sa vypisuje niekde v rohu obrazovky (ako grafický objekt create_text())
#   -  interval a r sú nejaké globálne premenné, napr. s hodnotami 500 a 20
#
#------------------------------------------------------------------------------
"""
print("------------------------------ 19 -------------------------------------")
from tkinter import *
import random
root = Tk()
root.configure(bg = 'white')
root.title('19.')
canvas = Canvas(root, bg = 'white', width = '400', height = '400')
canvas.pack()
#------------------------------------------------------------------------------
# canvas.update()
# canvas.after(3000)


def zmen_poziciu():
    """
    Definicia zabezpeci zmenu suradnice "kruhu" v casovom intervale "t"
    :return:
    """
    x, y = random.randrange(350), random.randrange(350)
    canvas.coords('kruh', x+r, y+r, x-r, y-r)
    canvas.after(t, zmen_poziciu)

def klik(event):
    """
    Definicia vyhodnocuje pocet zasahov kurzoka mysi do suradnic kruhu.
    Ak sa netrafis, tak skore -= 1 ak sa trafis, tak skore += 1
    :param event:
    :return:
    """
    global skore
    xy_klik = [event.x, event.y]                    # aktualna pozicia kliknutia kurzorom
    xy_kruh = canvas.coords('kruh')
    x_kruh = [xy_kruh[0], xy_kruh[2]]
    x_kruh.sort()
    y_kruh = [xy_kruh[1], xy_kruh[3]]
    y_kruh.sort()
    # print('xy_klik: {} <-> kruh_coords:{}' .format(xy_klik, (x+r, y+3, x-r, y-r)))
    # print(xy_klik)

    if float(xy_klik[0]) <= float(x_kruh[1]) and float(xy_klik[0]) >= float(x_kruh[0]):
        print('Trafil si X !!!')
        print('Y = ', y)
        if float(xy_klik[1]) <= float(y_kruh[1]) and float(xy_klik[1]) >= float(y_kruh[0]):
            print('Trafil si Y !!!')
            skore += 1
            canvas.itemconfig('text', text = 'Skore: ' + str(skore))
        else:
            print('Netrafil Y !!!!')
            skore -= 1
            canvas.itemconfig('text', text='Skore: ' + str(skore))
    else:
        print('Netrafil X!!!!')
        skore -= 1
        canvas.itemconfig('text', text='Skore: ' + str(skore))


t = 1000                            # Interval
r = 10                              # polomer kruhu
skore = 0
x = random.randrange(350)
y = random.randrange(350)
canvas.create_oval(x+r, y+r, x-r, y-r, tag='kruh', fill = 'red')
canvas.create_text(360, 20,tag='text',  text = 'Skore: ' + str(skore), font="arial 10 bold")

zmen_poziciu()
canvas.bind('<Button-1>', klik)


root.mainloop()



"""
#------------------------------------------------------------------------------
# 21. V strede plochy je malý útvar (obrázok, alebo štvorček, alebo text, …).
#     Ďalej máme dve globálne premenné dx=dy=0. Po stlačení jednej zo šípok sa
#     útvar začne pohybovať daným smerom, t. j. príslušná premenná dx alebo dy
#     sa zvýši alebo zníži o 1 (podľa zatlačeného smeru šípky) a útvar sa bude
#     posúvať o momentálne (dx, dy).
#
#     - na okrajoch plochy útvar zastane, t. j. nezrealizuje posunutie, ktoré by ho dostalo von z plochy
#     - aj keď útvar stojí na mieste, môžeme stláčať šípky a tým mu meniť (dx, dy) a teda ho môžeme aj rozbehnúť
#------------------------------------------------------------------------------
"""
print("------------------------------ 21 -------------------------------------")
from tkinter import *

root = Tk()
root.configure(bg = 'white')
root.title('21.')
canvas = Canvas(root, bg = 'white', width = '400', height = '400')
canvas.pack()

# ------------------------------------------------------------------------------

def posun(dx, dy, smer):
    global x, y
    x, y = canvas.coords('obrazok')[0], canvas.coords('obrazok')[1]
    x += dx
    y += dy
    sipka = smer

    if x >= 400:
        print('X = 400')
        x = 400

    if x <= 0:
        print('X = 0')
        x = 0

    if y >= 400:
        print('Y = 400')
        y = 400

    if y <= 0:
        print('Y = 0')
        y = 0

    print('x:{}, y:{}' .format(x, y))
    canvas.coords('obrazok', x, y)
    canvas.itemconfig('obrazok', text = sipka, font='arial 20 bold')


def udalost_vlavo(event):
    smer_vlavo = '◄'
    posun(-10, 0, smer_vlavo)

def udalost_vpravo(event):
    smer_vpravo = '►'
    posun(10, 0, smer_vpravo)

def udalost_hore(event):
    smer_hore = '▲'
    posun(0, -10, smer_hore)

def udalost_dolu(event):
    smer_dole = '▼'
    posun(0, 10, smer_dole)


# img = PhotoImage(file = 'Image\image1.png')
# canvas.create_image(200, 200, image=img, tag='obrazok')
canvas.create_text(200, 200, text='●', font='arial 30 bold', tag='obrazok')

canvas.bind_all('<Left>', udalost_vlavo)
canvas.bind_all('<Right>', udalost_vpravo)
canvas.bind_all('<Up>', udalost_hore)
canvas.bind_all('<Down>', udalost_dolu)

root.mainloop()


"""
#------------------------------------------------------------------------------
# http://input.sk/python2016/14.html
# 12. Zadefinujte triedu Okno, ktorá otvorí grafické okno a do stredu vypíše zadaný text. Výška otvoreného okna nech je 100.
      Vypísaný text nech je v strede okna fontom veľkosti 50. Inicializácia (metóda __init__()) vytvorí nový canvas (výšky 100)
      a do jeho stredu vypíše zadaný text. Zrejme si v atribútoch zapamätá canvas aj identifikačný kód pre create_text().
      Ďalšie dve metódy menia vypísaný text:

        zmen(text) zmení vypísaný text (zrejme na to použijete itemconfig())
        farba(farba) zmení farbu vypísaného textu (zrejme na to použijete itemconfig())
        napr.

        import tkinter
        okno = Okno('ahoj')
        okno.farba('red')
        okno.zmen('Python')

        vyskúšajte vytvoriť dve inštancie Okno

#------------------------------------------------------------------------------
"""
print("------------------------------ 12 -------------------------------------")

from tkinter import *
import random

class Okno:

    def __init__(self, text):
        self.text = text
        self.root = Tk()
        self.root.configure(bg='white')
        self.root.title(self.text)
        self.canvas = Canvas(self.root, bg='white', width='400', height='100')
        self.canvas_text = self.canvas.create_text(200,50, text = self.text, font='arial 50 bold')
        self.canvas.pack()


    def zmen(self,text):
        """
        Zmeni text v okne
        :param text:
        :return:
        """
        self.canvas.itemconfig(self.canvas_text, text=text)

    def farba(self,farba):
        """
        Zmeni farbu textu v okne
        :param farba:
        :return:
        """
        self.canvas.itemconfig(self.canvas_text, fill=farba)

#------------------------------------------------------------------------------

okna = []

for i in range(20):
    okno = Okno('Text'+str(i))
    okno.farba('#{:06x}'.format(random.randint(0, 0xFFFFFF)))
    okno.zmen('Python '+str(i))
    okna.append(okno)

# print('okna=[{}]' .format(okna))
print(dir(okno))

# okno1 = Okno('Ahoj')
# okno1.zmen('Python')
# okno1.farba('red')
#
# okno2 = Okno('Obed')
# okno2.zmen('Vecera')
# okno2.farba('blue')

# okno1.root.mainloop()
# okno2.root.mainloop()

for j in okna:
    j.root.mainloop()
