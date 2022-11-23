from data import nev, gyujtotavolsag, ar
from os import system

filename='objektivek.csv'

def menu():
    system('cls')
    print('--------------------MENÜ----------------------')
    print('0 - Kilépés')
    print('1 - Összes objektív a raktárban')
    print('2 - Objektív keresése ár alapján')
    print('3 - Objektív keresése gyújtótávolság alapján')
    print('4 - Objektív eladása')
    return input('Kérem válasszon: ')

def fajlBeolvasas():
    file=open('objektivek.csv','r', encoding='utf-8')
    file.readline() 
    for egysor in file:
        darabolt=egysor.strip().split(';')
        nev.append(darabolt[0])
        gyujtotavolsag.append(float(darabolt[1]))
        ar.append(float(darabolt[2]))
    file.close()

def loadObjektivek():
    system('cls')
    print('-------------OBJEKTIVEK RAKTÁRON--------------\n') 
    for i in range(0,len(nev)):
        print(f'\t{nev[i]} {gyujtotavolsag[i]}mm \n\t\tÁr: {ar[i]} Ft\n ')
    input('\nTovább...')
