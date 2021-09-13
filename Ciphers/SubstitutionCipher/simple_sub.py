import random as rd
import sys
import ciphy

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    message = '''If a man is offered a fact which goes against his instincts, he will scrutinize it closely, 
    and unless the evidence is overwhelming, he will refuse to believe it. If, on the other hand, he is offered
     something which affords a reason for acting in accordance to his instincts, he will accept it even on the 
     slightest evidence. The origin of myths is explained in this way. -Bertrand Russell'''

    key = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    validate_key(key)
    encrypted = translate_message(message, key=key, encrypting=True)
    print(f'This is the encrypted message: \n{encrypted}')
    decrypted = translate_message(encrypted, key=key, encrypting=False)
    print(f'This is the decrypted message:\n{decrypted}')


def validate_key(key):
    """Validates the key"""
    key_list = list(key)
    letters_list = list(LETTERS)
    key_list.sort()
    letters_list.sort()

    if key_list != letters_list:
        print('Sorry your key is wack, it must contain all of the letters in the alphabet')
        sys.exit()


def translate_message(message, key, encrypting=True):
    """Either encrypts or decrypts based on mode"""
    translated = []
    symbols_a = LETTERS
    symbols_b = key

    if not encrypting:
        symbols_a, symbols_b = symbols_b, symbols_a

    for symbol in message:
        if symbol.upper() in symbols_a:
            letter_index = symbols_a.find(symbol.upper())
            if symbol.isupper():
                translated.append(symbols_b[letter_index].upper())
            else:
                translated.append(symbols_b[letter_index].lower())
        else:
            translated.append(symbol)

    return ''.join(translated)


def get_random_key():
    key = list(LETTERS)
    rd.shuffle(key)
    return ''.join(key)


if __name__ == '__main__':
    main()
