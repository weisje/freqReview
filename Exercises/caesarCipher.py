# Caesar Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import pyperclip
import sys

# Message that will be run through the caesarCipher
message = 'This is the secret message'

key = 13 # Encryption/Decryption key number
mode = "encrypt" # Set to either encrypt or decrypt
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?." # Every symbol that is allowed to be encrypted
translated = "" # Storage variable for the crypted message

for symbol in message:
    # Check to see if the current symbol is in the allowed list of symbols
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        # Perform the cryption
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key
        else:
            sys.exit(f"\'{mode}\' is not a valid crypting mode.  Exiting.")

        # Handling for wrap around
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = symbolIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]

    else:
        translated = translated + symbol # Add the symbol without attempting to crypt it

print(translated)
pyperclip.copy(translated)