# Simple Substitution Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import string
import pyperclip
import random
import sys

LETTERS = string.ascii_uppercase


def main():
    myMessage = 'If a man is offered a fact which goes against his instincts, he will scrutinize it closely, and unless the evidence is overwhelming, he will refuse to believe it. If, on the other hand, he is offered something which affords a reason for acting in accordance to his instincts, he will accept it even on the slightest evidence. The origin of myths is explained in this way. -Bertrand Russell'
    myKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    myMode = 'encrypt'  # Set to either 'encrypt' or 'decrypt'.

    if not keyIsValid(myKey):
        sys.exit("There is an error in the key or symbol set.")
    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    print(f"Using key {myKey}")
    print(f"The {myMode}ed message is: ")
    print(translated)
    pyperclip.copy(translated)
    print("\nThis message has been copied to the clipboard.")


def keyIsValid(key) -> bool:
    """
    Checks to see if the key & available cipher letters contain the same characters.
    :param key: Key to be compared to the available characters for the cipher.
    :type key: str
    :return: bool
    """
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    return keyList == lettersList


def encryptMessage(key, message) -> str:
    """
    Encrypts with a simple sub cipher the provided message with the provided key.
    :param key: Value to be used as a key for the encryption.
    :type key: str
    :param message: Value to be encrypted
    :type message: str
    :return: str
    """
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message) -> str:
    """
    Decrypts with a simple sub cipher the provided message with the provided key.
    :param key: Value to be used as a key for the decryption.
    :type key: str
    :param message: Value to be decrypted
    :type message: str
    :return: str
    """
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode) -> str:
    """
    Engine that runs the appropriate mode of the simple sub cipher on the provided message with the defined key.
    :param key: Value to be used as the key for the simple sub cipher.
    :type key: str
    :param message: Value to be manipulated by the simple sub cipher.
    :type message: str
    :param mode: Which mode the function should run in for the current call.  Should be 'encrypt' or 'decrypt'
    :type mode: str
    :return: str
    """
    translated = ""
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        charsA, charsB = charsB, charsA

    for symbol in message:
        if symbol.upper() in charsA:
            symbolIndex = charsA.find(symbol.upper()) # Run cipher on message
            if symbol.isupper():
                translated += charsB[symbolIndex].upper()
            else:
                translated += charsB[symbolIndex].lower()
        else:
            translated += symbol

    return translated


def getRandomKey() -> str:
    """
    Takes the available list of characters, mixes them up, & returns the result to the caller.
    :return: str
    """
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)


if __name__ == '__main__':
    main()
