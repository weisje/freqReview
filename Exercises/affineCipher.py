# Affine Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import cryptoMath
import pyperclip
import random
import string
import sys

SYMBOLS = string.ascii_uppercase + string.ascii_lowercase + "1234567890 !?."


def main():
    pass


# TODO
def getKeyParts(key) -> tuple:
    """

    :param key:
    :type key:
    :return: tuple
    """
    pass


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
        if cryptoMath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB


if __name__ == '__main__':
    main()
