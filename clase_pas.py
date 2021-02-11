from getpass import getpass
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
import os, time
 
class contra():
    def usuarioCambiar(self):
        os.system("cls")
        print("Este es el usuario anterior: "+self.usuario())
        user= input("Ingresa el nuevo usuario que se ocupara en todo el programa: ")
        fp= open("user.txt", "wt")
        fp.write(user)
        fp.close()

    def contrasenaCambiar(self):
        os.system("cls")
        archivo= 'encrypted.bin'
        data= getpass("Ingresa tu contraseña a encriptar: ").encode("utf8")
        key= getpass("Ingresa la llave para encriptar la contraseña, la llave sin espacios: ").encode("utf8")

        self.AESencry(archivo, data, key)
        #pas= self.AESdecry(archivo, key)

    def usuario(self):
        fp= open("user.txt", "rt")
        user= fp.read()
        fp.close()
        return user

    def contrasena(self):
        archivo= 'encrypted.bin'
        key= getpass("Ingresa la llave para desencriptar la contraseña por favor: ").encode("utf8")
        pas= self.AESdecry(archivo, key)
        os.system("cls")
        return pas

    def AESencry(self, arch, frase, llave):
        cipher= AES.new(llave, AES.MODE_CBC)
        frase_cifrada= cipher.encrypt(pad(frase, AES.block_size))

        file_out= open(arch, "wb")
        file_out.write(cipher.iv)
        file_out.write(frase_cifrada)
        file_out.close()

    def AESdecry(self, arch, llave):
        file_in= open(arch, "rb")
        iv= file_in.read(16)
        ciphered_data= file_in.read()
        file_in.close()

        cipher= AES.new(llave, AES.MODE_CBC, iv= iv)
        frase_original= unpad(cipher.decrypt(ciphered_data), AES.block_size)
        frase_original_text= str(frase_original)
        frase_original_text= frase_original_text.lstrip("b'")
        frase_original_text= frase_original_text.rstrip("'")
        return frase_original_text

    def opcion(self):
        correcto= False
        num= 0

        while not correcto:
            os.system("cls")
            print("\n\n\n\t\tEn esta opción se muestra la contraseña, asegurate que nadie te esté viendo para que tu contraseña-")
            print("\t\tno sea revelada ni sea vista por nadie. Deberás ingresar un número entero.")
            try:
                num= int(input("\t\t\tDeseas continuar?, 1. Si, 2. No: "))
                correcto= True
            except ValueError:
                os.system("cls")
                print("\n\n\n\t\t\tError, debes de introducir un número entero y que esté en el menú la opción.")
                time.sleep(3)
        return num