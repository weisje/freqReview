# Transposition Cipher Decryption
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import math
import pyperclip


def decryptMessage(key, message):
    """
    Function for decrypting transposition cipher messages("tsinp ssrpt hmaaoiceegnsoirse") when a keylength is provided
    :param key: Value that defines the height of each column for decrypting the message
    :type key: int
    :param message: Variable of the encrypted message to be decrypted
    :type message: str
    :return: str
    """
    numOfColumns = int(math.ceil(len(message) / float(key))) # Number of "Columns" in the transposition grid.
    numOfRows = key # Number of "Rows" in the transposition grid
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message) # Number of shaded cells at the end of the message that were used as padding.

    plaintext = [''] * numOfColumns # Create a number of empty list equal to the number of columns to place characters in

    # Variables to act as a pointer to where the next character should go.
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol # Add symbol to the current column's list
        column += 1 # Move to the next column

        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes): # If to the end of a row or on the last column & hit a shaded box reset column count & add one to the row count to "move down".
            column = 0
            row += 1

    return ''.join(plaintext)


def main():
    message = "Cenoonommstmme oo snnio. s s c" # Message to be decrypted
    key = 8 # Keylength to be passed to the transposition cipher decrypter

    plaintext = decryptMessage(key, message)
    print(f"{plaintext}|") # Adds pipe ('|') to the end of the message in case there are purposeful whitespaces at the end of the decrypted message.
    pyperclip.copy(plaintext)


if __name__ == '__main__':
    main()
