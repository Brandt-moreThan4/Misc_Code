"""Creates word patterns based on the words in the dictionary file"""

import pprint
import ciphy


def main():
    all_words = load_dictionary()
    pattern_dictionary = identify_patterns(all_words)
    create_new_file(pattern_dictionary)


def load_dictionary():
    """Get a list of words from dictionary text file"""
    dictionary_path = ciphy.find_file('dictionary.txt')
    with open(dictionary_path) as f:
        all_words = f.read().split('\n')

    return all_words


def get_pattern(word):
    """Gets the number pattern of a word. Separated by periods."""

    word = word.upper()
    pattern = []
    letter_num = 0
    used_letters = {}

    for letter in word:
        if letter in used_letters:
            pattern.append(used_letters[letter])
        else:
            used_letters[letter] = str(letter_num)
            pattern.append(str(letter_num))
            letter_num += 1

    return '.'.join(pattern)


def identify_patterns(words_list):
    """Create a dictionary of word patterns."""

    all_patterns = {}
    for word in words_list:
        pattern = get_pattern(word)
        if pattern not in all_patterns:
            all_patterns[pattern] = [word]
        else:
            all_patterns[pattern].append(word)

    return all_patterns


def create_new_file(pattern_dictionary):
    """Write the dictionary to a new file as an assignment statement for easy import in other modules"""
    with open('word_patterns.py', 'w') as new_file:
        new_file.write('all_patterns = ')
        new_file.write(pprint.pformat(pattern_dictionary))


if __name__ == '__main__':
    main()
