# Caesar Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import copy
import makeWordPatterns
import os
import pyperclip
import re
import simpleSubCipher
import string
import wordPatterns

LETTERS = string.ascii_uppercase
nonLettersOrSpacePattern = re.compile('[^A-Z\s]')


def main():
    message = ""

    # Determine the possible valid ciphertext translations
    print("Hacking...")
    letterMapping = hackSimpleSub(message)

    # Display results to user
    print("Mapping:")
    print(letterMapping)
    print("\nOriginal ciphertext: ")
    print(message)
    print("\nCopying hacked message to clipboard:")
    hackedMessage = decryptWithCipherletterMapping(message, letterMapping)
    pyperclip.copy(hackedMessage)
    print(hackedMessage)


def getBlankCipherletterMapping() -> dict:
    """
    Returns a dictionary that is a blank cipher letter mapping
    :return: dict
    """
    returnDict = {}
    for letter in LETTERS:
        returnDict[letter] = []
    return returnDict


def addLettersToMapping(letterMapping, cipherword, candidate) -> None:
    """
    Adds the letters in the candidate as potential decryption letters for the cipher-letters in the cipher-letters mapping.
    :param letterMapping: Takes a dictionary value that stores a cipherletter mapping, which is copied by the function
    :type letterMapping: dict
    :param cipherword: String value of the ciphertext word
    :type cipherword: str
    :param candidate: Possible English word that the cipherword could decrypt to.
    :type candidate: str
    :return: None
    """

    for i in range(len(cipherword)):  # Count through to the end of the cipherword
        if candidate[i] not in letterMapping[
            cipherword[i]]:  # Check to see if possible character already listed in letterMapping for it
            letterMapping[cipherword[i]].append(
                candidate[i])  # If it is not, then append that as a potential character in the letter mapping


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
def removeSolvedLettersFromMapping(letterMapping) -> dict:
    """
    Cipher letters in the mapping that map to only one letter are "solved" & can be removed from the other letters.
    :param letterMapping: Current full letter mapping of the potentials for the letters
    :type letterMapping: dict
    :return: dict
    """
    pass


# TODO
def hackSimpleSub(message) -> dict:
    """
    Engine to run the simple substitution hacker functions
    :param message: Message to be interrogated & decrypted
    :type message: str
    :return: dict
    """
    pass


# TODO
def decryptWithCipherletterMapping(cipherText, letterMapping) -> str:
    """
    Takes the string of the cipher text decrypted with the letter mapping & replaces any ambiguous characters with an underscore
    :param cipherText: Message that was to be decrypted
    :type cipherText: str
    :param letterMapping: Letter mapping after character/frequency analysis
    :type letterMapping: dict
    :return: str
    """
    pass


if __name__ == '__main__':
    main()
