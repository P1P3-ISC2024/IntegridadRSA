from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from file_manager import *
import HacerHash as HH
from Crypto.Hash import SHA1
import binascii
from tkinter import messagebox


def encrypt_message(path_file="message.txt",path_key='publicKey_A.pem'):
    # Leer archivo
    content = HH.readFile(direccion=path_file)
    #print("hash: "+HH.Hashear( content ).hexdigest())
    #msg = bytes( HH.Hashear( content ).hexdigest() , encoding='utf-8')
    #msg = HH.Hashear( content ).hexdigest().encode('UTF-8')
    
    #   Abrir llave publica A
    f = open(path_key,'r')
    pubKey_B = RSA.importKey(f.read())
    #publicKey_B = pubKey_B.publickey()
    f.close()

    #   Cifrar usando llave publica A
    #encryptor = PKCS1_OAEP.new(publicKey_B)
    encryptor = pkcs1_15.new(pubKey_B)
    h = SHA1.new(content.encode())
    print(" <->"+content+"<->")
    print( "hash: ", h.hexdigest())
    encrypted = encryptor.sign( h )
    #   Escribit txt
    HH.write("message_C.txt", content, encrypted.hex() ) ;


def decrypt_message( content ,hash_RSA,path_key="privateKey_A.pem"):   
    #   Abrir llave privada A
    f = open(path_key,'r')
    privKey_A = RSA.importKey(f.read())
    
    #   Decifrar con privada A
    cipher = pkcs1_15.new(privKey_A)
    #message = cipher.decrypt(hash_RSA)
    h = SHA1.new(content)
    try:
        print( "hash: ", h.hexdigest() )
        cipher.verify(h, hash_RSA)
        messagebox.showinfo(title="Verification:",message=" :) YESS! is valid")
    except (ValueError , TypeError):
        print( ValueError)
        print( TypeError )
        messagebox.showinfo(title="Verification:",message=" NOO! >:c F*#k is fake")

    #   Retornar mensaje
    #return str(message.decode("utf-8"));


def main():
    encrypt_message()
    decrypt_message()

if __name__ == "__main__":
    main()
