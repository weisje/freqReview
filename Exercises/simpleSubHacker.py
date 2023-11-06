# Caesar Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import copy
import makeWordPatterns
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
        if candidate[i] not in letterMapping[cipherword[i]]:  # Check to see if possible character already listed in letterMapping for it
            letterMapping[cipherword[i]].append(
                candidate[i])  # If it is not, then append that as a potential character in the letter mapping


def intersectMappings(mapA, mapB) -> dict:
    """
    Creates a blank letter map & then adds only the potential decryption characters that exist in both maps
    :param mapA: First letter mapping sample
    :type mapA: dict
    :param mapB: Second letter mapping sample
    :type mapB: dict
    :return: dict
    """
    intersectedMapping = getBlankCipherletterMapping()
    for letter in LETTERS:
        # An empty list just means "any letter is possible." In this case just copy the other map entirely.
        if not mapA[letter]:
            intersectedMapping[letter] = copy.deepcopy(mapB[letter])
        elif not mapB[letter]:
            intersectedMapping[letter] = copy.deepcopy(mapA[letter])
        else: # If a letter in mapA[letter] exists in mapB[letter], add that letter to intersectedMapping[letter].
            for mappedLetter in mapA[letter]:
                if mappedLetter in mapB[letter]:
                    intersectedMapping[letter].append(mappedLetter)

    return intersectedMapping


def removeSolvedLettersFromMapping(letterMapping) -> dict:
    """
    Cipher letters in the mapping that map to only one letter are "solved" & can be removed from the other letters.
    :param letterMapping: Current full letter mapping of the potentials for the letters
    :type letterMapping: dict
    :return: dict
    """
    loopAgain = True # Value to keep going through if there are still unsolved characters in either map that can be compared & reduced.
    while loopAgain:
        loopAgain = False # Resets the trigger to assume that we will not have to loop again

        solvedLetters = [] # List of uppercase letters that have one & only one possible mapping in letterMapping
        for cipherLetter in LETTERS:
            if len(letterMapping[cipherLetter]) == 1: # Checking to see if the letter only has one dictionary value & is therefore "solved"
                solvedLetters.append(letterMapping[cipherLetter][0])

        # If a letter is solved, then it cannot possibly be a potential decryption letter for a different ciphertext letter.  We should remove it from those other lists.
        for cipherLetter in LETTERS:
            for solved in solvedLetters:
                if len(letterMapping[cipherLetter]) != 1 and solved in letterMapping[cipherLetter]: # Check to see if the current value is in the current iteration of cipherLetters as well as if there are other characters.  If so remove the solved character from it
                    letterMapping[cipherLetter].remove(solved)
                    if len(letterMapping[cipherLetter]) == 1: # A new character has been solved, so go through the process again
                        loopAgain = True

    return letterMapping


def hackSimpleSub(message) -> dict:
    """
    Engine to run the simple substitution hacker functions
    :param message: Message to be interrogated & decrypted
    :type message: str
    :return: dict
    """
    intersectedMap = getBlankCipherletterMapping()
    cipherwordList = nonLettersOrSpacePattern.sub('', message.upper()).split()
    for cipherword in cipherwordList:
        candidateMap = getBlankCipherletterMapping() # Get a new cipherletter mapping for each ciphertext word
        wordPattern = makeWordPatterns.getWordPattern(cipherword)
        if wordPattern not in wordPatterns.allPatterns:
            continue # This word was not in our dictionary, so continue

        # Add the letters of each candidate to the mapping
        for candidate in wordPatterns.allPatterns[wordPattern]:
            addLettersToMapping(candidateMap, cipherword, candidate)

        # Intersect the new mapping with the existing intersected mapping
        intersectedMap = intersectMappings(intersectedMap, candidateMap)

    # Remove any solved letters from the other lists:
    return removeSolvedLettersFromMapping(intersectedMap)


def decryptWithCipherletterMapping(ciphertext, letterMapping) -> str:
    """
    Takes the string of the cipher text decrypted with the letter mapping & replaces any ambiguous characters with an underscore
    :param ciphertext: Message that was to be decrypted
    :type ciphertext: str
    :param letterMapping: Letter mapping after character/frequency analysis
    :type letterMapping: dict
    :return: str
    """

    # First create a simple sub key from the letterMapping mapping
    key = ['x'] * len(LETTERS)
    for cipherletter in LETTERS:
        if len(letterMapping[cipherletter]) == 1:
            # If there's only one letter, add it to the key
            keyIndex = LETTERS.find(letterMapping[cipherletter][0])
            key[keyIndex] = cipherletter
        else:
            ciphertext = ciphertext.replace(cipherletter.lower(), '_')
            ciphertext = ciphertext.replace(cipherletter.upper(), '_')

    key = ''.join(key)

    # With the key we've created, decrypt the ciphertext
    return simpleSubCipher.decryptMessage(key, ciphertext)


if __name__ == '__main__':
    main()
