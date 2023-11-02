# Caesar Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import copy
import makeWordPatterns
import os
import pyperclip
import simpleSubCipher
import wordPatterns


def main():
    pass


# TODO
def getBlankCipherletterMapping() -> dict:
    """
    Returns a dictionary that is a blank cipher letter mapping
    :return: dict
    """
    pass


# TODO
def addLettersToMapping(letterMapping, cipherword, candidate) -> None:
    """
    Adds the letters in the candidate as potential decryption letters for the cipherletters in the cipherletters mapping.
    :param letterMapping: Takes a dictionary value that stores a cipherletter mapping, which is copied by the function
    :type letterMapping: dict
    :param cipherword: String value of the ciphertext word
    :type cipherword: str
    :param candidate: Possible English word that the cipherword could decrypt to.
    :type candidate: str
    :return: None
    """
    pass


# TODO
def intersectMapping(mapA, mapB) -> dict:
    """
    Creates a blank letter map & then adds only the potential decryption characters that exist in both maps
    :param mapA: First letter mapping sample
    :type mapA: dict
    :param mapB: Second letter mapping sample
    :type mapB: dict
    :return: dict
    """
    pass


# TODO
def removeSolvedLettersFromMapping():
    pass


# TODO
def hackSimpleSub():
    pass


# TODO
def decryptWithCipherletterMapping():
    pass


if __name__ == '__main__':
    main()
