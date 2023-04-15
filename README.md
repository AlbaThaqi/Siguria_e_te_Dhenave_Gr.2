# Book Cipher

## Përshkrimi i shkurtër i Book Cipher
Book Cipher është një teknikë kriptografike e cila përdor një libër ose një pjesë të tekstit si çelës për të enkriptuar apo dekriptuar një mesazh sekret. 
Në një book cipher, teksti i mesazhit konvertohet në një sekuencë numrash që u referohen fjalëve ose shkronjave specifike në libër. 
Këta numra më pas u transmetohen marrësit, i cili përdor të njëjtin libër për të kërkuar fjalët ose shkronjat përkatëse dhe për të fituar mesazhin origjinal.

## Ekzekutimi i programit të implementuar për Book Cipher

Ekzekutimi i programit bëhet përmes command line. 

Për enkriptim të mesazhit përdoret komanda si më poshtë:

`python bookCipher.py -m e -b book.txt -i message.txt -o output.txt`

, ndërsa për dekriptim të mesazhit përdoret komanda si më poshtë:

`python bookCipher.py -m d -b book.txt -i output.txt -o deciphered.txt`

, ku:

-m përcakton modin (encipher / decipher ose e / d);

-b përcakton librin që do të përdoret për enkriptim apo dekriptim;

-i përcakton fajllin e mesazhit që do të enkriptohet apo dekriptohet;

-o përcakton fajllin ku do të ruhet rezultati pas ekzekutimit.
