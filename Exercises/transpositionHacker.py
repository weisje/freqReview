# Transposition Cipher Hacker
# https://www.nostarch.com/crackingcodes (BSC Licensed)

import detectEnglish
import pyperclip
import transpositionDecrypt


def main():
    myMessage = "AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e  enlh na  indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no euarisfatt  e mealefedhsppmgAnlnoe(c -or)alat r lw o eb  nglom,Ain one dtes ilhetcdba. t tg eturmudg,tfl1e1 v  nitiaicynhrCsaemie-sp ncgHt nie cetrgmnoa yc r,ieaa  toesa- e a0m82e1w shcnth  ekh gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr aBercaeu thllnrshicwsg etriebruaisss  d iorr." # Message to be hacked
    hackedMessage = hackTransposition(myMessage)

    if hackedMessage is None:
        print("Failed to hack message")
    else:
        print("Copying hacked message to clipboard")
        print(hackedMessage)
        pyperclip.copy(hackedMessage)


def hackTransposition(message) -> str:
    """
    Function to iterate through all possible keys to attempt to find decoded text from an encrypted transposition cipher
    :param message: Encrypted transposition text to be decoded
    :type message: str
    :return: str
    """
    # Note: The book wanted me to add key prompts here on how to stop the code early but that seemed to go against the MVP of this project.  Did not include it here.
    for key in range(1, len(message)): # Loop through all possible keys up to the length of the provided message
        if key % 10 == 0:
            print(f"Trying key: {key}...")
        decryptedText = transpositionDecrypt.decryptMessage(key, message) # Submit current key to the transpositionDecrypt script to attempt to decrypt it
        if detectEnglish.isEnglish(decryptedText): # Check to see if the current message falls into the threshold of what we have defined as English
            print("\nPossible encryption hack:") # Tell the user there's a possible decryption
            print(f"key {key}: {decryptedText[:100]}\n")
            print("Enter (D)one or press any other key to continue hacking") # Prompt user if this is correct or to keep going
            response = input("> ")
            if response.strip().upper().startswith("D"):
                return decryptedText

    return None


if __name__ == '__main__':
    main()
