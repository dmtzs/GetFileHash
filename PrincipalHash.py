#@File: PrincipalHash.py
#@Author: Diego Martínez Sánchez
#@Brief: Main program which you need to run in order to execute the program in the right way.

import time, os, hashDoc, clase_pas, Pantallas

def prin():
    SacHash= hashDoc.SacarHash()
    Vistas= Pantallas.Menus()

    op= 0
    salir= False

    try:
        Lang= Vistas.Language()
        while not salir:
            op= Vistas.SeguroContinuar(Lang)

            if op==1:
                RutaEx= Vistas.RutaEx(Lang)
                SacHash.hash(RutaEx)
                Vistas.MenuPrin(0, Lang)
                salir= True

            elif op==2:
                Vistas.MenuPrin(1, Lang)
                salir= True
            
            else:
                Vistas.MenuPrin(2, Lang)

    except Exception as e:
        os.system("cls")
        Vistas.Excepciones(Lang, e)
        
    finally:
        Vistas.Finalmente(Lang)
        time.sleep(4)
        os.system("cls")

if __name__== "__main__":
    prin()