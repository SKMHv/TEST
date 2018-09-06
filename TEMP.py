
print("------------ 16.2.2 ------------")
print('===== GRAFICKE OBJEKTY =====')

from tkinter import *

class Kruh:
    canvas = None
    typ = 'kruh'

    def __init__(self, x, y, r, farba='red'):
        self.x, self.y, self.r = x, y, r
        self.farba = farba
        self.id = canvas.create_oval(self.x+self.r, self.y+self.r,
                                     self.x-self.r, self.y-self.r,
                                     fill = self.farba)
    def __str__(self):
        return 'Kruh({},{},{},{},{})' \
            .format(self.x+self.r, self.y+self.r,self.x-self.r, self.y-self.r,repr(self.farba))

    def posun(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
        self.canvas.move(self.id, dx, dy)

    def zmen(self, r):
        self.r = r
        self.canvas.coords(self.id,
                           self.x + self.r, self.y + self.r,
                           self.x - self.r, self.y - self.r)

    def prefarbi(self, farba):
        self.farba = farba
        self.canvas.itemconfig(self.id, fill=self.farba)


class Obdlznik:
    canvas = None
    typ = 'obdlznik'

    def __init__(self, x, y, sirka, vyska, farba='red'):
        self.x, self.y, self.sirka, self.vyska = x, y, sirka, vyska
        self.farba = farba
        self.id = canvas.create_rectangle(self.x, self.y,
                                          self.x+sirka, self.y+vyska,
                                          fill=self.farba)

    def __str__(self):
        return 'Obdlznik({},{},{},{},{})' .format(self.x, self.y, self.sirka, self.vyska, self.farba)


    def posun(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
        self.canvas.move(self.id, dx, dy)

    def zmen(self, sirka, vyska):
        self.r = r
        self.canvas.coords(self.id,
                           self.x, self.y,
                           self.x+sirka, self.y+vyska)

    def prefarbi(self, farba):
        self.farba = farba
        self.canvas.itemconfig(self.id, fill=self.farba)

class Skupina:
    def __init__(self):
        self.pole = []

    def pridaj(self, utvar):
        self.pole.append(utvar)
        print('Pridal som do pola')

    def prefarbi(self, farba):
        for utvar in self.pole:
            utvar.prefarbi(farba)

    def posun(self, dx, dy):
        for utvar in self.pole:
            utvar.posun(dx, dy)

    def prefarbi_typ(self, typ, farba):
        for utvar in self.pole:
            if utvar.typ == typ:
                utvar.prefarbi(farba)

    def posun_typ(self, typ, dx, dy):
        for utvar in self.pole:
            if utvar.typ == typ:
                utvar.posun(dx, dy)

    def citaj(self, skupina):
        return 'Obsah skupiny: ({})' .format(', '.join(self.pole))



# ---------------------------------------------------- >
root = Tk()
root.configure(bg = 'white')
root.title('16.2.2 GRAFICKE OBJEKTY')
canvas = Canvas(root, bg = 'white', width = '600', height ='600')
c = Kruh.canvas = Obdlznik.canvas = canvas
c.pack()

skupina_utvarov = Skupina()
k = Kruh(50, 50, 30, 'blue')
r = Obdlznik(100, 20, 100, 50)


skupina_utvarov.pridaj(k)
skupina_utvarov.pridaj(r)
print(skupina_utvarov.citaj())



k.prefarbi('green')
r.posun(50)





root.mainloop()