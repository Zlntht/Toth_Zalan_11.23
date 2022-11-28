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
    return input('\nKérem válasszon: ')

def fajlBeolvasas():
    file=open('objektivek.csv','r', encoding='utf-8')
    file.readline() 
    for egysor in file:
        darabolt=egysor.strip().split(';')
        nev.append(darabolt[0])
        gyujtotavolsag.append(int(darabolt[1]))
        ar.append(int(darabolt[2]))
    file.close()

def loadObjektivek():
    system('cls')
    print('-------------OBJEKTIVEK RAKTÁRON--------------\n') 
    for i in range(0,len(nev)):
        print(f'\t{nev[i]} {gyujtotavolsag[i]}mm \n\t\tÁr: {ar[i]} Ft\n ')
    input('\nVissza a menübe...')

def objektivEladas():
    system('cls')
    print('---------------OBJEKTÍV ELADÁS----------------\n')
    ujNev=input('\tObjektív típusa: ')
    ujGyujtotavolsag=int(input('\tGyujtótávolság: ').replace('mm',''))
    ujAr=int(input('\tÁra: ').replace('Ft',''))
    nev.append(ujNev)
    gyujtotavolsag.append(ujGyujtotavolsag)
    ar.append(ujAr)
    objektivFelvetele(ujNev,ujGyujtotavolsag,ujAr)
    input('\nSikeresen felvettük a listába!\n\nVissza a menübe...')

def objektivFelvetele(nev,gyujtotavolsag,ar):
    file=open('objektivek.csv','a',encoding='utf-8')
    file.write(f'\n{nev};{gyujtotavolsag};{ar}')
    file.close()

def keresesAr():
    system('cls')
    print('---------OBJEKTÍV SZŰRÉS ÁR ALAPJÁN----------\n')
    alsohatar=int(input('\tKérem adja meg az alsó határt: '))
    felsohatar=int(input('\tKérem adja meg az felső határt: '))
    for i in ar:
        if alsohatar<=i and i<=felsohatar:
            print(f'\t{nev[i]} {gyujtotavolsag[i]}mm \n\t\tÁr: {ar[i]} Ft\n ')
    input('\nVissza a menübe...')

def keresesGyujtotavolsag():
    system('cls')
    print('----OBJEKTÍV SZŰRÉS GYUJTÓTÁVOLSÁG ALAPJÁN-----\n')
    érték=int(input('\tKérem adja meg az értéket: '))
    for i in ar:
        if érték==i:
            print(f'\t{nev[i]} {gyujtotavolsag[i]}mm \n\t\tÁr: {ar[i]} Ft\n ')
    input('\nVissza a menübe...')