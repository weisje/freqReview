# Affine Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import cryptoMath
import pyperclip
import random
import string
import sys

SYMBOLS = string.ascii_uppercase + string.ascii_lowercase + "1234567890 !?."


def main():
    myMessage = """"A computer would deserve to be called intelligent 
    if it could deceive a human into believing that it was human."
    -Alan Turing"""
    myKey = 2894
    myMode = 'encrypt' # Set to either 'encrypt' or 'decrypt'

    if myMode.lower() == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode.lower() == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    else: # What to do if myMode is not set to an acceptable value
        print(f"\'{myMode}\' is not a valid mode for affineCipher.py.  Restart with either 'encrypt' or 'decrypt' selected.")
        sys.exit("Quitting...")

    print(f"Key: {myKey}")
    print(f"{myMode.title()}ed text:")
    print(translated)
    pyperclip.copy(translated)
    print(f"Full {myMode}ed text copied to the clipboard.")


def getKeyParts(key) -> tuple:
    """
    Function for returning the two portions of a provided key; the floor division of the provided key & the length of the SYMBOLS variable(keyA) as well as the modulo of the provided key & the length of the SYMBOLS variable(keyB).
    :param key: Number to be mathed upon to generate the two different keys
    :type key: int
    :return: tuple
    """
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    keyTuple = (keyA, keyB)
    return keyTuple


# TODO
def checkKeys(keyA, keyB, mode) -> None:
    """

    :param keyA:
    :type keyA:
    :param keyB:
    :type keyB:
    :param mode:
    :type mode:
    :return: None
    """
    pass


# TODO
def encryptMessage(key, message) -> str:
    """

    :param key:
    :type key:
    :param message:
    :type message:
    :return: str
    """
    pass


# TODO
def decryptMessage(key, message) -> str:
    """

    :param key:
    :type key:
    :param message:
    :type message:
    :return: str
    """
    pass


def getRandomKey() -> int:
    """
    Function for generating two random set of integers based on the length of the SYMBOLS variable, checking to see if the first is relatively prime with the length of the SYMBOLS variable, & returning the product of the first & the length of SYMBOLS summed with the second.
    :return: int
    """
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if cryptoMath.gcd(keyA, len(SYMBOLS)) == 1: # If keyA is relatively prime to the length of the SYMBOLS variable
            return keyA * len(SYMBOLS) + keyB


if __name__ == '__main__':
    main()
