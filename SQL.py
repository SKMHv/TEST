# ======================================
# 1. modul -> pymysql
# ======================================


import pymysql

class SQCConnector:
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1',
                               user='root',
                               password='Pipo246.',
                               db='echolonDB',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)

    def hladaj(self, email):
        sql = ("SELECT id, meno, priezvisko, datumzalozenia, email, heslo FROM `pouzivatelia` WHERE `email` = '%s' "  %email)
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
                return vysledok



        finally:
            self.conn.close()

#    def zapis(self, meno, priezvisko, datumzalozenia, email, heslo):



class Pouzivatel:
    def __init__(self, meno, priezvisko, datumzalozenia, email, heslo):
        self.meno, self.priezvisko, self.datumzalozenia, self.email, self.heslo = meno, priezvisko, datumzalozenia, email, heslo



    # def registruj(self):
    #     try:
    #         with self.conn.cursor() as cursor:
    #             # vytvor novy zapis do db
    #             sql = "INSERT INTO 'pouzivatelia' ('meno','priezvisko','datumzalozenia', 'email', 'heslo') VALUES (%s, %s, %s, %s, %s)"
    #             cursor.execute(sql,(self.meno, self.priezvisko, self.datumzalozenia, self.email, self.heslo))
    #             print(sql)
    #         self.conn.commit()
    #     finally:
    #         self.conn.close()




#p1 = Pouzivatel('Janko', 'Mrkvicka', '2016-12-21', 'dssd@gmail.com', '12364')
p1 = SQCConnector()
print(p1.hladaj('janko@hrasko.com'))

# ======================================
# 1. modul -> sqlite3
# ======================================

