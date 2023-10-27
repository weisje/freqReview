# Simple Substitution Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import string
import pyperclip
import random
import sys

LETTERS = string.ascii_uppercase


# TODO
def main():
    pass


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


# TODO
def encryptMessage(key, message) -> str:
    """
    Encrypts with a simple sub cipher the provided message with the provided key.
    :param key: Value to be used as a key for the encryption.
    :type key: str
    :param message: Value to be encrypted
    :type message: str
    :return: str
    """
    pass


# TODO
def decryptMessage(key, message) -> str:
    """
    Decrypts with a simple sub cipher the provided message with the provided key.
    :param key: Value to be used as a key for the decryption.
    :type key: str
    :param message: Value to be decrypted
    :type message: str
    :return: str
    """
    pass


# TODO
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
    pass


# TODO
def getRandomKey() -> str:
    """
    Takes the available list of characters, mixes them up, & returns the result to the caller.
    :return: str
    """
    pass


if __name__ == '__main__':
    main()
