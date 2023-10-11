# Transposition Cipher Encrypt/Decrypt File
# https://www.nostarch.com/crackingcodes (BSC Licensed)

import os
import sys
import time
import transpositionDecrypt, transpositionEncrypt


def main():
    inputDirectoryName = "Resources"
    inputFileName = "frankenstein"
    inputFileType = ".txt"
    fullInputFileName = inputDirectoryName + "\\" + inputFileName + inputFileType
    outputFileName = inputDirectoryName + "\\" + inputFileName + ".encrypted" + inputFileType
    cryptKey = 10 # Key to define how long the rows are for this round of crypting
    cryptMode = 'encrypt' # Set to "encrypt" or "decrypt"

    if cryptMode.lower() != 'encrypt' and cryptMode.lower() != 'decrypt': # Check to see if user entered a proper mode setting
        print(f"\'{cryptMode}\' is not a valid mode for this program.  The available modes are \'encrypt\' or \'decrypt\'.  Quitting...")
        sys.exit()

    if not os.path.exists(fullInputFileName): # Check to see if the input file exists or not
        sys.exit(f"The file \'{fullInputFileName}\' does not exist.  Quitting...")

    if os.path.exists(outputFileName): # Check to see if the output file already exists
        print(f"This will overwrite the file: \'{outputFileName}\'. (C)ontinue or (Q)uit?")
        response = input("> ")
        if not response.lower().startswith("c"):
            sys.exit("Quitting...")

    fileObj = open(fullInputFileName)
    content = fileObj.read()
    fileObj.close()
    print(len(content))


if __name__ == '__main__':
    main()
