# Portions of this code were sourced & inspired by "Cracking Codes with Python" https://www.nostarch.com/crackingcodes (BSD Licensed)
import sys


def caesarCipher(message, mode='encrypt', key=13):
    """
    Function for shifting letters of provided message a specified amount(key) in order to encrypt/decrypt it. i.e. Key 1 mode 0 turns "abc" > "bcd"
    :param message: Value that will be encrypted/decrypted
    :type message: str
    :param mode: Variable to show if the message should be encrypted('encrypt') or decrypted('decrypt')
    :type mode: str
    :param key: How far along should each symbol be shifted for the cipher
    :type key: int
    :return: str
    """
    SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?." # Every symbol that is allowed to be crypted
    message = message
    mode = mode.lower()
    key = int(key)
    translatedMessage = ""

    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol) # Locate the index within SYMBOLS for the current symbol being evaluated
            if mode == 'encrypt': # Encryption
                translatedIndex = symbolIndex + key # Shift the index of the current symbol to the right by a number equal to the provided key
            elif mode == 'decrypt': # Decryption
                translatedIndex = symbolIndex - key # Shift the index of the current symbol to the left by a number equal to the provided key
            else:
                sys.exit(f"\'{mode}\' is not a valid 'cryption mode.  Exiting")

            # Wraparound handler if the key would push the index counter beyond the count of SYMBOLS
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translatedMessage = translatedMessage + SYMBOLS[translatedIndex]
        else: # if the current symbol is not in the list of allowed symbols(SYMBOLS)
            translatedMessage = translatedMessage + symbol # Simply append the symbol to the translated message as is

    return translatedMessage


def reverseCipher(reverseSource):
    """
    Takes inputted string & provide a "mirrored"("derorrim") version of it.
    :param reverseSource: provided item to be reversed
    :type reverseSource: str
    :return: str
    """
    originalMessage = str(reverseSource)
    reversedMessage = ""
    letterCount = len(originalMessage) - 1
    while letterCount >= 0:
        reversedMessage = reversedMessage + originalMessage[letterCount]
        letterCount -= 1
    return reversedMessage


def sarcasmCipher(sourceText):
    """
    Takes inputted string & provides a "sarcastic"("sArCaStIc") output of it.
    :param sourceText: Source message provided when called
    :type sourceText: str
    :return: str
    """
    sourceMessage = str(sourceText)
    translatedMessage = ""
    letterCount = 0
    while letterCount < len(sourceMessage):
        if letterCount % 2 == 0:
            translatedMessage = translatedMessage + sourceMessage[letterCount].lower()
        else:
            translatedMessage = translatedMessage + sourceMessage[letterCount].upper()
        letterCount += 1

    return translatedMessage

def main():
    message = input("Source Message: ")
    print(caesarCipher(message))


if __name__ == '__main__':
    main()