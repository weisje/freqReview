# Portions of this code were sourced & inspired by "Cracking Codes with Python" https://www.nostarch.com/crackingcodes (BSD Licensed)
import math
import pyperclip
import os
import random
import string
import sys
import time


def gcd(a, b) -> int:
    """
    Function for calculating the greatest common denominator of two provided numbers using Euclid's algorithm
    :param a: First value to be compared
    :type a: int
    :param b: Second value to be compared
    :type b: int
    :return: int
    """
    while a != 0:
        a, b = b % a, a
    return b


# TODO
def findModInverse(a, m) -> int | None:
    """
    Function for finding the Mod inverse of a % m, which is the number x such that a*x % m = 1
    :param a: Integer to be multiplied by the suspected value
    :type a: int
    :param m: Modulo that will make the result of a * suspected value equal 1
    :type m: int
    :return: int | None
    """
    pass

def hackTranspositionEngine(message, checkInAmount=10) -> str:
    """
    Mechanical operation of cracking transposition ciphers.  Iterates through keys to the length of the message & attempts to decrypt with said keys
    :param message: Encrypted transposition message to be cracked
    :type message: str
    :param checkInAmount: Which keys(via modulo) should the program check in with the user while attempting to crack the message
    :type checkInAmount: int
    :return: str
    """
    for key in range(1, len(message)):
        if key % checkInAmount == 0:
            print(f"Trying key: {key}")
        decryptedMessage = transpositionDecrypt(key, message)

        if isEnglish(decryptedMessage): # If the results of the decrypted message fall into what we have defined as English, then prompt the user for feedback
            print("\nPossible encryption hack:")
            print(f"Key {key}: {decryptedMessage[:100]}")
            print(f"Enter (D)one or press any other key to continue.") # If user presses anything other than "D" then it will keep going through keys.
            response = input("> ")

            if response.strip().upper().startswith("D"):
                return decryptedMessage

    return None


def hackTranspositionController(message) -> None:
    """
    Function for coordinating the cracking of transposition ciphers by orchestrating the operation of the process
    :param message: Encrypted transposition message to be cracked
    :type message: str
    :return: str
    """
    myMessage = message

    hackedMessage = hackTranspositionEngine(myMessage)

    if hackedMessage is None:
        print("Failed to hack encryption.")
    else:
        print("Copying hacked message to clipboard")
        print(hackedMessage)
        pyperclip.copy(hackedMessage)


def loadDictionary(fullFileName) -> dict:
    """
    Function for loading a defined text file containing words on single lines into the program & returning it as a python dictionary
    :param fullFileName: Full file path to where the text file can be found for loading
    :type fullFileName: txt
    :return: dict
    """
    dictionaryWords = {}
    with open(fullFileName, 'r') as dictionaryFile:
        for word in dictionaryFile.read().split('\n'):
            dictionaryWords[word] = None # Apply each word to dictionaryWords as the key with no value.  This is because dicts are faster to search than lists
    dictionaryFile.close()
    return dictionaryWords


def getEnglishCount(message, DICTIONARY_WORDS, APPROPRIATE_CHARACTERS) -> float:
    """
    Function to search the provided message for words found in the DICTIONARY_WORDS variable & return a total ratio of words to length of all possible words
    :param message: String to be interrogated for words found in DICTIONARY_WORDS
    :type message: str
    :param DICTIONARY_WORDS: Dictionary of words to search when determining if the provided message has "real" words in it or not
    :type DICTIONARY_WORDS: dict
    :param APPROPRIATE_CHARACTERS: String of all the allowed characters in the message
    :type APPROPRIATE_CHARACTERS: str
    :return: float
    """

    message = message.upper()
    message = removeNonLetters(message, APPROPRIATE_CHARACTERS)
    possibleWords = message.split()

    if not possibleWords:  # If there are no possible words(because there are no appropriate characters) then return a 0.0 to say "Hey there isn't anything coherent here
        return 0.0

    matches = 0 # Variable for counting the number of matching words found from the message within the DICTIONARY_WORDS
    for word in possibleWords:
        if word in DICTIONARY_WORDS:
            matches += 1
    return float(matches) / len(possibleWords)


def removeNonLetters(message, APPROPRIATE_CHARACTERS) -> str:
    """
    Function for returning the provided message with all undefined/inappropriate characters removed
    :param message: Message to be reviewed & have undefined/inappropriate characters removed
    :type message: str
    :param APPROPRIATE_CHARACTERS: All characters that are allowed within the provided message
    :type APPROPRIATE_CHARACTERS: str
    :return: str
    """
    appropriateCharsOnly = []
    for symbol in message:
        if symbol in APPROPRIATE_CHARACTERS:
            appropriateCharsOnly.append(symbol)

    return ''.join(appropriateCharsOnly)


def isEnglish(message, wordPercentage=20, letterPercentage=85, wordFileName="Exercises\\Resources\\dictionary.txt", APPROPRIATE_CHARACTERS=string.ascii_uppercase+string.ascii_lowercase+" \t\n") -> bool:
    """
    Function for determining if a provided message contains an acceptable percentage of allowed letters & has an appropriate amount of defined words to determine if it is English.
    :param message: String value/phrase to be reviewed
    :type message: str
    :param wordPercentage: Minimum percentage of words that must exist in the message from the wordFile
    :type wordPercentage: float
    :param letterPercentage: Minimum ratio of characters in the message that are featured in APPROPRIATE_CHARACTERS
    :type letterPercentage: float
    :param wordFileName: Full file path to where the text file can be found for loading
    :type wordFileName: str
    :param APPROPRIATE_CHARACTERS: String of characters that are allowed in the message
    :type APPROPRIATE_CHARACTERS: str
    :return: bool
    """
    wordDictionary = loadDictionary(wordFileName)

    try:
        wordsMatch = getEnglishCount(message, wordDictionary, APPROPRIATE_CHARACTERS) * 100 >= wordPercentage
        numLetters = len(removeNonLetters(message, APPROPRIATE_CHARACTERS))
        messageLettersPercentage = float(numLetters) / len(message) * 100
        lettersMatch = messageLettersPercentage >= letterPercentage
        return wordsMatch and lettersMatch

    except ZeroDivisionError:
        print("The isEnglish() function has attempted to divide by zero.  This is likely due to an empty message string being fed to the function")
        print(f"Provided message length: {len(message)}")
        sys.exit("Quitting...")


def transpositionFileCipher(inputDirectoryName, inputFileName, inputFileType, cipherKey=10, cipherMode="encrypt", inputQualifier="") -> None:
    """
    Function for applying transposition cipher to entire files stored on the machine's directory.
    :param inputDirectoryName: Name of the folder/filepath that the file to be worked with is stored
    :type inputDirectoryName: str
    :param inputFileName: Name of the file, not including qualifiers(like ".encrypted") or filetypes(like ".txt"), that is to be worked.
    :type inputFileName: str
    :param inputFileType: Filetype of the file to be worked, including leading period(".txt")
    :type inputFileType: str
    :param cipherKey: Value to define the length of each "row" when working with the file
    :type cipherKey: int
    :param cipherMode: Mode in which the program will run, either in encryption mode("encrypt") or decryption mode("decrypt")
    :type cipherMode: str
    :param inputQualifier: Qualifiers that may have been added to the file during previous working(like ".encrypted") that could mess with the file's locating
    :type inputQualifier: str
    :return: None
    """

    cipherMode = cipherMode.lower()

    if cipherMode != 'encrypt' and cipherMode != 'decrypt': # Check to assure that the user has only entered an allowed value when entering the cipherMode value
        print(f"\'{cipherMode}\' is not a valid mode for this function.  The available modes are \'encrypt\' or \'decrypt\'.")
        sys.exit("Quitting...")

    outputQualifier = f".{cipherMode}ed"

    if cipherMode == 'decrypt':
        inputQualifier = '.encrypted'

    # Generate filepaths based on the cipherMode that the user has created for the input file & output file
    fullInputFileName = f"{inputDirectoryName}\\{inputFileName}{inputQualifier}{inputFileType}"
    fullOutputFileName = f"{inputDirectoryName}\\{inputFileName}{outputQualifier}{inputFileType}"

    if not os.path.exists(fullInputFileName): # Check to see if the input file exists & can be found on the system
        print(f"\'{fullInputFileName}\' does not exist")
        sys.exit("Quitting...")

    if os.path.exists(fullOutputFileName): # Check if the output file already exists & can be found
        print(f"This will overwrite the file: \'{fullOutputFileName}\'. (C)ontinue or (Q)uit?")
        response = input("> ")
        if not response.lower().startswith('c'): # If the file does exist & the user selects anything but 'c', exit the program.
            sys.exit('Quitting...')

    # Read the input file into the function
    try:
        with open(fullInputFileName) as fileObj:
            content = fileObj.read()
            fileObj.close()
    except Exception as e:
        print(f"While running the reading phase of function function was met with an exception: \'{e}\'.")
        sys.exit("Quitting...")

    print(f"{cipherMode.title()}ing \'{inputFileName}{inputQualifier}{inputFileType}\'...")

    # Begin of ciphering process
    startTime = time.time()
    try:
        if cipherMode == 'encrypt':
            translated = transpositionEncrypt(cipherKey, content)
        elif cipherMode == 'decrypt':
            translated = transpositionDecrypt(cipherKey, content)
    except Exception as e:
        print(f"While running cipher phase of function function was met with an exception: \'{e}\'.")
        sys.exit("Quitting...")
    totalTime = round(time.time() - startTime, 2)
    print(f"{cipherMode.title()}ing time: {totalTime} seconds.")
    # End of ciphering process

    # Write the translated object into the output file
    try:
        with open(fullOutputFileName, 'w') as outputFileObj:
            outputFileObj.write(translated)
        outputFileObj.close()
    except Exception as e:
        print(f"While running the writing phase of function function was met with an exception: \'{e}\'.")
        sys.exit("Quitting...")

    print(f"Done {cipherMode.title()}ing \'{fullInputFileName} ({len(content)} characters)")
    print(f"{cipherMode.title()}ed file is \'{fullOutputFileName}\'.")

def transpositionTest(randomSeed=42, testCases=20, messageBody=string.ascii_uppercase, messageDisplayLength=50) -> None:
    """
    Function for testing the functional operation of the transpositionEncrypt() & transpositionDecrypt() functions.
    :param randomSeed: Anchoring variable to base the generation of random characters
    :type randomSeed: int
    :param testCases: How many test cases should be run for the current test
    :type testCases: int
    :param messageBody: Characters that are allowed in the random character generation
    :type messageBody: str
    :param messageDisplayLength:How many characters for teach test case should be displayed when printing them
    :type messageDisplayLength: int
    :return: None
    """

    random.seed(randomSeed) # Set anchor seed for generation of test bodies
    for currentTest in range(testCases): # Perform a number of tests equal to the testCases variable
        message = messageBody * random.randint(4, 40) # Generate messages with between 4 & 40 iterations of the messageBody contents

        # Convert message contents from str to list, shuffle it up, & turn the shuffled mess back into a str.
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)

        # Print the current test body & add a padding zero if its count is nine or less.
        if currentTest + 1 <= 9:
            print(f"Test 0{currentTest + 1}: \"{message[:messageDisplayLength]}...\"")
        else:
            print(f"Test {currentTest + 1}: \"{message[:messageDisplayLength]}...\"")

        for key in range(1, int(len(message) / 2)): # Perform a number of tests equal to half the total length of the message.
            encryptedMessage = transpositionEncrypt(key, message)
            decryptedMessage = transpositionDecrypt(key, encryptedMessage)

            if message != decryptedMessage: # If the decrypt failed & produced something other than the original message
                print(f"Mismatch with key {key} & message \"{message}\".\nDecrypted as: \"{decryptedMessage}\"")
                sys.exit()

    print("Transposition cipher test passed.")


def transpositionDecrypt(keyLength, message) -> str:
    """
    Function for decrypting transposition cipher messages("tsinp ssrpt hmaaoiceegnsoirse") when a keylength is provided
    :param keyLength: Value that defines the height of each column for decrypting the message
    :type keyLength: int
    :param message: Variable of the encrypted message to be decrypted
    :type message: str
    :return: str
    """
    key = int(keyLength)
    message = str(message)
    numOfColumns = int(math.ceil(len(message) / float(key))) # Number of "Columns" in the transposition grid.
    numOfRows = key # Number of "Rows" in the transposition grid.
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)  # Number of shaded cells at the end of the message that were used as padding.

    plaintext = [''] * numOfColumns # Generate a number of empty lists equal to the number of columns to place characters while decrypting

    # Variables that act as pointers for placing characters from the message while decrypting the message
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1

        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes): # If to the end of a row or on the last column & hit a shaded box reset column count & add one to the row count to "move down".
            column = 0
            row += 1

    return ''.join(plaintext)


def transpositionEncrypt(keyLength, message) -> str:
    """
    Function for performing a transposition cipher encryption on a provided message
    :param keyLength: Length of each entry for the transposition cipher to work with
    :type keyLength: int
    :param message: Message to be encrypted
    :type message: str
    :return: str
    """
    key = int(keyLength)
    message = str(message)
    cipherText = [''] * key # Generate a number of lists equal to the key value to act as the column holders for the provided message

    for column in range(key): # Loop through for each column by the key value
        currentIndex = column # Set initial index value to match that of the current working column
        while currentIndex < len(message): # Work until the working index is less than the length of the current message.
            cipherText[column] += message[currentIndex] # Add the letter at the current working index to ciphertext list for the current working column
            currentIndex += key # Increase the index by the value of the key. This is the main mechanical worker for this transposition cipher.

    return ''.join(cipherText) # Return the cipher as a single string.


def caesarHacker(message, SYMBOLS="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.") -> None:
    """
    Function for solving caesar ciphers through bruteforce by iterating through every possible key to solve the message.
    :param message: Variable of the message to be decrypted
    :type message: str
    :param SYMBOLS: Variable of all the possible encryption characters available for the decryption attempt
    :type SYMBOLS: str
    :return: None
    """
    message = str(message)
    SYMBOLS = str(SYMBOLS)

    for key in range(len(SYMBOLS)):
        translated = ""
        for symbol in message:
            if symbol in SYMBOLS: # If the symbol is able to be decrypted
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key

                if translatedIndex < 0: # Handle wraparound to bring it to the end if it would cause an underflow error.
                    translatedIndex = translatedIndex + len(SYMBOLS)
                translated = translated + SYMBOLS[translatedIndex]

            else: # If the symbol cannot be decrypted just append it directly
                translated = translated + symbol

        if key < 10:
            print(f"Key 0{key}: {translated}")
        else:
            print(f"Key {key}: {translated}")


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
    myMessage = "AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e  enlh na  indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no euarisfatt  e mealefedhsppmgAnlnoe(c -or)alat r lw o eb  nglom,Ain one dtes ilhetcdba. t tg eturmudg,tfl1e1 v  nitiaicynhrCsaemie-sp ncgHt nie cetrgmnoa yc r,ieaa  toesa- e a0m82e1w shcnth  ekh gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr aBercaeu thllnrshicwsg etriebruaisss  d iorr."
    hackTranspositionController(myMessage)


if __name__ == '__main__':
    main()
