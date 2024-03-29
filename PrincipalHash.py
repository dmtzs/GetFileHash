#@File: PrincipalHash.py
#@Author: Diego Martínez Sánchez
#@Brief: Main program which you need to run in order to execute the program in the right way.
try:
    import os
    import time
    import platform
    from biblios import *
except ImportError as eImp:
    print(f"The following error ocurred: {eImp}")

def comandoShell():
    sistema= platform.system()

    if sistema== "Windows":
        return "cls"
    else:
        return "clear"

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
        os.system(comandoShell())
        Vistas.Excepciones(Lang, e)
        
    finally:
        Vistas.Finalmente(Lang)
        time.sleep(4)
        os.system(comandoShell())

if __name__== "__main__":
    try:
        prin()
    except KeyboardInterrupt:
        print("Was pressed Ctrl + C")
    except Exception as ex:
        print(f"The following ERROR ocurred: {ex}")
    finally:
        print("Ending program")