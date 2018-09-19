# =============================================
# CVICENIA
# =============================================
# 3. Zadefinujte triedu UcetHeslo, ktorá je odvodená z triedy Ucet a má takto zmenené správanie:
#
#   -  __init__(meno, heslo, suma) - k účtu si zapamätá aj heslo
#   -  vklad(suma) - si najprv vypýta heslo a až keď je správne, zrealizuje vklad
#   -  vyber(suma) - si najprv vypýta heslo a až keď je správne, zrealizuje výber,
#      inak vráti None
#   -  pri definovaní týchto metód volajte ich pôvodné verzie z triedy Ucet
#   -  otestujte napr.


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
        self.vyberam = 0
        if self.suma > 0:
            if self.suma < suma:
                self.vyberam = self.suma
                self.suma = 0
            elif suma < 0:
                self.vyberam = 0
            else:
                self.vyberam = suma
                self.suma = self.suma - suma
        else:
            print('Na ucte je zostatok ... ', self.suma, ', Vyber nie je mozny!')
            self.vyberam = 0

        return self.vyberam



class UcetHeslo(Ucet):
    def __init__(self, meno, heslo, suma=0):
        super().__init__(meno, suma)
        self.heslo = heslo

    def stav(self):
        self.ucet_pass = input('Zadaj heslo k uctu: ')

        if self.ucet_pass != self.heslo:
            print('Nespravne meno heslo!')
            return None
        else:
            return Ucet.stav(self)

    def vklad(self, suma):
        self.ucet_pass = input('Pre vklad zadaj heslo k uctu: ')
        if self.ucet_pass != self.heslo:
            print('Nespravne meno heslo!')
            return None
        else:
            Ucet.vklad(self,suma)

    def vyber(self, suma):
        self.ucet_pass = input('Pre vyber zadaj heslo k uctu: ')
        if self.ucet_pass != self.heslo:
            print('Nespravne meno heslo!')
            return None
        else:
            return Ucet.vyber(self,suma)

# ------------------------------------------------------------

mbank = UcetHeslo('mbank', 'gigi')
csob = Ucet('csob', 100)
tatra = UcetHeslo('tatra', 'gogo', 17)
sporo = Ucet('sporo', 50)

#print(dir(mbank))
print(mbank.stav())
mbank.vklad(20)
print(mbank.stav())
mbank.vyber(20)
print(mbank.stav())