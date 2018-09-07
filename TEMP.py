
# DEDENIE Z NDRADENEJ TRIEDY UTVAR

from tkinter import *
import random

class Utvar:
    canvas = None

    def __init__(self, x, y, farba='red' ):
        self.x, self.y = x, y
        self.farba = farba
        self.id = None

    def posun(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
        self.canvas.move(self.id, dx, dy)

    def prefarbi(self, farba):
        self.farba = farba
        self.canvas.itemconfig(self.id, fill=self.farba)

class Kruh(Utvar):
    canvas = None

    def __init__(self, x, y, r, farba='red'):
        super().__init__(x, y, farba)
        self.r = r
        self.id = canvas.create_oval(self.x+self.r, self.y+self.r,
                                     self.x-self.r, self.y-self.r,
                                     fill = self.farba)
    def __str__(self):
        return 'Kruh({},{},{},{},{})' .format(self.x+self.r, self.y+self.r,
                                              self.x-self.r, self.y-self.r,
                                              repr(self.farba))

    def zmen(self, r):
        self.r = r
        self.canvas.coords(self.id,
                           self.x + self.r, self.y + self.r,
                           self.x - self.r, self.y - self.r)

class Obdlznik(Utvar):
    canvas = None

    def __init__(self, x, y, sirka, vyska, farba='red'):
        super().__init__(x, y, farba)
        self.sirka, self.vyska = sirka, vyska
        self.id = canvas.create_rectangle(self.x, self.y,
                                          self.x+sirka, self.y+vyska,
                                          fill=self.farba)

    def __str__(self):
        return 'Obdlznik({},{},{},{},{})' .format(self.x, self.y, self.sirka, self.vyska, self.farba)


    def zmen(self, sirka, vyska):
        self.r = r
        self.canvas.coords(self.id,
                           self.x, self.y,
                           self.x+sirka, self.y+vyska)

class Skupina:
    def __init__(self):
        self.pole = []

    def pridaj(self, utvar):
        self.pole.append(utvar)
        print('Pridal som do pola utvar - ', utvar.__str__())

    def prefarbi(self, farba):
        for utvar in self.pole:
            utvar.prefarbi(farba)

    def posun(self, dx, dy):
        for utvar in self.pole:
            utvar.posun(dx, dy)

    def prefarbi_typ(self, typ, farba):
        for utvar in self.pole:
            if isinstance(utvar, typ):
                utvar.prefarbi(farba)

    def posun_typ(self, typ, dx, dy):
        for utvar in self.pole:
            if isinstance(utvar, typ):
                utvar.posun(dx, dy)

    def citaj(self):
        skup_utvary = []
        for utvar in self.pole:
            skup_utvary.append(utvar.__str__())
        return skup_utvary

    # return 'Obsah skupiny: ({})' .format(', '.join(self.pole))


# ---------------------------------------------------- >
root = Tk()
root.configure(bg = 'white')
root.title('16.2.2 GRAFICKE OBJEKTY')
canvas = Canvas(root, bg = 'white', width = '600', height ='600')
c = Kruh.canvas = Obdlznik.canvas = canvas
c.pack()

skupina_utvarov = Skupina()
t1 = Kruh(50, 50, 30)
t2 = Obdlznik(100, 20, 100, 50)

# isinstance(i, t), ktorá zistí, či je inštancia i typu t alebo je typom niektorého jeho predka
print(isinstance(t1, Utvar))        # True
print(isinstance(t1, Kruh))         # True
print(isinstance(t1, Obdlznik))     # False
print(isinstance(t2, Obdlznik))     # True
# print(type(t1))     # <class '__main__.Kruh'>
# print(type(t2))     # <class '__main__.Obdlznik'>

t1.prefarbi('green')
t2.posun(50)

skupina_utvarov.pridaj(t1)
skupina_utvarov.pridaj(t2)
print('Obsah skupiny: [{}]' .format(', '.join(skupina_utvarov.citaj())))

skupina_utvarov.prefarbi_typ(Kruh, 'black')
skupina_utvarov.posun_typ(Obdlznik, -10, -25)






root.mainloop()


