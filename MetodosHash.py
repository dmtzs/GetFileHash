import os, time, hashlib

class archYrutas():
    def NomCarpe(self, lstFiles, path, lstFiles2):
        lstDir= os.walk(path)

        for root, dirs, files in lstDir:
            for carpe in dirs:
                (nombreCarpe, extension)= os.path.splitext(carpe)
                if carpe!="Ignore":
                    lstFiles2.append(nombreCarpe)
                    try:
                        lstFiles.append(nombreCarpe.rstrip(" - OK"))
                    except:
                        pass

    def NomArch(self, path, exten):
        lstFiles= []
        lstDir= os.walk(path)

        for root, dirs, files in lstDir:
            for fichero in files:
                (nombreFichero, extension)= os.path.splitext(fichero)
                if exten== "All":
                    lstFiles.append(nombreFichero+extension)
                elif exten!="All":
                    if (extension== exten):
                        lstFiles.append(nombreFichero+extension)
            break
        return lstFiles

    def getsha256file(self, archivo):
        bande= 0
        try:
            hashsha= hashlib.sha256()
            with open(archivo, "rb") as f:
                for bloque in iter(lambda: f.read(4096), b""):
                    hashsha.update(bloque)
            return hashsha.hexdigest(), bande
        except Exception as e:
            bande= 1
            print(f"ERROR de función: {e}")
            return "", bande