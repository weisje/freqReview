# Transposition Cipher Test
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import random
import string
import sys
import transpositionDecrypt
import transpositionEncrypt


def main():
    random.seed(42) # Seed in which to generate the transposition test subjects

    for i in range(20): # Run 20 tests
        message = string.ascii_uppercase * random.randint(4, 40) # Give the message a random length
        message = list(message) # Convert message to list to mix it up more easily
        random.shuffle(message) # Shuffle the generated list of letters
        message = ''.join(message) # Convert message back to a string
        if i <= 8:
            testNumberStr = f"0{i + 1}" # Add padding for tests less than 10
        else:
            testNumberStr = f"{i + 1}"
        print(f"Test #{testNumberStr}: \"{message[:50]}...\"") # Print current random string to be tested

        for key in range(1, int(len(message)/2)): # test each message with keys 1 through half the length of the entire message(i.e. length of 400 tests keys 1 through 200).
            encrypted = transpositionEncrypt.encryptMessage(key, message) # Encrypted message for each key
            decrypted = transpositionDecrypt.decryptMessage(key, encrypted) # Decrypted string for encrypted message for each key
            if message != decrypted: # Act if decrypted message does not match plaintext message
                print(f"Mismatch with key {key} and message {message}.")
                print(f"Decrypted as {decrypted}")
                sys.exit()

    print("Transposition cipher test passed.")


if __name__ == '__main__':
    main()