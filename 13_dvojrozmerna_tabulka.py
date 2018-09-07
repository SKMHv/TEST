
# ---------------------------------
# Tabuľka farieb
# ----------------------------------

# Ukážme dve malé aplikácie, v ktorých vytvoríme dvojrozmerný zoznam náhodných farieb,
# potom ho vykreslíme do grafickej plochy ako postupnosť malých farebných štvorčekov
# - vznikne farebná mozaika a na záver to otestujeme klikaním myšou.

# Prvý program vygeneruje dvojrozmerný zoznam náhodných farieb, vykreslí ho a uloží do textového súboru:

import  random
from tkinter import *

master = Tk()

w = Canvas(master, width=200, height=400)
w.pack()


tab = []
for i in range(20):                                         # pocet riadkov 20
    p=[]
    for j in range(30):                                     # pocet stlpcov 30
        p.append(f'#{random.randrange(256**3):06x}')        # pridaj farbu do pola stlpcov p[]
    tab.append(p)                                           # do tabulky tab[] pridaj prvok riadku s farbami

d, x0, y0 = 10, 30, 10                                      # d = dlzka, X0,y0 = zaciatocna suradnica
for i in range(len(tab)):                                   # od 0 - 19
    for j in range(len(tab[i])):                            # od 0 - 30
        x, y = d*j+x0, d*i+y0                               # vyrataj suradnice x,y
        w.create_rectangle(x, y, x+d, y+d, fill=tab[i][j], outline='')  # kresli stvorec

with open('FILE/tabulka_farieb.txt', 'w') as subor:        # vytvor / otvor subor tabulka_farieb.txt na editovanie
    for riadok in tab:                                      # pre kazdy riadok z tabulky tab[]
        print(' '.join(riadok), file=subor)                 # zapis prvky z riadku ako string s odelovacom ' '


mainloop()


# V druhej časti programu už nebudeme generovať dvojrozmerný zoznam, ale prečítame ho z uloženého súboru.
# Keďže plánujeme klikaním meniť farby kliknutých štvorčekov, musíme si pamätať ich identifikačné čísla,
# ktoré vznikajú pri ich vykreslení pomocou create_rectangle() - použijeme na to pomocnú dvojrozmernú tabuľku re
# (rovnakých rozmerov ako tabuľka farieb). Na záver doplníme funkciu na zabezpečenie klikania: kliknutý štvorček
# sa zafarbí, napr. na bielo:

import  random
from tkinter import *
from DEF import vypis

master = Tk()
w = Canvas(master, width=360, height=260)
w.pack()

# naplnenie tabulky tab[] prvkami zo suboru tabulka_farieb.txt
tab = []
with open('FILE/tabulka_farieb.txt', 'r') as subor:        # otvor subor tabulka_farieb.txt na citanie
    for riadok in subor:                                    # pre kazdy riadok suboru
       tab.append(riadok.split())                           # pridaj riadok ako prvok do tabulky tab[]


# inicializujem pomocnu tabulku re[][] pre id nakreslenych stvorcov
re = []
for i in range(len(tab)):
    re.append([0] * len(tab[i]))

vypis(re)           # vypis pomocne pole re[]

# vykresli a id. cisla uloz do zoznamu re[][]
d, x0, y0 = 10, 30, 10
for i in range(len(tab)):
    for j in range(len(tab[i])):
        x, y = d*j + x0, d*i + y0
        re[i][j] = w.create_rectangle(x, y, x+d, y+d, fill=tab[i][j], outline='')

def klik(event):
    stlpec, riadok = (event.x - x0) // d, (event.y - y0) // d
    if 0 <= riadok < len(tab) and 0 <= stlpec < len(tab[riadok]):
        w.itemconfig(re[riadok][stlpec], fill='white')
        #tab[riadok][stlpec] = 'white'

w.bind('<Button-1>', klik)

mainloop()

# -----------------------
# Hra LIFE
# -----------------------
"""
Pravidlá:

v nekonečnej štvorcovej sieti žijú bunky, ktoré sa rôzne rozmnožujú, resp. umierajú
v každom políčku siete je buď živá bunka, alebo je políčko prázdne (budeme označovať ako 1 a 0)
každé políčko má 8 susedov (vodorovne, zvislo aj po uhlopriečke)
v každej generácii sa s každým jedným políčkom:
    - ak je na políčku bunka a má práve 2 alebo 3 susedov, tak táto bunka prežije aj do ďalšej generácie
    - ak je na políčku bunka a má buď 0 alebo 1 suseda, alebo viac ako 3 susedov, tak bunka na tomto políčku do ďalšej generácie neprežije (umiera)
    - ak má prázdne políčko presne na troch susediacich políčkach živé bunky, tak sa tu v ďalšej generácii narodí nová bunka

Štvorcovú sieť s 0 a 1 budeme ukladať v dvojrozmernej tabuľke veľkosti n x n. V tejto tabuľke je momentálna generácia bunkových živočíchov.
Na to, aby sme vyrobili novú generáciu, si pripravíme pomocnú tabuľku rovnakej veľkosti a do nej budeme postupne zapisovať bunky novej generácie.
Keď už bude celá táto pomocná tabuľka hotová, prekopírujeme ju do pôvodnej tabuľky. Dvojrozmernú tabuľku budeme vykresľovať do grafickej plochy.
"""

import  random
from tkinter import *

master = Tk()
w = Canvas(master, width=600, height=600, bg = "white")
w.pack()


def inicializuj_siet():
    """
    Vykresli maticu nxn stvorcov o velikosti d
    :return: viacrozmerne pole re[]
    """
    d, x0, y0 = 10, 40, 70
    xt, yt = x0+(n*d)/2, y0-35
    re = []
    global text
    text = w.create_text(xt, yt ,text='1. GENERACIA', font='arial 25')
    for i in range(n):
        re.append([0]*n)
        for j in range(n):
            x, y = d*j+x0, d*i+y0
            re[i][j] = w.create_rectangle(x, y, x+d, y+d, fill="white", outline="grey")
    return re


def nahodne():
    """
    Vygeneruje viacrozmerne pole siet[p[0],p[1],..p[n]] s nahodnymi hodnotami 0 a 1
    :return: viacrozmerne pole siet[]
    """
    siet = []

    for i in range(n):
        p = []
        for j in range(n):
            p.append(random.randrange(2))   # pre urcenu siet treba 2 zmenit na 1
        siet.append(p)

    # siet[5][2] = siet[5][3] = siet[5][4] = siet[4][4] = siet[3][3] = 1        # odkomentovat ak chcem urcit siet sam
    return siet

def kresli(t):
    for i in range(n):
        for j in range(n):
            farba = ['white', 'black'][siet[i][j]]
            w.itemconfig(re[i][j], outline='red', width=2)
            w.update()
            w.after(t)
            w.itemconfig(re[i][j], fill=farba, outline="grey",width=1)
            w.update()



def pocet_susedov(rr, ss):
    pocet = 0
    for r in(rr-1, rr, rr+1):
        for s in(ss-1, ss, ss+1):
                if 0 <= r < n and 0 <= s < n:
                    pocet += siet[r][s]
    return pocet - siet[rr][ss]

def nova():
    siet1 = []
    for i in range (n):
        siet1.append([0] * n)

    for i in range(n):
        for j in range(n):
            p = pocet_susedov(i, j)
            if p == 3 or p == 2 and siet[i][j]:
                siet1[i][j] = 1

    siet[:] = siet1
    kresli(0)


def rob(kolko=100):
    for i in range(kolko):
        w.itemconfig(text, text='{}. GENERACIA' .format(i+2))
        nova()

# START

n = 50
re = inicializuj_siet()         # vykresli siet
#print('re - ', re)
siet = nahodne()
#print('siet = ', siet)
kresli(0)
rob()

mainloop()



# -----------------------
# CVICENIA - http://python.input.sk/13.html#vytvaranie-dvojrozmernych-tabuliek
# -----------------------


# 1. Funkcia vypis_sucty(tab) vypíše súčty prvkov v jednotlivých riadkoch tabuľky, súčty vypisuje vedľa seba.
#    >>> vypis_sucty([[1, 2, 3], [4], [5, 6]])
#       6 4 11

def vypis_sucty(tab):
    for i in tab:
        sucet = 0
        #print('riesim i - ', i)
        for j in i:
            sucet += j
        print(sucet, end=' ')

a = [[1,2,3],[4],[5,6]]
vypis_sucty(a)


# 2. Funkcia zoznam_suctov(tab) počíta súčty prvkov v riadkoch (podobne ako v predchádzajúcej úlohe),
#    ale tieto súčty nevypisuje ale ukladá do výsledného zoznamu.
#    >>> suc = zoznam_suctov([[1, 2, 3], [4], [5, 6]])
#    >>> suc
#        [6, 4, 11]

def zoznam_suctov(tab):
    vysl =[]
    for i in tab:
        sucet = 0
        print('riesim i - ', i)
        for j in i:
            sucet += j
        vysl.append(sucet)
    return vysl


a = [[1,2,3],[4],[5,6]]
suc = zoznam_suctov(a)
print(suc)


# 3. Funkcia pridaj_sucty(tab) podobne ako predchádzajúce úlohy počíta súčty po riadkoch, ale ich ukladá na koniec každého riadka tabuľky.
#       >>> a = [[1, 2, 3], [4], [5, 6]]
#       >>> pridaj_sucty(a)
#       >>> a
#       [[1, 2, 3, 6], [4, 4], [5, 6, 11]]


def pridaj_sucty(tab):
    for i in tab:
        sucet = 0
        print('riesim i - ', i)
        for j in i:
            sucet += j
        i.append(sucet)

a = [[1,2,3],[4],[5,6]]
pridaj_sucty(a)
print(a)

# 4. Funkcia preklop(matica) vyrobí novú maticu (dvojrozmernú tabuľku), v ktorej bude pôvodná preklopená okolo hlavnej
#    uhlopriečky. Predpokladáme, že všetky riadky majú rovnakú dĺžku.
#       >>> p = [[1, 2], [5, 6], [3, 4]]
#       >>> q = preklop(p)
#       >>> q
#       [[1, 5, 3], [2, 6, 4]]

def preklop(matica):
    # inicializuj prazdnu maticu
    inv_matica = [[0]*len(matica), [0]*len(matica)]
    print('inv_matica = ', inv_matica)

    # preklapam maticu
    for i in range(len(matica)):
        n = 0
        for j in matica[i]:
            inv_matica[n][i] = j
            print('inv_matica[{}][{}] - {}'.format(n,i,inv_matica[n][i]))
            n += 1
    print('----- preklopenie ukoncene -----')
    return inv_matica

p = [[1, 2], [5, 6], [3, 4]]
q = preklop(p)
print(q)

# 5. Funkcia preklop_sa(matica) pracuje ako predchádzajúci príklad, ale namiesto výslednej matice
#    (teda funkcia nič nevracia) funkcia zmení samotnú vstupnú maticu.
#
#    >>> p = [[1, 2], [5, 6], [3, 4]]
#    >>> preklop_sa(p)
#    >>> p
#        [[1, 5, 3], [2, 6, 4]]

def preklop_sa(matica):
    # inicializuj prazdnu inv maticu
    inv_matica = []
    for i in range(len(matica[0])):
        inv_matica.append([0]*len(matica))

    print('inv_matica = ', inv_matica)
    print('----- inverzna matica inicializovana -----\n')

    # preklapam maticu
    for i in range(len(matica)):
        n = 0
        for j in matica[i]:
            inv_matica[n][i] = j
           # print('inv_matica[{}][{}] - {}'.format(n,i,inv_matica[n][i]))
            n += 1
    print('inv_matica - ', inv_matica)
    print('----- inverzna matica naplnena -----\n')

    matica.clear()
    print('matica - ', matica)
    print('----- povodna matica vynulovana -----\n')

    for i in inv_matica:
        matica.append(i)
    print(matica)
    print('----- povodna matica naplnena -----\n')

p = [[1, 2], [5, 6], [3, 4]]
preklop_sa(p)
print(p)


# 6. Funkcia zisti_dlzky(tab) zistí, či sú všetky riadky vstupnej tabuľky rovnako dlhé, ak áno,
#    funkcia vráti túto dĺžku, inak vráti None.
#
#       >>> p = [[1, 2], [3, 4], [5, 6]]
#       >>> zisti_dlzky(p)
#           2
#       >>> zisti_dlzky([[1, 2, 3]])
#           3
#       >>> zisti_dlzky([[], [1, 2, 3]])    # vráti None
#       >>>


def zisti_dlzky(tab):
    dlzky = []

    for i in tab:
        dlzky.append(len(i))

    print('dlzky - ', dlzky)
    print('------------ dlzky su nacitane ------------')

    dlzka = dlzky[0]
    if len(tab) > 1 and len(tab) != 0:
        for j in dlzky[1:]:
            if j != dlzka:
                return
            else:
                return dlzka

    else:
        return dlzka


p = [[1, 2], [3, 4], [5, 6]]
print('1. [[1, 2], [3, 4], [5, 6]] = ', zisti_dlzky(p),'\n')
print('2. [[1, 2, 3]] = ', zisti_dlzky([[1, 2, 3]]), '\n')
print('3. [[], [1, 2, 3]] = ', zisti_dlzky([[], [1, 2, 3]]), '\n')
print('4. [[]] = ', zisti_dlzky([[]]), '\n')
print('5. [[],[],[]] = ', zisti_dlzky([[],[],[]]), '\n')
print('6. [[],[],[1]] = ', zisti_dlzky([[],[],[1]]), '\n')

# 7. Funkcia dopln(tab) doplní do vstupnej tabuľky do každého riadka minimálny počet None tak, aby mali všetky riadky rovnakú dĺžku.
#
#       >>> a = [[5, 6], [1, 2, 3], [4]]
#       >>> dopln(a)
#       >>> a
#       [[5, 6, None], [1, 2, 3], [4, None, None]]

def dopln(tab):

    dlzky = []
    for i in tab:
        dlzky.append(len(i))

    print('dlzky - ', dlzky)

    max_dlzka = max(dlzky)
    print('max dlzka - ', max_dlzka)


    print('------------ dlzky su nacitane a zistena najvacsia ------------')

    for j in tab:
        if len(j) < max_dlzka:
            for r in range(max_dlzka - len(j)):
                j.append(None)
        print('j = ', j)
    print('----------------------------------------------------------------')

a = [[5, 6], [1, 2, 3], [4]]
dopln(a)
print(a)

# 8. Zistite, čo počíta

def test(mat):
    vysl, n = 0, len(mat)
    for i in range(n):
        for j in range(n):
            print('{} += abs({}) - {}' .format(vysl,mat[i][j], mat[j][i]), end = " => ")
            vysl += abs(mat[i][j] - mat[j][i])
            print(vysl)

    return vysl

a = [[1, 2], [1, 1]]
b = [[1, 2, 3], [2, 2, 1], [3, 1, 3]]

print(test(a))  # 2
print(test(b))  # 0


# 9. Funkcia zisti(tab1, tab2) zistí, či majú dve vstupné tabuľky úplne rovnaké rozmery,
#    t. j. majú rovnaký počet rovnakodlhých riadkov.
#
#         >>> a = [[5, 6], [1, 2, 3], [4]]
#         >>> b = [[0, 0], [0, 0, 0], [0]]
#         >>> zisti(a, b)
#             True
#         >>> del b[-1][-1]
#         >>> zisti(a, b)
#             False

def zisti(tab1, tab2):
    if len(tab1) != len(tab2):
        return False
    else:
        for i in range(len(tab1)):
            if len(tab1[i]) != len(tab2[i]):
                return False
        return True

a = [[5, 6], [1, 2, 3], [4]]
b = [[0, 0], [0, 0, 0], [0]]
print(zisti(a, b))      # True
del b[-1][-1]
print(zisti(a, b))      # False

# 10. Funkcia sucet(tab1, tab2) vráti novú tabuľku, ktorá je súčtom dvoch vstupných rovnakoveľkých číselných tabuliek.
#     Funkcia vráti takú tabuľku, v ktorej je každý prvok súčtom dvoch prvkov zo vstupných tabuliek s rovnakým indexom.
#
#         >>> a = [[5, 6], [1, 2, 3], [4]]
#         >>> b = [[-1, -3], [-2, 0, 1], [2]]
#         >>> c = sucet(a, b)
#         >>> c
#             [[4, 3], [-1, 2, 4], [6]]

def sucet(tab1, tab2):
    from DEF import zisti
    print()

    if zisti(tab1, tab2) != False:
        print('Su rovnako velke ------')
        tab_suctov = []

        for i in range(len(tab1)):
            j_sucty = []
            for j in range(len(tab1[i])):
                j_sucty.append(tab1[i][j] + tab2[i][j])
            tab_suctov.append(j_sucty)

        return tab_suctov

    else:
        return print('Tabulky nie su rovnako velke !!!')


c = 0
a = [[5, 6], [1, 2, 3], [4]]
b = [[-1, -3], [-2, 0, 1], [2]]
c = sucet(a, b)                 # [[4, 3], [-1, 2, 4], [6]]
print('---------------------------------------------------------')

print(c)


# 11. Textový súbor v každom riadku obsahuje niekoľko slov, oddelených medzerou (riadok môže byť aj prázdny).
#     Funkcia citaj(meno_suboru) prečíta tento súbor a vyrobí z neho dvojrozmernú tabuľku: každý riadok tabuľky zodpovedá jednému riadku súboru,
#
#       napr. ak súbor text.txt:
#
#            anicka dusicka
#            kde si bola
#            ked si si cizmicky
#            zarosila
#
#        potom:
#
#         >>> s = citaj('text.txt')
#         >>> s
#             [['anicka', 'dusicka'], ['kde', 'si', 'bola'], ['ked', 'si', 'si', 'cizmicky'], ['zarosila']]



def citaj(meno_suboru):
    tab = []

    with open(meno_suboru, 'r') as subor:    # otvor subor na citanie
        for riadok in subor:                 # pre kazdy riadok suboru
            tab.append(riadok.split())       # pridaj riadok ako prvok do tabulky tab[]

    return tab

subor = '/home/echolom/PycharmProjects/untitled1/FILE/subor_text.txt'
print('------------------------------------------------------------')

print(citaj(subor))       # [['anicka', 'dusicka'], ['kde', 'si', 'bola'], ['ked', 'si', 'si', 'cizmicky'], ['zarosila']]


# 12. Funkcia zapis(tab, meno_suboru) je opačná k predchádzajúcemu príkladu: zapíše danú dvojrozmernú tabuľku slov do súboru.
#         napr.
#
#             >>> s = [['ANICKA', 'dusicka'], ['kde', 'si', 'bola'], ['ked', 'si', 'si', 'cizmicky'], ['zarosila']]
#             >>> zapis(s, 'text1.txt')
#
#                 vytvorí rovnaký súbor ako bol text.txt


def zapis(tab, meno_suboru):

    with open(meno_suboru, 'w') as subor:                           # otvory/vytvory subor na zapis
        for riadok in tab:                                          # pre kazdy riadok tabulky
            print(' '.join([str(i) for i in riadok]), file=subor)   # vsetke prvky riadku zmen na str, prvky oddel ' ' a zapis do suboru
    print('dokoncene - do suboru  boli zapisane riadky')


subor = '/home/echolom/PycharmProjects/untitled1/FILE/subor_cislo.txt'
#s = [['anicka', 'dusicka'], ['kde', 'si', 'bola'], ['ked', 'si', 'si', 'cizmicky'], ['zarosila']]
s = [[1, 11, 21], [345], [-5, 10]]
print('------------------------------------------------------------')

zapis(s,subor)

# 13. Funkcia citaj_cisla(meno_suboru) bude podobná funkcii citaj(meno_suboru) z (11) úlohy,
#     let táto predpokladá, že vstupný súbor obsahuje len celé čísla. Funkcia vráti dvojrozmernú tabuľku čísel.
#
#       napr.pre textový súbor z(12) úlohy:
#
#           >>> tab = citaj_cisla('cisla.txt')
#           >>> tab
#               [[1, 11, 21], [345], [-5, 10]]


def citaj_cisla(meno_suboru):
    tab = []
    n = 0
    with open(meno_suboru, 'r') as subor:            # otvory/vytvory subor na zapis
        for riadok in subor:                         # pre kazdy riadok suboru
            print(type(riadok))
            tab.append(riadok.split())               # pridaj riadok ako prvok do tabulky tab[]
            tab[n] = [int(i) for i in tab[n]]        # premen prvky riadku v tab[] na integer
            n += 1
    return tab


subor = '/home/echolom/PycharmProjects/untitled1/FILE/subor_cislo.txt'

print('------------------------------------------------------------')

a = citaj_cisla(subor)
print(a)                        # [[1, 11, 21], [345], [-5, 10]]

# 14. Funkcia prvky(tab) z dvojrozmernej tabuľky vyrobí (funkcia vráti) jednorozmernú:
#     všetky prvky postupne pridáva do výsledného zoznamu.
#
#         >>> a = [[5, 6], [1, 2, 3], [4]]
#         >>> b = prvky(a)
#         >>> b
#         [5, 6, 1, 2, 3, 4]


def prvky(tab):
    print()
    vysl_tab = []
    for riadok in tab:
        for i in riadok:
            #print('tlacim i -', i)
            vysl_tab.append(i)

    return vysl_tab

a = [[5, 6], [1, 2, 3], [4]]
b = prvky(a)
print(b)            # [5, 6, 1, 2, 3, 4]


# 15. Funkcia vyrob(pr, ps, hodnoty) vyrobí dvojrozmernú tabuľku s počtom riadkov pr a počtom stĺpcov ps.
#     Prvky zoznamu hodnoty postupne priradzuje po riadkoch do novovytváranej tabuľky.
#     Ak je vstupný zoznam hodnôt kratší ako potrebujeme, začne z neho čítať od začiatku.
#
#     napr.
#
#         >>> xy = vyrob(3, 2, [3, 5, 7])
#         >>> xy
#         [[3, 5], [7, 3], [5, 7]]
#         >>> vyrob(3, 3, list(range(1, 20, 2)))
#         [[1, 3, 5], [7, 9, 11], [13, 15, 17]]


def vyrob(pr, ps, hodnoty):
    print()
    new_tab = []
    n = 0
    print('----- inicializujem tabulku -----')

    for r in range(pr):
        new_tab.append([0]*ps)
        for s in range(ps):
            new_tab[r][s] = hodnoty[n]
            if n != len(hodnoty)-1:
                n += 1
            else:
                n = 0

#    print("new_tab - ", new_tab)

    return  new_tab



xy = vyrob(3, 2, [3, 5, 7])
print('--------------------------------------------')
print(xy)           # [[3, 5], [7, 3], [5, 7]]

print(vyrob(3, 3, list(range(1, 20, 2))))  # [[1, 3, 5], [7, 9, 11], [13, 15, 17]]


# 16. Vytvorte (napr. v notepade) textový súbor, ktorý obsahuje aspoň 5 riadkov s piatimi farbami (len mená farieb).
#     Napíšte funkciu kruhy(meno_suboru), ktorá prečíta tento súbor a farby zo súboru vykreslí ako farebné kruhy.
#     Tieto budú vykreslené tesne vedľa saba po riadkoch. Súbor najprv prečítajte do dvojrozmernej tabuľky farieb a potom vykresľujte.
#
#         Text. subor obsahuje:
#
#         yellow yellow blus yellow yellow
#         yellow blue yellow blue yellow
#         blue yellow red yellow blue
#         yellow blue yellow blue yellow
#         yellow yellow blue yellow yellow
#
#         Volanie:
#
#         >>> kruhy('farby.txt')
#             vykreslí 25 kruhov v piatich radoch po 5


from tkinter import *

def kruhy(meno_suboru):
    master = Tk()
    w = Canvas(master, width=400, height=400, bg = 'black')
    w.pack()

    # naplnenie tabulky tab[] prvkami zo suboru tabulka_farieb.txt
    tab = []
    with open(meno_suboru, 'r') as subor:        # otvor subor tabulka_farieb.txt na citanie
        for riadok in subor:                     # pre kazdy riadok suboru
            tab.append(riadok.split())           # pridaj riadok ako prvok do tabulky tab[]
    print('tab - ', tab)

    # zacinam kreslit kruhy
    a = 50                                       # velikost kruhu
    y = 0                                        # startovacia suradnica y
    for i in range(len(tab)):
        x = 0                                    # suradnica pre x
        for j in range(len(tab[i])):
            w.create_oval(x,y,x+a,y+a, outline=tab[i][j])
            print('x1,y1 x2,y2 - {},{} {}{}  ' .format(x,y, x+10,y+10))
            x += a
        y += a
        print('Dalsi riadok --------------')


    mainloop()

# --------------------------------------------------------

subor = '/home/echolom/PycharmProjects/untitled1/FILE/cviv_13_16_farby_kruhov.txt'
kruhy(subor)


# 17. Predchádzajúci príklad upravte tak, aby ak by bol v súbore namiesto nejakej farby None, bude to označovať,
#     že sa príslušný kruh vynechá (ostane po ňom prázdne miesto).
#
#        napr. súbor môže vyzerať aj takto:
#
#             yellow yellow blus yellow yellow
#             yellow blue None blue yellow
#             blue None red None blue
#             yellow blue None blue yellow
#             yellow yellow blue yellow yellow
#
#         volanie:
#         >>> kruhy('farby.txt')
#         vykreslí 21 kruhov v piatich radoch po 5, 4, 3, 4, 5 kruhoch


from tkinter import *

def kruhy(meno_suboru):
    master = Tk()
    w = Canvas(master, width=400, height=400, bg = 'black')
    w.pack()

    # naplnenie tabulky tab[] prvkami zo suboru tabulka_farieb.txt
    tab = []
    with open(meno_suboru, 'r') as subor:        # otvor subor tabulka_farieb.txt na citanie
        for riadok in subor:                     # pre kazdy riadok suboru
            tab.append(riadok.split())           # pridaj riadok ako prvok do tabulky tab[]
    print('tab - ', tab)

    # zacinam kreslit kruhy
    a = 50                                       # velikost kruhu
    y = 0                                        # startovacia suradnica y
    for i in range(len(tab)):
        x = 0                                    # suradnica pre x
        for j in range(len(tab[i])):
            farba = tab[i][j]                    # prirad hodnotu prvku z tab do farba
            if farba != 'None':                  # ak hodnota prvka tabulky tab sa nerovna 'None'
                w.create_oval(x,y,x+a,y+a, outline=farba)
            else:
                print('Farba je None - prazdny kruh')
            print('x1,y1 x2,y2 - {},{} {}{}  ' .format(x,y, x+10,y+10))
            x += a
        y += a
        print('Dalsi riadok --------------')


    mainloop()

# --------------------------------------------------------

subor = '/home/echolom/PycharmProjects/untitled1/FILE/cviv_13_17_farby_kruhov.txt'
kruhy(subor)

# 18. Textový súbor v prvom riadku obsahuje dve čísla: počet riadkov a stĺpcov dvojrozmernej tabuľky.
#     V každom ďalšom sa nachádza trojica čísel: číslo riadka, číslo stĺpca, hodnota. Funkcia precitaj(meno_suboru)
#     z tohto súboru vytvorí dvojrozmernú tabuľku čísel, v ktorej budú na zadaných pozíciách dané hodnoty.
#
#         napr pre subor
#             4 5
#             3 1 7
#             0 1 1
#             3 3 3
#             2 4 9
#
#         >>> tab = precitaj('subor.txt')
#         >>> tab
#         [[0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 9], [0, 7, 0, 3, 0]]

def precitaj(meno_suboru):

    # naplnenie tabulky tab[] prvkami zo suboru tabulka_farieb.txt
    tab = []
    with open(meno_suboru, 'r') as subor:   # otvor subor tabulka_farieb.txt na citanie
        r = 0
        for riadok in subor:                # pre kazdy riadok suboru
            tab.append(riadok.split())      # pridaj riadok ako prvok do tabulky tab[]
            tab[r] = [int(i) for i in tab[r]]  # premen prvky riadku v tab[] na integer
            r += 1

    print('tab - ', tab)

    # zisti pocet riadkov a stlpcov novej tabulky
    pocet_riadkov = 0
    pocet_stlpcov = 0
    for i in tab:
        if pocet_riadkov < i[0]:
            pocet_riadkov = i[0]
        if pocet_stlpcov < i[1]:
            pocet_stlpcov = i[1]

    print('Pocet riadkov = ', pocet_riadkov)
    print('Pocet stlpcov = ', pocet_stlpcov)

    # inicializuj novu tabulku
    vysl_tab = []
    for i in range(pocet_riadkov):
        vysl_tab.append([0]*pocet_stlpcov)

    # print('vysl_tab = ', vysl_tab)

    # naplnam vysl_tab
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if j == 2:
                vysl_tab[tab[i][0]][tab[i][1]] = tab[i][j]
    # print('Vysledna tabulka - ', vysl_tab)
    return vysl_tab

t = precitaj('/home/echolom/PycharmProjects/untitled1/FILE/cviv_13_18.txt')
print('================================\nVysledna tabulka - ', t)