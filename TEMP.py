# =============================================
# CVICENIA
# =============================================
# 7. Z triedy Turtle zo (6) úlohy odvoďte triedu Turtle1, do ktorej dopíšete metódu strom(n, d) (z prednášky)
#
#      - potom otestujte, napr.
#
#         t = Turtle1()
#         t.lt(90)
#         t.strom(5, 60)
#
#   vyskúšajte, či aj v tejto triede fungujú príklady z prednášky s kreslením domčeka rôznym typom čiar

from tkinter import *
from math import sin, cos, pi

class Pero:
#    print('Inicializujem Pero')
    canvas = None
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
        self.polygon = (self.x, self.y)
        self.pise = True

    def pu(self):
#        print('Pero je hore pu()')
        self.pise = False

    def pd(self):
#        print('Pero je dole pd()')
        self.pise = True

    def setpos(self,x,y):
        #print('setpos({},{})' .format(x,y))
        if self.pise:
            canvas.create_line(self.x, self.y, x, y, width=1)
            self.x, self.y = x, y
            self.polygon += (self.x, self.y)
        else: self.x, self.y = x, y

class Turtle(Pero):
    def __init__(self,x=200, y=200, uhol=0):
        super().__init__(x,y)
        self.uhol = uhol
    def lt(self, uhol):
        self.uhol -= uhol

    def rt(self, uhol):
        self.uhol += uhol

    def fd(self, dlzka):
        x, y = 0, 0
        x = round(self.x + dlzka*cos((self.uhol*pi)/ 180), 10)
        y = round(self.y + dlzka*sin((self.uhol*pi)/ 180), 10)
        Pero.setpos(self, x, y)

    def bk(self, dlzka):
        x, y = 0, 0
        x = round(self.x - dlzka * cos((self.uhol * pi) / 180), 10)
        y = round(self.y - dlzka * sin((self.uhol * pi) / 180), 10)
        Pero.setpos(self, x, y)


class Turtle1(Turtle):

    def strom(self,n,d):
        self.fd(d)
        if n > 0:
            self.lt(40)
            self.strom(n - 1, d * 0.6)
            self.rt(90)
            self.strom(n - 1, d * 0.7)
            self.lt(50)
        self.bk(d)


    def domcek(self,dlzka):
        for uhol in 90, 90, 90, 30, 120, -60:
            self.fd(dlzka)
            self.rt(uhol)


# ---------------------------------------------------- >
root = Tk()
root.configure(bg = 'white')
root.title('16.3.5 ')
canvas = Canvas(root, bg = 'white', width = 400, height = 400)
c = Pero.canvas = canvas
c.pack()

p1 = Turtle1(100, 200)
p2 = Turtle1()

# print('Inicializacia p1: x={}, y={}, uhol={}' .format(p1.x, p1.y, p1.uhol))

print('Test:\n============================')

p1.domcek(50)
print('Polygon p1: ',p1.polygon)
print('Polygon p2: ',p2.polygon)

p2.lt(90)
p2.strom(5, 60)

c.mainloop()
