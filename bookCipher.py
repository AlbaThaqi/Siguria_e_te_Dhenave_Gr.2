import argparse
import json
import random

def encipher(sourcemessagefilename, bookfilename, outputfilename):

    print("Enciphering message : " + sourcemessagefilename)
    print("Using book          : " + bookfilename)
    print("Output to           : " + outputfilename)

    with open(sourcemessagefilename, "rt", encoding="utf-8") as sf, open(bookfilename, "rt", encoding="utf-8") as bkf:

        # marrja e madhesise se librit

        booktext = bkf.read()
        booksize = len(booktext)

        enciphered = []
        sourceText = sf.read()

        for sourcechar in sourceText:

            # per te evituar zgjedhjen e te njejtes pozite per secilin karakter cdo here, fillojme nga nje pozite random
            # kerkimi behet deri ne fund dhe pastaj nese ende nuk eshte gjetur behet kerkimi nga fillimi i fajllit deri te pozita fillestare e kerkimit

            startpos = random.randrange(booksize)

            charpos = booktext.index(sourcechar, startpos)
            if (charpos == -1):
                charpos = booktext.index(sourcechar, 0, startpos)

            if (charpos == -1):
                raise ValueError("Character : " + sourcechar +
                                 ", was not found in the book")

            enciphered.append(charpos)
            
    with open(outputfilename, "wt") as of:
        json.dump(enciphered, of)

    print("Enciphering completed.")
    return

def decipher(encipheredmessagefilename, bookfilename, decipheredmessagefilename):

 

    print("Deciphering message : " + encipheredmessagefilename)

    print("Using book            : " + bookfilename)

    print("Output to             : " + decipheredmessagefilename)

 

    decipheredmsg = []

 

    with open(encipheredmessagefilename, "rt") as ef, open(bookfilename, "rt", encoding="utf-8") as bkf:

        enciphered = json.load(ef)

        booktext = bkf.read()

        for encipheredpos in enciphered:

            decipheredmsg.append(booktext[encipheredpos])

 

    with open(decipheredmessagefilename, "wt", encoding='UTF-8') as uf:

        uf.write("".join(decipheredmsg))

 

    print("Deciphering completed.")

 

    return