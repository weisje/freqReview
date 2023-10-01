# Reverse Cipher
# https://www.nostarch.com/crackingcodes (BSD Licensed)

message = input("Message to be reversed: ")
reversedMessage = ""
letterCount = len(message) - 1

while letterCount >= 0:
    reversedMessage = reversedMessage + message[letterCount]
    letterCount = letterCount - 1

print(reversedMessage)