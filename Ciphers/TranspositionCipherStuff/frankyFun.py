"""Reads the text of Frankenstein and either encrypts or decrypts it base don user input.
    Then puts the converted text into a new txt file. I should probably spend a little time
    refactoring this because right now you have to manually make sure the input and output
    files are grabbing the correct file.
"""

import time
import os
import sys
import transpositionCipher as tc


def franky_test():
    input_file_path = 'Franky.txt'
    # input_file_path = 'franky.encrypted.txt'
    key = 7

    encrypting = input('(E)ncrypting or (D)ecrypting?\n')
    if encrypting.lower().startswith('e'):
        encrypting = True
    else:
        encrypting = False

    if not os.path.exists(input_file_path):
        print(f'Sorry the file "{input_file_path}" does not exists. So I am going to give up now')
        sys.exit()

    with open(input_file_path) as f:
        all_text = f.read()

    start_time = time.time()
    if encrypting:
        converted = tc.encrypt_message(all_text, key=key)
    else:
        converted = tc.decrypt_message(all_text, key=key)
    total_time = round(time.time() - start_time, 5)
    print(f'Total encryption time was {total_time}')

    if encrypting:
        output_filename = 'franky.encrypted.txt'
    else:
        output_filename = 'franky.decrypted.txt'

    output_file = open(output_filename, 'w')
    output_file.write(converted)
    output_file.close()


if __name__ == '__main__':
    franky_test()
