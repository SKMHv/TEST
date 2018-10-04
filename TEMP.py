# =============================================
# CVICENIA
# =============================================

import pymysql
import datetime


class Pouzivatel:
    """
    Trieda Pouzivatel obsahuje nasledovne funkcie: ...
    """
    def __init__(self, meno, priezvisko, datumzalozenia, email, heslo):
        self.meno, self.priezvisko, self.datumzalozenia, self.email, self.heslo = meno, priezvisko, datumzalozenia, email, heslo

        # vyhladaj / skontroluj ci pouzivatel existuje
        # ak existuje tak vrat existujuceho
        # ak neexistuje tak zaloz noveho
        # SQLdb.zapis(self, sql)


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



# --------------------------------------------------------------
p1 = SQLdb('echolonDB')
p1.SQLconnect()
print(p1.hladaj('pouzivatelia','email','janko@hrasko.com'))
p1.SQLdisconnect()