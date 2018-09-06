"""
6. Znakové reťazce
"""
# ===============================================================
# 6.1. Typ string
# ===============================================================
# Čo už vieme o znakových reťazcoch:
#
#     reťazec je postupnosť znakov uzavretá v apostrofoch '' alebo v úvodzovkách ""
#     vieme priradiť reťazec do premennej
#     zreťaziť (zlepiť) dva reťazce
#     násobiť (zlepiť viac kópií) reťazca
#     načítať zo vstupu (pomocou input()) a vypisovať (pomocou print())
#     vyrobiť z čísla reťazec (str()), z reťazca číslo (int(), float())
#     rozobrať reťazec vo for-cykle
#
# Postupne prejdeme tieto možnosti práce s reťazcami a doplníme ich o niektoré novinky.
#
# Keďže znakový reťazec je postupnosť znakov uzavretá v apostrofoch '' alebo v úvodzovkách "", platí:
#
#     môže obsahovať ľubovoľné znaky (okrem znaku apostrof ' v '' reťazci, a znaku úvodzovka " v úvodzovkovom "" reťazci)
#     musí sa zmestiť do jedného riadka (nesmie prechádzať do druhého riadka)
#     môže obsahovať špeciálne znaky (zapisujú sa dvomi znakmi, ale pritom v reťazci reprezentujú len jeden), vždy začínajú znakom '\' (opačná lomka):
#         \n - nový riadok
#         \t - tabulátor
#         \' - apostrof
#         \" - úvodzovka
#         \\ - opačná lomka
#---------------------------------------------------------------

print('Monty\nPython') # >>Monty
                       #   Python

# --------------------------------------------------------------
# VIACRIADKOVE RETAZCE
# --------------------------------------------------------------
macek = '''Išiel Macek
do Malacek
šošovičku mlácic'''
# >>> macek   # 'Išiel Macek\ndo Malacek\nšošovičku mlácic'
print(macek)  # Išiel Macek
              # do Malacek
              # šošovičku mlácic

'''tento retazec obsahuje " aj ' a funguje'''            # 'tento retazec obsahuje " aj \' a funguje'
print('''tento retazec obsahuje " aj ' a funguje''')     # tento retazec obsahuje " aj ' a funguje

# --------------------------------------------------------------
# DLZKA RETAZCA
# --------------------------------------------------------------
# Štandardná funkcia len() vráti dĺžku reťazca (špeciálne znaky ako '\n', '\'', a pod. reprezentujú len 1 znak):
a = 'Python'
len(a)                      # 6
len('Peter\' s dog')        # 12
len('\\\\\\')               # 3

# Túto funkciu už vieme naprogramovať aj sami, ale v porovnaní so štandardnou funkciou len() bude oveľa pomalšia:
def dlzka(retazec):
    pocet = 0
    for znak in retazec:
        pocet += 1
    return pocet

dlzka('Python')                 # 6
a = 'x' * 100000000
dlzka(x)                        # 100000000
len(x)                          # 100000000
# --------------------------------------------------------------
# OPERACIA IN
# --------------------------------------------------------------
#Aby sme zistili, či sa v reťazci
#nachádza nejaký konkrétny znak,
# doteraz sme to museli riešiť takto:

def zisti(znak, retazec):
    for z in (retazec):
        if z == znak:
            return True
    return False

zisti('y', 'Python')         # True
zisti('T', 'Python')         # False

#Pritom existuje binárna operácia in, ktorá zisťuje,
#či sa zadaný podreťazec nachádza v nejakom konkrétnom reťazci. Jej tvar je

# >>> podretazec in retazec

#Najčastejšie sa bude využívať v príkaze if a v cykle while, napr.

'nt' in 'Monty Python'          # True
'y P' in 'Monty Python'         # True
'tyPy' in 'Monty Python'        # False
'pyt' in 'Monty Python'         # False

# Na rozdiel od našej vlastnej funkcie zisti(), operácia in funguje nielen
# pre zisťovanie jedného znaku, ale aj pre ľubovoľne dlhý podreťazec.
# Ak niekedy budeme potrebovať negáciu tejto podmienky, môžeme zapísať

#     if not 'a' in retazec:
#     if 'a' not in retazec:        # odporuca sa tento sposob

# --------------------------------------------------------------
# Operácia indexovania [ ]
# --------------------------------------------------------------
#
# Pomocou tejto operácie vieme pristupovať k jednotlivým znakom postupnosti (znakový reťazec je postupnosť znakov). Jej tvar je
#
#     reťazec[číslo]
#
# Celému číslu v hranatých zátvorkách hovoríme index:
#
#     znaky v reťazci sú indexované od 0 do len()-1, t.j. prvý znak v reťazci má index 0, druhý 1, … posledný má index len()-1
#     výsledkom indexovania je vždy 1-znakový reťazec (čo je nový reťazec s kópiou 1 znaku z pôvodného reťazca) alebo chybová správa, keď indexujeme mimo znaky reťazca
#
# Očíslujme znaky reťazca:
#
#     M 	o 	n 	t 	y 	  	P 	y 	t 	h 	o 	n
#     0 	1 	2 	3 	4 	5 	6 	7 	8 	9 	10 	11
#
# Napr. do premennej abc priradíme reťazec 12 znakov a pristupujeme ku niektorým znakom pomocou indexu:

abc = 'Monty Python'
abc[3]                  # 't'
abc[9]                  # 'h'
abc[12]                 # IndexError: string index out of range
abc[len(abc)-1]         # 'n' - posledny znak retazca 'dlzka retazca - 1'

#Často sa indexuje v cykle, kde premenná cyklu nadobúda správneho správne hodnoty indexov, napr.
a = 'Python'
for i in range(len(a)):
    print(i, a[i])

# 0 P
# 1 y
# 2 t
# 3 h
# 4 o
# 5 n

