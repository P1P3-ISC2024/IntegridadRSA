"""
    Este programa verifica una codigo hash de un archivo con Sha-1

    Programador: Martinez Alfaro Felipe de Jesus.
    Clase: Cryptography.
    Profesor: CORTEZ DUARTE NIDIA ASUNCION.
    fecha: 31/05/2023.
"""

'''__Imports__'''
import hashlib as Hash;
import regex as rex;
from rsa_file import decrypt_message;
from tkinter import messagebox

'''___Funciones___'''
def readFile(direccion,modo = "r"):
    fuente = open(direccion,modo); # abre archivo en modo lectura
    content = fuente.read();      # extrae todo el contenido
    fuente.close()
    return content;

#funcion para guardar localmente el contenido de una string en un archivo
def writeFile(direccion,contenido,modo = "w"):
    with open(direccion,modo) as file:
        file.write(contenido)
        file.close();

def Hashear(string):
    return Hash.sha1(string.encode())

def comprobar(contenido,path_key):
    hashi = rex.findall(r"<hash>(\S+)<hash>",contenido)[0]
    texto = rex.sub("<hash>\S+<hash>","",contenido);
    print(" <->"+texto+"<->")
    decrypt_message(texto.encode(),bytes.fromhex(hashi),path_key)
    #print("hash: ",hashi);
    print("\ntexto:\n"+texto)
    """print("\nValido: ",end="")
    if(hashi != Hash.sha1(texto.encode()).hexdigest()):
        print("No >:v")
        messagebox.showinfo(title="Verification:",message=" NOO! >:c F*#k is fake")
        return False;
    else:
        print("Si :)");
        messagebox.showinfo(title="Verification:",message=" :) YESS! is valid")
        return True;"""
