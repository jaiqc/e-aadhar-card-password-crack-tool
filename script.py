#! /usr/bin/env python3
import exrex
import subprocess
import sys
import os
import time
import platform
from pathlib import Path

#Linux:
#  To work in most of linux, i used APT Manager : "sudo apt-get install pdfcrack"
#  If your system not use APT Packate Manager Then Install "pdfcrack" from your packate manager
#Windows:
#  Windows User only have to install required library in Root Shell

def process_e_aadhar_card_crack(filename):

    if platform.system() == "Linux":  #Crack In Linux
        
        try:
            tic = time.time()
            subprocess.call(["pdfcrack",filename,"--wordlist="+ os.path.join(os.getcwd(),"wordlist")])
        except Exception:
            subprocess.call(["sudo","apt-get","install","pdfcrack","-y"])
            tic = time.time()
            subprocess.call(["pdfcrack",filename,"--wordlist="+ os.path.join(os.getcwd(),"wordlist")])
        # output = subprocess.call(["pdfcrack",filename,"--wordlist="+ os.path.join(os.getcwd(),"wordlist")])
    if platform.system() == "Windows": #Crack On Windows
        subprocess.call(["windows/pdfcrack.exe",filename,"--wordlist="+ os.path.join(os.getcwd(),"wordlist")])
    toc = time.time()
    print("Time Taken: " , str(toc - tic))

def generate_e_aadhar_card_word_list():
    #  Wordlist Logic:
    #  Month Pattern : (0[0-9])|(1[0-2])
    #  Day Pattern   : (0[1-9])|(1[0-9])|(2[0-9])|(3[0-2])
    #  Year Pattern  : (19[3-9][0-9])|(20[012][0-9])
    #  NAME          : ([A-Z])([A-Z])([A-Z])([A-Z])
    #  Final Pattern : (([A-Z])([A-Z])([A-Z])([A-Z])2[0-0])([0-2])([0-9])
    #                  ----------------------------- --------------------
    # (Only 2000 to 2999)        NAME                         Year

    if not Path("wordlist").is_file():
        print("Generating world list file...")
        with open("wordlist", "w") as words:  # Generate WordList
            # Change Here To Get Diffrent Wordlist
            data = list(exrex.generate(
                r'(([A-Z])([A-Z])([A-Z])([A-Z])2[0-0])([0-2])([0-9])'))
            for listitem in data:
                words.write('%s\n' % listitem)

    else:
        print("World list file is already exist")


def main():
    try:
        filename = sys.argv[1]  # FileName
    except Exception:
        print("<#>You Missed File Name\nSyntax:\n       Python3 script.py <E_Adhar_card_filenmae.pdf>")
        exit()
    
    generate_e_aadhar_card_word_list()
    process_e_aadhar_card_crack(filename=filename)

if __name__ == "__main__":
    main()
