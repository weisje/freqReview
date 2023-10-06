# Transposition Cipher Decryption
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import math
import pyperclip


def decryptMessage(key, message): # TODO
    """
    Function for decrypting transposition cipher messages("tsinp ssrpt hmaaoiceegnsoirse") when a keylength is provided
    :param key: Value that defines the height of each column for decrypting the message
    :type key: int
    :param message: Variable of the encrypted message to be decrypted
    :type message: str
    :return: str
    """
    numOfColumns = int(math.ceil(len(message) / float(key)))
    plaintext = [''] * numOfColumns

    return ''.join(plaintext)


def main():
    message = "Cenoonommstmme oo snnio. s s c" # Message to be decrypted
    key = 8 # Keylength to be passed to the transposition cipher decrypter

    plaintext = decryptMessage(key, message)
    print(f"{plaintext}|") # Adds pipe ('|') to the end of the message in case there are purposeful whitespaces at the end of the decrypted message.
    pyperclip.copy(plaintext)


if __name__ == '__main__':
    main()
