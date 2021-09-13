import math
import random as rd
import sys
import  os

import ciphy


def encrypt_message(message, key):
    cipher_text = ['' for x in range(key)]
    for col in range(key):
        pointer = col

        while pointer < len(message):
            cipher_text[col] += message[pointer]
            pointer += key
    return ''.join(cipher_text)


def decrypt_message(secret_message, key):
    """Decrypt a Transposition Cipher given the key."""
    num_of_columns = math.ceil(len(secret_message) / key)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_rows * num_of_columns) - len(secret_message)
    decrypted_grid = [''] * num_of_columns

    col = 0
    row = 0

    for letter in secret_message:
        decrypted_grid[col] += letter
        col += 1

        if col == num_of_columns or (col == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1

    return ''.join(decrypted_grid)


def hack_transposition(text):
    """Try to decrypt using a shit tone of different keys and hope one looks
        like it might be intelligible"""
    print(f'About to try to hack. There are {len(text)} possible keys.')
    for key in range(1, len(text)):
        print(f'Trying key: {key}')
        decrypted_text = decrypt_message(text, key)
        if ciphy.is_english(decrypted_text):
            print(f'We may have a match!')
            print(f'How does this looks?\n{decrypted_text[:150]}')
            response = input('\nY for yes. Press enter to keep exploring>>')
            if response.strip().upper() == 'Y':
                return decrypted_text
    return None


def brute_force_hack():
    print(f'cd = {os.getcwd()}')
    text = """Cb b rssti aieih rooaopbrtnsceee er es no npfgcwu plri
ch nitaalr eiuengiteehb(e1 hilincegeoamn fubehgtarndcstudmd nM eu eacBoltaetee
oinebcdkyremdteghn.aa2r81a condari fmps" tad l t oisn sit u1rnd stara nvhn fs
edbh ee,n e necrg6 8nmisv l nc muiftegiitm tutmg cm shSs9fcie ebintcaets h a
ihda cctrhe ele 1O7 aaoem waoaatdahretnhechaopnooeapece9etfncdbgsoeb uuteitgna.
rteoh add e,D7c1Etnpneehtn beete" evecoal lsfmcrl iu1cifgo ai. sl1rchdnheev sh
meBd ies e9t)nh,htcnoecplrrh ,ide hmtlme. pheaLem,toeinfgn t e9yce da' eN eMp a
ffn Fc1o ge eohg dere.eec s nfap yox hla yon. lnrnsreaBoa t,e eitsw il ulpbdofg
BRe bwlmprraio po droB wtinue r Pieno nc ayieeto'lulcih sfnc ownaSserbereiaSm
-eaiah, nnrttgcC maciiritvledastinideI nn rms iehn tsigaBmuoetcetias rn"""

    with open('franky.encrypted.txt') as f:
        text = f.read()

    hacked_message = hack_transposition(text)
    if hacked_message is None:
        print('Guess you were not able to hack it')
    else:
        print(f'Nice!! The hacked message is:\n{hacked_message}')


if __name__ == '__main__':
    pass
    #brute_force_hack()
