# Book Cipher

## Përshkrim i shkurtër i Book Cipher
Book Cipher është një teknikë kriptografike e cila përdor një libër ose një pjesë të tekstit si çelës për të enkriptuar apo dekriptuar një mesazh sekret. 
Në një book cipher, teksti i mesazhit konvertohet në një sekuencë numrash që u referohen fjalëve ose shkronjave specifike në libër. 
Këta numra më pas u transmetohen marrësit, i cili përdor të njëjtin libër për të kërkuar fjalët ose shkronjat përkatëse dhe për të fituar mesazhin origjinal.

## Programi i implementuar për Book Cipher dhe ekzekutimi i tij

Programi për Book Cipher është implementuar në gjuhën programuese Python në kuadër të lëndës Siguria e të Dhënave.

Ekzekutimi i këtij programi bëhet përmes command line. 

Për enkriptim të mesazhit përdoret komanda si më poshtë:

`python bookCipher.py -m e -b book.txt -i message.txt -o output.txt`

, ndërsa për dekriptim të mesazhit përdoret komanda si më poshtë:

`python bookCipher.py -m d -b book.txt -i output.txt -o deciphered.txt`

, ku:

-m përcakton modin (encipher / decipher ose e / d);

-b përcakton librin që do të përdoret për enkriptim apo dekriptim;

-i përcakton fajllin e mesazhit që do të enkriptohet apo dekriptohet;

-o përcakton fajllin ku do të ruhet rezultati pas ekzekutimit.


## Libraritë e nevojshme

Për ta ekzekutuar programin duhet të keni të instaluar paraprakisht ndonjë nga environments siç janë PyCharm apo IDLE Python dhe libraritë e Python si më poshtë:

- argparse

- json

- random

Këto librari mund të instalohen përmes komandës 'pip'. Shembull:

`pip install argparse`

## Anëtarët e grupit

- Alba Thaqi

- Albatin Totaj

- Ajshe Selmani

- Bleron Mexhuani
