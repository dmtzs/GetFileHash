import time, shutil, os, clase_pas

class Fecha():
    def calendario(self, arre):
        bisiesto= 0
        fecha_actual= ""
        fecha_actual= time.strftime("%m%d%y")
        fp= open("idda.txt", "r")
        fecha_anterior= fp.read()
        fp.close()
        arre[0]= fecha_anterior
        arre[1]= fecha_actual

        anio= time.strftime("%Y")
        mes= time.strftime("%m")
        dia= time.strftime("%d")

        parse_anio= int(anio)
        parse_mes= int(mes)
        parse_dia= int(dia)

        parse_dia+=1

        if parse_anio%4==0 and parse_anio%100!=0 or parse_anio%400==0:
            bisiesto= 1
        else:
            bisiesto= 0

        if (parse_mes==4 or parse_mes==6 or parse_mes==9 or parse_mes==11) and (parse_dia>30):
            aux= parse_dia-30
            parse_dia= 1+aux
            parse_mes+=1
            if parse_mes>12:
                parse_mes= 1
                parse_anio+=1

        elif (parse_mes==1 or parse_mes==3 or parse_mes==5 or parse_mes==7 or parse_mes==8 or parse_mes==10 or parse_mes==12) and (parse_dia>31):
            aux= parse_dia-31
            parse_dia= 1+aux
            parse_mes+=1
            if parse_mes>12:
                parse_mes= 1
                parse_anio+=1

        elif parse_mes==2 and bisiesto== 0 and parse_dia>28:
            aux= parse_dia-28
            parse_dia= 1+aux
            parse_mes+=1

        elif parse_mes==2 and bisiesto== 1 and parse_dia>29:
            aux= parse_dia-29
            parse_dia= 1+aux
            parse_mes+=1
        else:
            pass

        cade_anio= str(parse_anio)
        cade_anio= cade_anio[2:4]
        cade_dia= str(parse_dia)
        cade_mes= str(parse_mes)

        if parse_dia>=1 and parse_dia<=9:
            cade_dia= "0"+cade_dia
        else:
            pass

        cade_fecha_nueva= cade_mes+"/"+cade_dia+"/"+cade_anio

        fp= open("idda.txt", "wt")
        fp.write(cade_fecha_nueva)
        fp.close()

    def comprobar_carpeta_mesDia(self, bandemes):
        dia= time.strftime("%d")
        mes= time.strftime("%m")
        anio= time.strftime("%Y")

        VarSPTyLOR= anio+mes+dia
        parsemes= int(mes)

        if parsemes==1:
            mes= "Enero"
        elif parsemes==2:
            mes= "Febrero"
        elif parsemes==3:
            mes= "Marzo"
        elif parsemes==4:
            mes= "Abril"
        elif parsemes==5:
            mes= "Mayo"
        elif parsemes==6:
            mes= "Junio"
        elif parsemes==7:
            mes= "Julio"
        elif parsemes==8:
            mes= "Agosto"
        elif parsemes==9:
            mes= "Septiembre"
        elif parsemes==10:
            mes= "Octubre"
        elif parsemes==11:
            mes= "Noviembre"
        elif parsemes==12:
            mes= "Diciembre"
        else:
            pass

        carpeta= (dia+" "+mes)
        if bandemes==2:
            mes= mes+"\\"
            return mes
        elif bandemes==1:
            anio= anio+"\\"
            return anio
        elif bandemes==3:
            return carpeta
        elif bandemes==5:
            return VarSPTyLOR
        else:
            pass

class archYrutas():
    def NomArch(self, lstFiles, path, exten):
        lstDir= os.walk(path)


        for root, dirs, files in lstDir:
            for fichero in files:
                (nombreFichero, extension)= os.path.splitext(fichero)
                if (extension== exten):
                    lstFiles.append(nombreFichero+exten)

    def renom(self, lstFiles, path, scan):
        os.rename(path+lstFiles[0], path+scan)
    
    def mover(self, path, scan, path2):
        shutil.move(path+scan, path2+scan)

    def mover_multiples_archs(self, path, scan, path2):
        for i in scan:
            shutil.move(path+i, path2+i)

    def verificadir(self, path2):
        if os.path.isdir(path2):
            pass
        else:
            os.mkdir(path2)

    def agre_elim(self, acc, lineas):
        bande= 0
        print(acc)

        try:
            if acc[1] is True and acc[2] is False:
                lineas.append(acc[0]+"\n")
            elif acc[1] is False and acc[2] is True:
                pos= int(acc[0])
                pos-=1
                lineas.pop(pos)
            
            fp= open("carpetas_vacias_apps.txt", "wt")
            for i in lineas:
                fp.write(i)
            fp.close()
            bande= 1
        except ValueError:
            bande= 0
        return bande

    def agre_elim_no_gra(self, rad, carpe, lin):
        exito= 0
        aux= 0

        try:
            if rad==1:
                lin.append(carpe+"\n")
                exito= 1
            elif rad==2:
                carpe+="\n"
                for m in lin:
                    if m==carpe:
                        lin.pop(aux)
                        exito= 1
                        break
                    else:
                        aux+=1
            else:
                pass

            fp= open("carpetas_vacias_apps.txt", "wt")
            for p in lin:
                fp.write(p)
            fp.close()
        except ValueError:
            exito= 0
            os.system("cls")
            print("\n\n\n\t\t\tOcurrió algún error inesperado en la función: agre_elim_no_gra.")
            time.sleep(4)
        return exito