# =============================================
# CVICENIA
# =============================================
# Zadefinujte triedu Ucet s metódami:
#
#    - __init__(meno, suma) - meno účtu a počiatočná suma, napr. Ucet('mbank', 100) alebo Ucet('jbanka')
#
#    - __str__() - reťazec v tvare 'ucet mbank -> 100 euro' alebo ucet jbanka -> 0 euro
#
#    - stav() - vráti momentálny stav účtu
#
#    - vklad(suma) - danú sumu pripočíta k účtu
#
#    - vyber(suma) - vyberie sumu z účtu (len ak je to kladné číslo), vráti vybranú sumu, ak je na účte
#      menej ako požadovaná suma, vyberie len toľko koľko sa dá
#
#    - otestujte napr.

# mbank = Ucet('mbank')
# csob = Ucet('csob', 100)
# tatra = Ucet('tatra', 17)
# sporo = Ucet('sporo', 50)
# mbank.vklad(sporo.vyber(30) + tatra.vyber(30))
# csob.vyber(-5)
# spolu = 0
# for ucet in mbank, csob, tatra, sporo:
#     print(ucet)
#     spolu += ucet.stav()
# print('spolu = ', spolu)

# Vypise:
# ucet mbank -> 47 euro
# ucet csob -> 100 euro
# ucet tatra -> 0 euro
# ucet sporo -> 20 euro
# spolu =  167

class Ucet:
    def __init__(self, meno, suma = 0):
        self.meno = meno
        self.suma = suma

    def __str__(self):
        return 'Ucet {} -> {} euro'.format(self.meno, self.suma)

    def stav(self):
        return self.suma

    def vklad(self, suma):
        self.suma += suma

    def vyber(self, suma):
        self.vyber = 0
        if self.suma > 0:
            if self.suma < suma:
                self.vyber = self.suma
                self.suma = 0
            elif suma < 0: self.vyber = 0
            else:
                self.vyber = suma
                self.suma = self.suma - suma
        else:
            print('Na ucte je zostatok ... ', self.suma, ', Vyber nie je mozny!')
            self.vyber = 0

        return self.vyber

mbank = Ucet('mbank')
csob = Ucet('csob', 100)
tatra = Ucet('tatra', 17)
sporo = Ucet('sporo', 50)

print(mbank)                             # Ucet mbank -> 0 euro
print(sporo)                             # Ucet sporo -> 50 euro
print(tatra)                             # Ucet tatra -> 17 euro

mbank.vklad(sporo.vyber(30) + tatra.vyber(30))
print(mbank)                             # Ucet mbank -> 47 euro
print(sporo)                             # Ucet sporo -> 20 euro
print(tatra)                             # Ucet tatra -> 0 euro
csob.vyber(-5)
print(csob)

