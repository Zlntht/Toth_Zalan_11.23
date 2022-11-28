from functions import *
from os import system

fajlBeolvasas()
valasztas=''
while valasztas!='0':
    valasztas=menu()
    if valasztas=='1':
        loadObjektivek()
    elif valasztas=='2':
        keresesAr()
    elif valasztas=='3':
        pass
    elif valasztas=='4':
        objektivEladas()