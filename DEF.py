

def vypis(tab):
    """
    Funkcia vypise dvojrozmernu tabulku
    :param tab: dvojrozmerna tabulka
    :return: vypise prvky dvojrozmernej tabulky oddelene ' '
    """
    print(' /========  DEF \ vypis(tab) - START ========\\')
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            print(tab[i][j], end=' ')
        print()
    print(' /========  DEF \ vypis(tab) ========\\')


def zisti(tab1, tab2):
    """
    Funkcia zisti ci su rovnako dlhe/velke tabulky
    :param tab1:
    :param tab2:
    :return: True - ak sa velikosti zhoduju, False - ak sa velikosti nezhoduju
    """
    if len(tab1) != len(tab2):
        return False
    else:
        for i in range(len(tab1)):
            if len(tab1[i]) != len(tab2[i]):
                return False
        return True