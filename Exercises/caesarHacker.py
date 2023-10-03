# Caesar Cipher Hacker
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

message = "cba heddhgfedb onkm lkjii iqkp"
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?." # Every symbol that is allowed to be encrypted

# Loop through every possible key
for key in range(len(SYMBOLS)):
    translated = ""
    for symbol in message:
        if symbol in SYMBOLS: # If the symbol can be decrypted
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            if translatedIndex < 0: # Handle wraparound
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]

        else: # Append the symbol without decrypting
            translated = translated + symbol

    if key < 10:
        print(f"Key #0{key}: {translated}")
    else:
        print(f"Key #{key}: {translated}")
