from data import objektivek
from os import system

filename='objektivek.csv'

def menu():
    system('cls')
    print('-----------------MENÜ-------------------')
    print('0 - Kilépés')
    print('1 - Összes objektív a raktárban')
    print('2 - Objektív keresése ár alapján')
    print('3 - Objektív keresése gyújtótávolság alapján')
    print('4 - Objektív eladása')
    return input('Kérem válasszon: ')

def loadObjektivek():
    file=open(filename,'r',encoding='utf-8')

    file.close()