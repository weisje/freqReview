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


# TODO
def loadDictionary() -> dict:
    """

    :return: dict
    """
    pass


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