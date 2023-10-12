# Transposition Cipher Encrypt/Decrypt File
# https://www.nostarch.com/crackingcodes (BSC Licensed)

import os
import sys
import time
import transpositionDecrypt, transpositionEncrypt


def main():
    inputDirectoryName = "Resources"
    inputFileName = "frankenstein"
    inputQualifier = ""
    inputFileType = ".txt"
    outputQualifier = ""
    cryptKey = 10  # Key to define how long the rows are for this round of crypting
    cryptMode = 'decrypt'  # Set to "encrypt" or "decrypt"
    cryptMode = cryptMode.lower()

    if cryptMode != 'encrypt' and cryptMode != 'decrypt': # Check to see if user entered a proper mode setting
        print(f"\'{cryptMode}\' is not a valid mode for this program.  The available modes are \'encrypt\' or \'decrypt\'.  Quitting...")
        sys.exit()

    # Add some controllers based on what the user is doing; encrypting or decrypting.  This then knows what to look for as well as adding context to the results filename for the user.
    if cryptMode == 'encrypt':
        outputQualifier = ".encrypted"
    if cryptMode == 'decrypt':
        inputQualifier = ".encrypted"
        outputQualifier = ".decrypted"

    # Assigns values to the filenames based on which cryptMode the user has selected
    fullInputFileName = f"{inputDirectoryName}\\{inputFileName}{inputQualifier}{inputFileType}"
    outputFileName = f"{inputDirectoryName}\\{inputFileName}{outputQualifier}{inputFileType}"

    if not os.path.exists(fullInputFileName): # Check to see if the input file exists or not
        sys.exit(f"The file \'{fullInputFileName}\' does not exist.  Quitting...")

    if os.path.exists(outputFileName): # Check to see if the output file already exists
        print(f"This will overwrite the file: \'{outputFileName}\'. (C)ontinue or (Q)uit?")
        response = input("> ")
        if not response.lower().startswith("c"): # Assumes the user doesn't want to move forward if they select anything but the 'continue'
            sys.exit("Quitting...")

    # Read input file into the program
    fileObj = open(fullInputFileName)
    content = fileObj.read()
    fileObj.close()

    print(f"{cryptMode.title()}ing...")

    # Begin the crypting process
    startTime = time.time()
    if cryptMode == 'encrypt':
        translated = transpositionEncrypt.encryptMessage(cryptKey, content)
    elif cryptMode == 'decrypt':
        translated = transpositionDecrypt.decryptMessage(cryptKey, content)
    totalTime = round(time.time() - startTime, 2)
    print(f"{cryptMode.title()}ing time: {totalTime} seconds.")

    outputFileObj = open(outputFileName, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print(f"Done {cryptMode}ing {fullInputFileName} ({len(content)} characters).")
    print(f"{cryptMode.title()}ed file is \'{outputFileName}\'.")


if __name__ == '__main__':
    main()
