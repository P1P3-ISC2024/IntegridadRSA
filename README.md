# IntegridadRSA
Este programa está diseñado para comprobar la integridad y autenticidad de un txt, a traves de la firma digital de un archivo con RSA y la comparación de hash con Sha1

-Caracteristicas:
  1. Puede firmar y verificar la firma.
  2. Cuenta con interfaz gráfica.
  3. Selección de archivos a traves del explorador de archivos.

-Notas:
  1. Se requiere haber generado previamente las llaves públicas y privadas (archivos .pem).
  2. Para abrir el programa ejecute el archivo **main.py**.
  3. Si al firmar o verificar no se lanza una ventana emergente de que ha terminado puede que halla existido un error en el prcoeso, revise las instrucciones.

-Firmar un archivo:
  1.  Ejecuta el archivo **main.py**.
  2.  Selecciona la opción SIGN DOCUMENT.
  3.  Presiona el botón SELECT.
  4.  Presiona el botón KEY para buscar tu llave privada(.pem).
  5.  Presiona el botón FILE para buscar el archivo .txt a firmar.
  6.  Presiona el botón SIGN para firmar.
  7.  Espera a que se genere el archivo . message_C.txt

-Verificar un archivo:
  1.  Ejecuta el archivo **main.py**.
  2.  Selecciona la opción CHECK SIGNATURE.
  3.  Presiona el botón SELECT.
  4.  Presiona el botón KEY para buscar la llave pública del autor(.pem).
  5.  Presiona el botón FILE para buscar el archivo .txt a verificar.
  6.  Presiona el botón VERIFY para iniciar la verificadión.
  7.  Espera a la ventana emergente que indique la validez.
