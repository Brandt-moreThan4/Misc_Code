import sys
import random as rd
import ciphy

# note the space at the front
SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""


def get_key_parts(key):
    """Translates an initial key into two sub-keys which are both used in the cipher"""
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return keyA, keyB


def validate_keys(keyA, keyB, mode='encrypt'):
    """Checks to make sure your keys aren't wack. Exits program if they are wack"""
    if mode == 'encrypt':
        if keyA == 1:
            sys.exit('The affine cipher is shit when key a is set to 1. Do better.')
        if keyB == 0:
            sys.exit('The affine cipher is shit when key  is set to 0. Do better.')
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        sys.exit(f'Keys A and B must be greater than 0. Key B must be between 0 and {len(SYMBOLS) - 1}. Try again')
    if ciphy.gcd(keyA, len(SYMBOLS)) != 1:
        # Below is needed I think because otherwise you could have duplicate mappings for letters
        sys.exit(f'Yo sorry, but Key A:"{keyA}" and the symbol set size:"{len(SYMBOLS)}" are not relatively prime. '
                 f'Choose a different key.')


def encrypt_message(message, key):
    """Encrypts the message with Affine Cipher method"""
    keyA, keyB = get_key_parts(key)
    validate_keys(keyA, keyB)
    cipher_message = []
    for symbol in message:
        if symbol in SYMBOLS:
            symbol_index = SYMBOLS.find(symbol)
            cipher_message.append(SYMBOLS[(symbol_index * keyA + keyB) % len(SYMBOLS)])
        else:
            cipher_message.append(symbol)
    return ''.join(cipher_message)


def decrypt_message(message, key):
    """Decrypts the message with Affine Cipher method"""
    keyA, keyB = get_key_parts(key)
    validate_keys(keyA, keyB, mode='decrypt')
    translated_text = []
    mod_inverse_of_A = ciphy.find_mod_inverse(keyA, len(SYMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            symbol_index = SYMBOLS.find(symbol)
            # I don't understand how below works
            translated_text.append(SYMBOLS[(symbol_index - keyB) * mod_inverse_of_A % len(SYMBOLS)])
        else:
            translated_text.append(symbol)
    return ''.join(translated_text)


def get_random_valid_key():
    """Returns a random, valid key..."""
    while True:
        keyA = rd.randint(2, len(SYMBOLS))
        keyB = rd.randint(2, len(SYMBOLS))

        if ciphy.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB


def main():
    message = '''"A computer would deserve to be called intelligent if it could deceive a human into believing
    that it was human." - Alan turing'''

    key = 2023
    encrypted_text = encrypt_message(message, key)
    print(f'Encrypted Message is:\n{encrypted_text}')
    decrypted_text = decrypt_message(encrypted_text, key)
    print(f'Decrypted Message is:\n{decrypted_text}')


if __name__ == '__main__':
    main()
