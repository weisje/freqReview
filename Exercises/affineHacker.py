# Affine Cipher Hacker
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import affineCipher
import cryptoMath
import detectEnglish
import pyperclip


# TODO
def main():
    pass


def hackAffine(message) -> str | None:
    """
    Function for brute-forcing messages that are suspected to be encrypted with an Affine Cipher
    :param message: Variable to be interrogated to see if it can be decrypted
    :type message: str
    :return: str
    """
    print("Hacking...")

    for key in range(len(affineCipher.SYMBOLS) ** 2): # Iterate through all the possible keys up to the square of the length of allowed symbols
        keyA = affineCipher.getKeyParts(key)[0]
        if cryptoMath.gcd(keyA, len(affineCipher.SYMBOLS)) != 1:
            continue
        decryptedText = affineCipher.decryptMessage(key, message)
        if not SILENT_MODE:
            print(f"Tried key {key}... {decryptedText[:40]}")

        if detectEnglish.isEnglish(decryptedText): # If we find possible English according to the dictionary
            print("\nPossible encryption hack:")
            print(f"Key: {key}")
            print(f"Decrypted message: {decryptedText[:200]}\n")
            print("Enter (D)one if correct or press Enter to continue hacking:") # Check with user to see if we want to stop here or keep trying
            response = input("> ")

            if response.strip().upper().startswith("D"):
                return decryptedText

    return None


if __name__ == '__main__':
    main()
