import os, time

class Menus():
    def MenuPrin(self, bandera):
        os.system("cls")

        if bandera==0:
            print("\n\n\n\n\n\t\t\tÉxito al generar el archivo word con los hash!!")

        elif bandera==1:
            print("\n\n\n\n\n\t\t\tSaliendo del programa, recuerda llenar los requisitos previos")
            print("\t\t\tComo el archivo excel para que obtenga todas las rutas necesarias y los datos necesarios.")

        elif bandera==2:
            print("\n\n\n\n\n\t\t\tPor favor, ingresa una de las opciones que se te pide ingresar")
            print("\t\t\tRegresando a la vista anterior")

        time.sleep(4)

    def SeguroContinuar(self):
        salir= False
        while not salir:
            os.system("cls")
            print("\n\n\n\n\t\t\tEstas a punto de ejecutar el script para obtener el hash de una ruta en específico.")
            print("\t\t\tPor favor, verifica que los requisitos previos ya estén hechos, como el excel de donde tomará las cosas-")
            print("\t\t\tComo los archivos en la ruta. Ingresa debajo el número de la opción que deseas: ")
            try:
                retorno= int(input("\t\t\tDeseas continuar? 1. Si, 2. No/Salir: "))
                salir= True
            except:
                os.system("cls")
                print("\n\n\n\n\t\t\tPor favor, debes ingresar un número entero que sea de las opciones mostradas.")
                print("\t\t\tVolviendo al menú anterior.")
                time.sleep(4)
        return retorno
    
    def RutaEx(self):
        salir= False
        while not salir:
            os.system("cls")
            print("\n\n\n\n\tPor favor, ingresa la ruta de donde sacaremos el archivo excel con los demás datos.")
            print("\tUn ejemplo de una ruta sería : C:\\NmCarpe\\NomArchivo.xlsx")
            print("\tAsegurate de que sea un excel, si necesitas ayuda con la ruta de tu archivo llama a help desk para saber.")
            try:
                rutita= str(input("\t\t\tIngresa la ruta del archivo excel (.xlsx): "))#HACER LA FUNCIÓN EN LA QUE SE PUEDA REGRESAR DESDE AQUÍ AL MENÚ PRINCIPAL.
                salir= True
            except:
                os.system("cls")
                print("\n\n\n\n\n\tSi ves esto es por que te faltó poner el nombre del archivo al final de la cadena")
                print("\tPor favor, ingresa el nombre del archivo con la extensión (.xlsx)")
                print("\tRegresando al menú anterior...")
        return rutita