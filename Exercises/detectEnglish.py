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


# TODO
def getEnglishCount(message) -> float:
    """

    :param message:
    :type message:
    :return: float
    """
    pass


# TODO
def removeNonLetters(message) -> str:
    """

    :param message:
    :type message:
    :return: str
    """
    pass


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