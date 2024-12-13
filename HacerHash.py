"""
    Este programa Genera una codigo hash de un archivo con Sha-1

    Programador: Martinez Alfaro Felipe de Jesus.
    Clase: Cryptography.
    Profesor: CORTEZ DUARTE NIDIA ASUNCION.
    fecha: 31/05/2023.
"""

'''__Imports__'''
import hashlib as Hash;

'''___Funciones___'''
def readFile(direccion,modo = "r"):
    fuente = open(direccion,modo); # abre archivo en modo lectura
    content = fuente.read();      # extrae todo el contenido
    fuente.close()
    return content;
#funcion para guardar localmente el contenido de una string en un archivo
def writeFile(direccion,contenido,modo = "w"):
    with open(direccion, modo) as file:
        file.write(contenido)
        file.close();

def write(direccion, texto_plano, hashi):
    writeFile(direccion ,texto_plano + "<hash>"+hashi+"<hash>");

def Hashear(string):
    return Hash.sha1(string.encode())
