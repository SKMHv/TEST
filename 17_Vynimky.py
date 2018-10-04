"""
#------------------------------------------------------------------------------
# 17 VYNIMKY
# http://input.sk/python2017/17.html
#------------------------------------------------------------------------------
"""
print("------------------------------ 17 -------------------------------------")


# -----------------------------------------
# try - except
# -----------------------------------------
# Blok príkazov medzi try a except bude teraz Python spúšťať „opatrnejšie“, t.j. ak pri ich vykonávaní nastane
# uvedená chyba (meno chyby za except), vykonávanie bloku príkazov sa okamžite ukončí a pokračuje sa príkazmi
# za except, pritom Python zruší chybový stav, v ktorom sa práve nachádzal. Ďalej sa pokračuje v príkazoch
# za touto konštrukciou.

# Ak pri opatrnejšom vykonávaní bloku príkazov uvedená chyba nenastane, tak príkazy za except sa preskočia
# a normálne sa pokračuje v príkazoch za konštrukciou.

# Ukážme to na predchádzajúcom príklade (pomocnú funkciu test_cele_cislo() teraz už nepotrebujeme):

def cislo():
    while True:
        vstup = input('zadaj cislo: ')
        try:
            return int(vstup)
        except ValueError:
            print('*** chybne zadane cele cislo ***')

# To isté by sa dalo zapísať aj niekoľkými inými spôsobmi, napr.

def cislo():
    while True:
        try:
            return int(input('zadaj cislo: '))
        except ValueError:
            print('*** chybne zadane cele cislo ***')

def cislo():
    while True:
        try:
            vysledok = int(input('zadaj cislo: '))
            break
        except ValueError:
            print('*** chybne zadane cele cislo ***')
    return vysledok

def cislo():
    ok = False
    while not ok:
        try:
            vysledok = int(input('zadaj cislo: '))
            ok = True
        except ValueError:
            print('*** chybne zadane cele cislo ***')
    return vysledok


# Na predchádzajúcom príklade sme videli, že odteraz bude pre nás dôležité meno chyby (napr. ako v predchádzajúcom
# príklade ValueError). Mená chýb nám prezradí Python, keď vyskúšame niektoré konkrétne situácie, napr.

# >>> 1+'2'
# ...
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# >>> 12/0
# ...
# ZeroDivisionError: division by zero
# >>> x+1
# ...
# NameError: name 'x' is not defined
# >>> open('')
# ...
# FileNotFoundError: [Errno 2] No such file or directory: ''
# >>> [1,2,3][10]
# ...
# IndexError: list index out of range
# >>> 5()
# ...
# TypeError: 'int' object is not callable
# >>> ''.x
# ...
# AttributeError: 'str' object has no attribute 'x'
# >>> 2**10000/1.
# ...
# OverflowError: int too large to convert to float
# >>> import x
# ...
# ImportError: No module named 'x'
# >>> def t(): x += 1
# >>> t()

# ----------------------------------------------------------
# Spracovanie viacerých výnimiek
# ----------------------------------------------------------

# Pomocou try a except môžeme zachytiť aj viac chýb ako jednu. V ďalšom príklade si funkcia vyžiada celé číslo,
# ktoré bude indexom do nejakého zoznamu. Funkcia potom vypíše hodnotu prvku s týmto indexom.
# Môžu tu nastať dve rôzne výnimky:

#    * ValueError pre zle zadané celé číslo indexu
#    * IndexError pre index mimo rozsah zoznamu

def zisti(zoznam):
    while True:
        try:
            vstup = input('Zadaj index: ')
            index = int(vstup)
            print('Prvok zoznamu = ', zoznam[index])
            break
        except ValueError:
            print('Chybne zadane cele cislo !!!')
        except IndexError:
            print('Index mimo rozsah !!!')

# ----- TEST -----------

zisti(['prvy', 'druhy', 'treti', 'stvrty'])

# Zadaj index: 2.
# Chybne zadane cele cislo !!!
# Zadaj index: 55
# Index mimo rozsah !!!
# Zadaj index: 1
# Prvok zoznamu =  druhy

# To isté by sme dosiahli aj vtedy, keby sme to zapísali pomocou dvoch vnorených príkazov try:

def zisti(zoznam):
    while True:
        try:
            try:
                vstup = input('zadaj index: ')
                index = int(vstup)
                print('prvok zoznamu =', zoznam[index])
                break
            except ValueError:
                print('*** chybne zadane cele cislo ***')
        except IndexError:
            print('*** index mimo rozsah zoznamu ***')

# ----------------------------------------------------------
# Zlúčenie výnimiek
# ----------------------------------------------------------

# Niekedy sa môže hodiť, keď máme pre rôzne výnimky spoločný kód. Za except môžeme uviesť aj viac rôznych mien
# výnimiek, ale musíme ich uzavrieť do zátvoriek (urobiť z nich tuple), napr.

def zisti(zoznam):
    while True:
        try:
            print('prvok zoznamu =', zoznam[int(input('zadaj index: '))])
            break
        except (ValueError, IndexError):
            print('*** chybne zadany index zoznamu ***')

zisti(['prvy', 'druhy', 'treti', 'stvrty'])


# zadaj index: 22
# *** chybne zadany index zoznamu ***
# zadaj index: 2a
# *** chybne zadany index zoznamu ***
# zadaj index: 3
# prvok zoznamu = stvrty

# Uvedomte si, že pri takomto zlučovaní výnimiek môžeme stratiť detailnejšiu informáciu o tom, čo sa v skutočnosti
# udialo.

# Príkaz try - except môžeme použiť aj bez uvedenia mena chyby: vtedy to označuje zachytenie všetkých typov chýb, napr.

def zisti(zoznam):
    while True:
        try:
            print('prvok zoznamu =', zoznam[int(input('zadaj index: '))])
            break
        except:
            print('*** chybne zadany index zoznamu ***')



# ----------------------------------------------------------
# Práca so súbormi
# ----------------------------------------------------------

# Pri práci so súbormi výnimky vznikajú veľmi často a nie je jednoduché ošetriť všetky situácie pomocou
# podmienených príkazov. Najčastejšou chybou je neexistujúci súbor:

try:
    with open('x.txt') as subor:
        cislo = int(subor.readline())
except FileNotFoundError:
    print('*** neexistujuci subor ***')
    cislo = 0
except (ValueError, TypeError):
    print('*** prvy riadok suboru neobsahuje cele cislo ***')
    cislo = 10

# Prípadne sa môže hodiť pomocná funkcia, ktorá zistí, či súbor s daným menom existuje:

def existuje(meno_suboru):
    try:
        with open(meno_suboru):
            return True
    except (TypeError, OSError, FileNotFoundError):
        return False

# ----------------------------------------------------------
# Vyvolanie výnimky
# ----------------------------------------------------------

# V niektorých situáciách sa nám môže hodiť vyvolanie vzniknutej chyby aj napriek tomu,
# že ju vieme zachytiť príkazom try - except. Slúži na to nový príkaz raise, ktorý má niekoľko variantov.
# Prvý z nich môžete vidieť v upravenej verzii funkcie cislo(). Funkcia sa najprv 3-krát pokúsi prečítať
# číslo zo vstupu, a ak sa jej to napriek tomu nepodarí, rezignuje a vyvolá známu chybu ValueError:

def cislo():
    pokus = 0
    while True:
        try:
            return int(input('zadaj cislo: '))
        except ValueError:
            pokus += 1
            if pokus >= 3:
                raise
            print('*** chybne zadane cele cislo ***')

# >>> cislo()
# zadaj cislo: jeden
# *** chybne zadane cele cislo ***
# zadaj cislo: dva
# *** chybne zadane cele cislo ***
# zadaj cislo: tri
# ...
# ValueError: invalid literal for int() with base 10: 'tri'

# Pomocou príkazu raise môžeme vyvolať nielen práve zachytenú výnimku, ale môžeme vyvolať ľubovoľnú inú chybu
# aj s vlastným komentárom, ktorý sa pri nej vypíše, napr.

# raise ValueError('chybne zadane cele cislo')
# raise ZeroDivisionError('delenie nulou')
# raise TypeError('dnes sa ti vobec nedari')

# ----------------------------------------------------------
# Príklad s metódou index()
# ----------------------------------------------------------

# Poznáme už metódu index(), ktorá v zozname (typ list, tuple alebo str) nájde prvý výskyt nejakej hodnoty.
# Metóda je zaujímavá tým, že vyvolá výnimku ValueError, ak sa táto hodnota v zozname nenachádza.
# Kým sme nepoznali odchytávanie výnimiek, väčšinou sme museli najprv kontrolovať, či sa tam príslušný prvok
# nachádza a až potom, keď sa nachádza, volali sme index(), napr.


def nahrad(zoznam, h1, h2):
    if h1 in zoznam:
        i = zoznam.index(h1)
        zoznam[i] = h2

# pomoocu try - except to vyriešime výrazne efektívnejšie:


def nahrad(zoznam, h1, h2):
    try:
        i = zoznam.index(h1)
        zoznam[i] = h2
    except ValueError:
        pass

# Táto metóda index(), ktorá funguje pre jednorozmerné zoznamy, nás môže inšpirovať aj na úlohu, v ktorej
# budeme hľadať indexy do dvojrozmernej tabuľky. Napíšme funkciu hladaj(zoznam, hodnota), ktorá hľadá prvý
# výskyt danej hodnoty v dvojrozmernom zozname a ak taký prvok nájde, vráti jeho číslo riadku a číslo stĺpca.
# Ak sa tam taký prvok nenachádza, funkcia by mala vyvolať rovnakú výnimku, ako to robila pôvodná metóda index(),
#  t.j. ValueError: hodnota is not in list. Zapíšme riešenie dvoma vnorenými cyklami:

def hladaj(zoznam, hodnota):
    for r in range(len(zoznam)):
        for s in range(len(zoznam[r])):
            if zoznam[r][s] == hodnota:
                return r, s
    raise ValueError(f'{hodnota!r} is not in list')


print(hladaj(((2,5),(1,6),(3,4),(9,8)), 4))    # (2,1)
print(hladaj(((2,5),(1,6),(3,4),(9,8)), 7))    # line 16, in hladaj raise #ValueError(f'{hodnota!r} is not in list') RuntimeError: No active exception to reraise


# Táto metóda index(), ktorá funguje pre jednorozmerné zoznamy, nás môže inšpirovať aj na úlohu, v ktorej
# budeme hľadať indexy do dvojrozmernej tabuľky. Napíšme funkciu hladaj(zoznam, hodnota), ktorá hľadá prvý
# výskyt danej hodnoty v dvojrozmernom zozname a ak taký prvok nájde, vráti jeho číslo riadku a číslo stĺpca.
# Ak sa tam taký prvok nenachádza, funkcia by mala vyvolať rovnakú výnimku, ako to robila pôvodná metóda index(),
#  t.j. ValueError: hodnota is not in list. Zapíšme riešenie dvoma vnorenými cyklami:

def hladaj(zoznam, hodnota):
    for r in range(len(zoznam)):
        for s in range(len(zoznam[r])):
            if zoznam[r][s] == hodnota:
                return r, s
    raise ValueError(f'{hodnota!r} is not in list')


print(hladaj(((2,5),(1,6),(3,4),(9,8)), 4))    # (2,1)
print(hladaj(((2,5),(1,6),(3,4),(9,8)), 7))    # line 16, in hladaj raise #ValueError(f'{hodnota!r} is not in list') RuntimeError: No active exception to reraise

# alebo to isté zápis pomocou štandardnej funkcie enumerate():

def hladaj(zoznam, hodnota):
    for r, riadok in enumerate(zoznam):
        for s, prvok in enumerate(riadok):
            if prvok == hodnota:
                return r, s
    raise ValueError(f'{hodnota!r} is not in list')

# Hoci je toto správne riešenie, vieme ho zapísať aj efektívnejšie
# pomocou volania metódy index():

def hladaj(zoznam, hodnota):
    for r, riadok in enumerate(zoznam):
        try:
            s = riadok.index(hodnota)
            return r, s
        except ValueError:
            pass
    raise ValueError(f'{hodnota!r} is not in list')

# Ak si ale uvedomíme, že neúspešné hľadanie prvku v r-tom riadku zoznamu pomocou index() vyvolá presne tú istú chybu,
# ktorú sme zachytili a potom znovu vyvolali, môžeme to celé skrátiť takto:

def hladaj(zoznam, hodnota):
    for r, riadok in enumerate(zoznam):
        try:
            s = riadok.index(hodnota)
            return r, s
        except ValueError:
            if r == len(zoznam)-1:
                raise

# Teda zachytená chyba ValueError v poslednom riadku dvojrozmerného zoznamu označuje,
# že sa hodnota nenachádza v žiadnom riadku zoznamu a teda sa opätovne vyvolá zachytená
# chyba. (Zamyslite sa, ako bude toto riešenie fungovať pre prázdny dvojrozmerný zoznam,
# teda zoznam, ktorý neobsahuje ani jeden riadok).



















