import time, os, hashDoc, clase_pas, Pantallas

SacHash= hashDoc.SacarHash()
Vistas= Pantallas.Menus()

op= 0
salir= False

try:
    while not salir:
    #Menú en caso de que se necesitase, archivo Pantallas
    #Ingresar también la validación del número entero, archivo Pantallas, este no va pero es bueno que lo tenga en caso hayan-
    #menús más grandes

        op= Vistas.SeguroContinuar()

        if op==1:
            RutaEx= Vistas.RutaEx()
            SacHash.hash(RutaEx)
            Vistas.MenuPrin(0)
            salir= True

        elif op==2:
            Vistas.MenuPrin(1)
            salir= True
        
        else:
            Vistas.MenuPrin(2)

except Exception as e:
    os.system("cls")
    print(f"Ocurrió el ERROR: {e}")
    
finally:
    print("\n\t\t\tFinalizando la ejecución del programa...")
    time.sleep(4)
    os.system("cls")