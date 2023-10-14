# Detect English Module
# https://www.nostarch.com/crackingcodes (BSD Licensed)

"""
To use this code type:
  import detectEnglish
  detectEnglish.isEnglish(someString) # Returns True or False
(There must be a "dictionary.txt" file in this directory with all
English words in it, one per line.  You can download this from
https://www.nostarch.com/crackingcodes/.)
"""

import string

UPPERLETTERS = string.ascii_uppercase
LETTERS_AND_SPACE = UPPERLETTERS + string.ascii_lowercase + ' \t\n'


def loadDictionary(dictionaryFile="Resources\\dictionary.txt") -> dict:
    """
    Function for facilitating the loading of the word dictionary file into the module
    :param dictionaryFile: Filepath of the word dictionary file to be loaded into the function
    :type dictionaryFile: str(filepath)
    :return: dict
    """
    dictionaryFile = open(dictionaryFile)
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None # Loads words from dictionaryFile into a dictionary with a blank value because dicts are faster to search than lists
    dictionaryFile.close()
    return englishWords


ENGLISH_WORDS = loadDictionary()


def getEnglishCount(message) -> float:
    """
    Function that reviews provided string value, compares it to a defined word dictionary, & determines if it contains words or not.
    :param message: Value to be interrogated & compared to the word dictionary
    :type message: str
    :return: float
    """
    message = message.upper()
    message = removeNonLetters(message) # Remove characters that are not defined by the LETTERS_AND_SPACE variable
    possibleWords = message.split()

    if not possibleWords: # Book: "if possibleWords == []"
        return 0.0 # no possible words were found in message, so returns 0.0

    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS: # Check to see if the current word was found in the loaded word dictionary
            matches += 1

    return float(matches) / len(possibleWords)


# TODO
def removeNonLetters(message) -> str:
    """
    Function that facilitates the removal of characters not defined by LETTERS_AND_SPACES variable from a provided message
    :param message: Variable to have non-letters removed from
    :type message: str
    :return: str
    """
    lettersOnly = [] # Final list of characters that were not removed
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)


# TODO
def isEnglish(message, wordPercentage=20, letterPercentage=85) -> bool:
    """

    :param message:
    :type message:
    :param wordPercentage:
    :type wordPercentage:
    :param letterPercentage:
    :type letterPercentage:
    :return: bool
    """
    pass