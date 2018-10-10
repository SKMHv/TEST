# =============================================
# CVICENIA
# =============================================

import pymysql
import datetime


class Pouzivatel:
    """
    Trieda Pouzivatel obsahuje nasledovne funkcie: ...
    """
    def __init__(self, meno, priezvisko, email, heslo):
        self.meno, self.priezvisko, self.email, self.heslo = meno, priezvisko, email, heslo


    # def vytvor_pouzivatela(self):
    #     Pouzivatel.vyhladaj_pouzivatela(self.email)

        # vyhladaj / skontroluj ci pouzivatel existuje
        # ak existuje tak vrat existujuceho
        # ak neexistuje tak zaloz noveho
        # SQLdb.zapis(self, sql)

    def vyhladaj_pouzivatela(self,email):
        SQLdb.hladaj('pouzivatelia','email',email)





#    def deaktivuj_pouzivatela(self,email):

# ----------------------- SQL -----------------------

class SQLdb:
    """
    Trieda obsahuj nasledovne funkcie: SQLconnect, SQLdisconnect, historia, hladaj, zapis
    """
    def __init__(self,db):
        self.db = db
        self.conn = None

    def SQLconnect(self):
        """
        Pripoji sa k danej databaze self.db
        :return:
        """
        self.conn = pymysql.connect(host='127.0.0.1',
                               user='root',
                               password='Pipo246.',
                               db = self.db,
                               charset='utf8mb4',
                               autocommit=True,
                               cursorclass=pymysql.cursors.DictCursor)

    def SQLdisconnect(self):
        self.conn.close()


    def historia(self, pouzivatelia_id, operacia):
        """
        Zapise operaciu oo historie
        :return:
        """
        sql = "INSERT INTO historia (pouzivatelia_id, operacia, cas) values ('{}', '{}', NOW())" .format(pouzivatelia_id, operacia)
        SQLdb.zapis(self, sql)

    def hladaj(self, table, co, hodnota):
        """
        Vyhlada pouzivatela podla email.
        :param email: email pouzivatela
        :return: pouzivatel s atributmi
        """
        operacia = 'hladaj'
        sql = ("SELECT id, meno, priezvisko, datumzalozenia, email, heslo FROM `{}` WHERE `{}` = '{}' " .format(table, co, hodnota))
        print(sql)
        try:
            with self.conn:
                cursor = self.conn.cursor()
                cursor.execute(sql)
                #id, meno = cursor.fetchone()
                vysledok = cursor.fetchone()
                #print(vysledok)
                # for columm in  vysledok:
                #     print(columm)
                #print(id, meno)
                print('Vraciam vysledok z hladania')
                return vysledok

        finally:
            teraz = datetime.datetime.now()
            print(teraz)
            SQLdb.historia(self, 1, operacia)
            print('vykonal som zapis do historie a pokracujem')

    def zapis(self,sql):
        """
        Funkcia zapise hodnoty do tabulky podla sql parametra
        :param sql:
        :return:
        """
        print(sql)
        try:
            with self.conn:
                cursor = self.conn.cursor()
                cursor.execute(sql)
                print('Pred commit historia')
                self.conn.commit()
        finally:
            print('Po commit historia')
# ---------------------------------------------------------------
# ========================== TESTUJ =============================
db = SQLdb('echolonDB')
db.SQLconnect()
p1 = Pouzivatel('Jozko', 'Pucik', 'jozko.pucik@gmail.com', '111111')
p1.vyhladaj_pouzivatela('jozko.pucik@gmail.com')
#print(db.hladaj('pouzivatelia','email','janko@hrasko.com'))
db.SQLdisconnect()
