# Transposition Cipher Encryption
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import pyperclip

def main():
    myMessage = 'Common sense is not so common.'
    myKey = 8

    cipherText = encryptMessage(myKey, myMessage)
    print(cipherText + '|')
    pyperclip.copy(cipherText)

def encryptMessage(key, message):
    """
    Function for encrypting provided message as transposition cipher
    :param key: length of each line for the provided message
    :type key: int
    :param message: Message to be encrypted with transposition cipher
    :type message: str
    :return: str
    """

    cipherText = [''] * key

    for column in range(key):
        currentIndex = column
        while currentIndex < len(message):
            cipherText[column] += message[currentIndex]
            currentIndex += key

    return ''.join(cipherText)

if __name__ == '__main__':
    main()