# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 12:02:27 2017

@author: michal.hvila
"""
#==============================================================================
# PRIRADENIA
#==============================================================================
#
#
#pretypovanie hodnôt
#
#Mená typov int, float a str zároveň súžia ako mená pretypovacích funkcií, 
#ktoré dokážu z jedného typu vyrobiť hodnotu iného typu:
#
#    int(hodnota) z danej hodnoty vyrobí celé číslo, napr.
#        int(3.14) => 3
#        int('37') => 37
#    float(hodnota) z danej hodnoty vyrobí desatinné číslo, napr.
#        float(333) => 333.0
#        float('3.14') => 3.14
#    str(hodnota) z danej hodnoty vyrobí znakový reťazec, napr.
#        str(356) => '356'
#        str(3.14) => '3.14'
#
#Zrejme pretypovanie reťazca na číslo bude fungovať len vtedy, keď je to správne
#zadaný reťazec, inak funkcia vyhlási chybu.
#
#------------------------------------------------------------------------------
#round() zaokrúhľovanie čísla
#
#round(cislo)
#round(cislo, pocet)
#    Parametre:	
#
#        cislo – celé alebo desatinné číslo
#        pocet – celé číslo, ktoré vyjadruje na koľko desatinných miest sa bude
#        zaokrúhľovať; ak je to záporné číslo, zaokrúhľuje sa na počet mocnín desiatky
#
# Funkcia round(cislo) vráti zaokrúhlenú hodnotu zadaného čísla na celé číslo. 
# Funkcia round(cislo, pocet) vráti zaokrúhlené číslo na príslušný počet desatinných miest, napr.
#
#    round(3.14) => 3
#    round(-0.74) => -1
#    round(3.14, 1) => 3.1
#    round(2563, -2) => 2600
#==============================================================================
# PRIRADOVACIE RIKAZY 
#==============================================================================
#Python na tieto prípady aktualizácie nejakej premennej ponúka špeciálny zápis priraďovacieho príkazu:
#
#    meno_premennej += hodnota        # meno_premennej = meno_premennej + hodnota
#    meno_premennej -= hodnota        # meno_premennej = meno_premennej - hodnota
#    meno_premennej *= hodnota        # meno_premennej = meno_premennej * hodnota
#    meno_premennej /= hodnota        # meno_premennej = meno_premennej / hodnota
#    meno_premennej //= hodnota       # meno_premennej = meno_premennej // hodnota
#    meno_premennej %= hodnota        # meno_premennej = meno_premennej % hodnota
#    meno_premennej **= hodnota       # meno_premennej = meno_premennej ** hodnota

#==============================================================================
# ZNAKOVE RETAZCE
#==============================================================================
# - viac riadkove retazce: 
print("#-1.--------------------------------------------------------------------------")
retazec ="""prvy riadok
druhy riadok
treti riadok"""
print(retazec)
print()

#-----------------------------------------------------------------------------
# - zretazenie viacerych hodnot   
print("#-2.--------------------------------------------------------------------------")
meno, x, y = 'A', 180, 225
r = 'bod ' + meno + ' na súradniciach (' + str(x) + ',' + str(y) + ')'
print(r)
#-----------------------------------------------------------------------------
# - sablona prirasdenia
print("#-3.--------------------------------------------------------------------------")
meno, x, y = 'A', 180, 225
print("Bod {} ma suradnice ({},{})".format(meno,x,y))

#==============================================================================
# CYKLUS 
#==============================================================================
# - hodnota lubovolneho typuv cykle
print("#-4.--------------------------------------------------------------------------")
for x in (3, 3.14, 22/7, 8., 1000-1e-36 ):
    x2 = x ** 2
    print("Druha mocnina z", x, "sa rovna =", x2)

#-----------------------------------------------------------------------------
# - retazec ako hodnota cyklu
print("#-5.--------------------------------------------------------------------------")
for pismeno in "Python":
    print(pismeno * 5)

#==============================================================================
# GENEROVANIE POSTUPNOSTI CISEL 
#==============================================================================
#funkcia range()
#
#range(stop)
#range(start, stop)
#range(start, stop, krok)
#    Parametre:	
#        start – prvý prvok vygenerovanej postupnosti (ak chýba, predpokladá sa 0)
#        stop – hodnota, na ktorej sa už generovanie ďalšej hodnoty postupnosti 
#               zastaví - táto hodnota už v postupnosti nebude
#        krok – hodnota, o ktorú sa zvýši (resp. zníži pre záporný krok) každý 
#               nasledovný prvok postupnosti, ak tento parameter chýba, predpokladá sa 1
#
#Väčšinou platí, že do parametra stop nastavíme o 1 väčšiu hodnotu, ako potrebujeme
#poslednú hodnotu vygenerovanej postupnosti.
#
print("#-6.--------------------------------------------------------------------------")
for i in range(5):
    print(i, end=", ")          # 0, 1, 2, 3, 4,
    
print("#-7.--------------------------------------------------------------------------")
for i in range(1, 10):
    print(i, end=", ")          # 1, 2, 3, 4, 5, 6, 7, 8, 9,
    
print("#-8.--------------------------------------------------------------------------")
for i in range(0, 101, 10):
    print(i, end=", ")          # 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
    
print("#-9.--------------------------------------------------------------------------")
for i in range(1, 6):
    print(i, i**1, i**2, i**3)
    
print("#-10.-------------------------------------------------------------------------")
for i in range(1,6):
    print("{:4}{:5}{:5}{:6}" .format(i, i**1, i**2, i**3))
    
print("#-11.-------------------------------------------------------------------------")
n = 5
for i in range(1, n+1):
    print("*" * i)

print("#-12.-------------------------------------------------------------------------")
n = 5
for i in range(n):                          # To iste ako range(0,5)
    print(" " * (n-1-i) + "*" * (2*i+1))    
for i in range(n):
    print(" " * i + "*" * (2*n-2*i-1))

print("#-13.-------------------------------------------------------------------------")
n = 10
sucet = 0
for i in range(1, n + 1):
    sucet = sucet + 1
    print(sucet, end=" + ")                   # 1+2+3+4+5+6+7+8+9+10+
print( "0 =", sucet)

print("#-14.-------------------------------------------------------------------------")
n = 10
sucin = 1
for i in range(1, n + 1):
    print("{:3} * {:6}" .format(i, sucin), end=" = ")   #  1 *     1 = 
    sucin = sucin * i
    print("{:6}" .format(sucin))  
print("----------------------------")    
print("{}! = {}".format(n, sucin))                      # 10! = 3628800

print("#-15.-------------------------------------------------------------------------")   
retazec = "Python"
pocet = 0   
for i in retazec:
    pocet = pocet + 1
print(retazec, " = ", pocet, "- pocet znakov") # Python  =  6 - pocet znakov

print("#-16.-------------------------------------------------------------------------") 
retazec = "Python"
novy = ""
pocet = 0    
for i in retazec:
    novy += 2*i
    pocet += 1

print(novy, " = ", pocet * 2, "- pocet znakov") # Python  =  6 - pocet znakov


#==============================================================================
# VNORENE CYKLY
#==============================================================================
print("#-17.-------------------------------------------------------------------------") 
for i in range(10):
    for j in range(0, 100, 10):
        print(i + j, end=" ")
    print()
        
print("#-18.-------------------------------------------------------------------------")
for i in range(10):
    for j in range(i, 100, 10):
        print(j, end=" ")
    print()

print("#-19.-------------------------------------------------------------------------")

for i in range(0, 100, 10):
    for j in range(i, i + 10):
        print(j, end=" ")
    print()
        
print("#-20.-------------------------------------------------------------------------")
p = 7 
for r in range(1, p + 1):
    for c in range(1, r + 1):
        print(c, end=" ")
    print()
for r in range(1, p + 1):
    for c in range(1, 2 + p - r):
        print(c, end=" ")
    print()

print("#-21.-------------------------------------------------------------------------")
p = 7
c = 1 
for r in range(1, p+ 1):
    for s in range(1, r + 1):
        print(c, end=" ")
        c+=1
    print()    
    
    















