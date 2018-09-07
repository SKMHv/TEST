# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 10:43:43 2017
@author: michal.hvila
http://howto.py.cz/cap02.htm
http://python.input.sk/04.html
http://mikee.micarp.sk/school/sps-python/
"""
#==============================================================================
#1 Hodnoty, typy, operatory 
#==============================================================================
type("Hello paklasa") #Out[x]: str
type(17)              #Out[x]: int 
type(14.4)            #Out[x]: float
type(15,8)            #TypeError: type() takes 1 or 3 arguments
print(1,000,000)      #1 0 0
type(True)            #Out[x]: bool
type(False)           #Out[x]: bool
#=== Boolovsky vyraz ===
5==5                  #Out[x]: True
5==6                  #Out[x]: False
#=== Operatyory ===
#x < 90 	je menšie ako
#x <= 50 	je menšie alebo rovné
#x == 50 	rovná sa
#x != 77 	nerovná sa
#x > 100 	je väčšie ako
#x >= 90 	je väčšie alebo rovné
#40 < x <= 50 	je väčšie ako ... a zároveň menšie alebo rovné ...
#a < b < c 	a je menšie ako b a zároveň je b menšie ako c
#==============================================================================
#==============================================================================
#2 Premenne
#==============================================================================
n = 17
pi = 3.14159
message = "What's up, DOC?"
print(n, pi, message)


type(n)
type(pi)
type(message)
#==============================
#>Zmena priradenia
#==============================
bruce = 5
print(bruce)
bruce = 7
print(bruce)
#==============================
#>aktualizacia premennej zo zavislostou predchodzej hodnoty
#==============================
x = 10              #inicializacia
x = x ** 2          #aktualizacia
print(x)            #100
#==============================================================================
#3 Mena a klucove slova
#==============================================================================
# Mena premmenych nzacinaju cislom, neobsahuju zakazane znaky(#$^%%) a
# nesmu byt totozne s nazvom klucoveho slova pythonu
#klucove slova:   
# and      del     global      not       with 
# as       elif    if          or        yield
# assert   else    import      pass      True 
# break    except  in          raise     False
# class    finally is          return    None 
# continue for     lambda      try    
# def      from    nonlocal    while 
#==============================================================================
#4 Zakladne datove typy
#==============================================================================
#   Číselné typy
#       int - integers, čísla celá
#       fraction - zlomky
#       float - čísla s desetinnou čárkou
#       complex - komplexní čísla
#       bool - typ s hodnotami True a False
#       NoneType - specielní typ s jedinou hodnotou None
#   Sekvence
#       list - seznam
#       tuple - entice
#       range - řada
#       str - string, řetězec znaků
#       array - kolekce indexovaných prvků (předem určeného) stejného typu
#       bytearray - měnitelná sekvence bajtů pro celá čísla v rozsahu od nuly do 255
#       bytes - neměnitelná verze předchozího typu
#       memoryview - formát pro přístup k vnitřním datům objektů bytes a bytearray bez jejich kopírování
#   Sety
#       set - množina, neuspořádaná kolekce jedinečných objektů
#       frozen set - totéž jako set ale neměnitelná (immutable)
#   Mappings
#       dict - dictionary neboli slovník - neuspořádaná kolekce párových objektů key: value
# 
#==============================================================================
#5 Zmena typu
#==============================================================================
#INT
int(3.9999)    #Out[x]: 3
int(-3.9999)   #Out[x]: -3
int(1.0)       #Out[x]: 1
#FLOAT
float(33)      #Out[x]: 33.0
float(3.14159) #Out[x]: 33.14159
float(1.00)    #Out[x]: 1.0
#STR
str(23)        #Out[x]: '23'
str(3.14159)   #Out[x]: '3.14159'
str(1.00)      #Out[x]: '1.0'
#str(true)     #NameError: name 'true' is not defined 
str(True)      #Out[x]: 'True'
str("25aASD")  #Out[x]: '25aASD'
#==============================================================================
#6 Operandy a operandy
#==============================================================================
x = 2*((3+4-4)-4)+24/6*2  #Out[x]: .....
print(x)                  #Out[x]: 6.0
y = int(x//6)             #Out[x]: .....
print(y)                  #Out[x]: 1
z = x//6                  #Out[x]: ..... //-celociselne delenie
print(z)                  #Out[x]: 1.0 
#==============================
# Operator modulo - urcenie zvysku po deleni
#==============================
q = 7//3
print(q)       #Out[x]: 2
q = 7%3
print(q)       #Out[x]: 1 (operator modulo vrati zvysok)
#prikl. prepocet zadanych sekund
cel_sekund = int(input("Kolko sekund celkom: "))                    # zadaj hodnotu - vstup klavesa
hodiny = cel_sekund // 3600                                         # celocieslne delenie hodnoty s 3600
sekundy_zvysok = cel_sekund % 3600                                  # zvysok delenia hodnoty s 3600
minuty = sekundy_zvysok // 60                                            
sekundy =  sekundy_zvysok % 60
print(cel_sekund,"s = Hodin:",hodiny," Minuty:",minuty," Sekundy:",sekundy)
#==============================================================================
#2.8 Logicke operatory - and, or, not
#==============================================================================
# n%2 == 0 or n%3 == 0 - trvdenie je pravdive ak jedna z podmienok je pravdiva
# x > 0 and x < 10 - tvrdenie je pravdive ak obe podmienky splna x (x je vacsie ako 0 a mensie ako 10)
# not(x>10) tvrdenie je pravdive ak x>10 je nepravda, t.j. x<10

     
   
     

     
#==============================================================================
#2.9 Vstup klavesnice
#==============================================================================     
     
n = input("Zadaj svoje meno - ")    # vyzva pre zadanie hodnoty z klavesnice. Defaultne typ string
print(n) 

m = int(input("Zadaj svoj pocet rokov - ")) # Hodnota zadana z klavesnice iba integer (Cele cislo)
print(m)
#FUNKCIE
#==============================================================================
#3.1 Definicie / Funkcie
#============================================================================== 
  


   
     
     
     
#==============================================================================
#x.x Podmienky
#==============================================================================     
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
    


    

          
       
        

   














 




     
     
     
     
     
     