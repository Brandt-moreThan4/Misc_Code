"""Decrypting a Caesar Cipher with Brute Force"""
import ciphy

message = 'We shall run and not grow weary'
encrypted_message = ciphy.caesar_encrypt(message, key=10)
print(f'The message is: "{message}"')
print(f'The Encrypted message is: "{encrypted_message}" \n')
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
translated_messages = []
# Try all possible keys and add description attempt to list to spot check which one looks correct.
for key in range(len(LETTERS)):
    translated_message = ''

    for symbol in encrypted_message:
        # This makes sense if you google how the Caesar Cipher works
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num -= key
            if num < 0:
                num += len(LETTERS)
            translated_message += LETTERS[num]
        else:
            # If we don't recognize the symbol then just stick it in anyway
            translated_message += symbol
    translated_messages.append(translated_message)

for message in translated_messages:
    print(message)