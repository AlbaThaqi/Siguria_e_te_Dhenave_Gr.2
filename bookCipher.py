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

        
