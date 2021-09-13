import re
import os
import copy
import pprint
import simple_sub
import word_patterns
import make_word_patterns
import ciphy

LETTERS = ciphy.LETTERS
non_letters_or_spaces_pattern = re.compile('[^A-Z\s]')


def main():
    message = '''Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo
     txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu
      eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj
       aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm'''

    print("Let's go.")
    letter_mapping = hack_simple_sub(message)

    print(f"Mapping:")
    pprint.pprint(letter_mapping)
    decrypted = decrypt_with_cipher_letter_mapping(message, letter_mapping)
    print(f"Decrypted:\n{decrypted}")



def get_blank_cipher_letter_mapping():
    """Returns a dictionary value that is a blank cipherletter mapping."""
    return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [],
            'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [],
            'Y': [], 'Z': []}


def add_letters_to_mapping(master_mapping, cipher_word, candidate):
    """Adds new potential mappings from the candidate to the master mapping if not already there"""

    # Not sure why the below deep copy is necessary?
    master_mapping = copy.deepcopy(master_mapping)

    for i in range(len(cipher_word)):
        if candidate[i] not in master_mapping[cipher_word[i]]:
            master_mapping[cipher_word[i]].append(candidate[i])

    return master_mapping

def intersect_mappings(map_a, map_b):
    """Find a letter mapping with only mappings found in both provided maps."""

    intersected_mapping = get_blank_cipher_letter_mapping()

    for letter in LETTERS:
        if map_a[letter] == []:
            intersected_mapping[letter] = copy.deepcopy(map_b[letter])
        elif map_b[letter] == []:
            intersected_mapping[letter] = copy.deepcopy(map_a[letter])
        else:
            for mapped_letter in map_a[letter]:
                if mapped_letter in map_b[letter]:
                    intersected_mapping[letter].append(mapped_letter)

    return intersected_mapping


def remove_solved_letters(master_mapping):
    """Cleans up the mapping by removing the 'solved' letters from other mappings that contain these solved letters"""

    master_mapping = copy.deepcopy(master_mapping)
    loop_again = True

    while loop_again:
        loop_again = False

        solved_letters = []
        for letter in LETTERS:
            if len(master_mapping[letter]) == 1:
                solved_letters.append(master_mapping[letter][0])

        for letter in LETTERS:
            for solved_letter in solved_letters:
                if len(master_mapping[letter]) > 1 and solved_letter in master_mapping[letter]:
                    master_mapping[letter].remove(solved_letter)
                    if len(master_mapping[letter]) == 1:
                        loop_again = True

    return master_mapping

def hack_simple_sub(message):
    """Put stuff here"""
    intersected_map = get_blank_cipher_letter_mapping()
    cipher_word_list = non_letters_or_spaces_pattern.sub('', message.upper()).split()

    for cipher_word in cipher_word_list:
        new_map = get_blank_cipher_letter_mapping()
        word_pattern = make_word_patterns.get_pattern(cipher_word)
        if word_pattern not in word_patterns.all_patterns:
            continue

        for candidate in word_patterns.all_patterns[word_pattern]:
            new_map = add_letters_to_mapping(new_map, cipher_word, candidate)

        intersected_map = intersect_mappings(intersected_map, new_map)

    return remove_solved_letters(intersected_map)


def decrypt_with_cipher_letter_mapping(cipher_text, letter_mapping):
    """Return decrypted string using the letter mapping provided"""
    key = ['x'] * len(LETTERS)
    for cipher_letter in LETTERS:
        if len(letter_mapping[cipher_letter]) == 1:
            key_index = LETTERS.find(letter_mapping[cipher_letter][0])
            key[key_index] = cipher_letter
        else:
            cipher_text = cipher_text.replace(cipher_letter.lower(), '_')
            cipher_text = cipher_text.replace(cipher_letter.upper(), '_')

    key = ''.join(key)
    decrypted = simple_sub.translate_message(cipher_text, key=key, encrypting=False)
    return decrypted


if __name__ == '__main__':
    main()