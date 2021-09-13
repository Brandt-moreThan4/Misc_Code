import os

"""Cipher stuff"""

# These constants are used in a few different functions
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACES = LETTERS + LETTERS.lower() + ' \t\n'


def gcd(num1, num2):
    while num1 != 0:
        num1, num2 = num2 % num1, num1
    return num2


def find_mod_inverse(a, m):
    """I don't know how but it works. This is from Al's book"""
    if gcd(a, m) != 1:
        return None  # No mod inverse exists if the two numbers aren't relatively prime
    u1, u2, u3, = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3  # // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


def reverse(string_input):
    """Reverses a string"""

    letter_count = len(string_input)
    backwards = ''
    x = 1
    while x <= letter_count:
        backwards += string_input[-x]
        x += 1
    return backwards


def caesar_encrypt(message, key):
    """Encrypt a message with the provided key using Caesar Cipher method."""
    message = message.upper()
    encrypted_message = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num += key
            if num > len(LETTERS) - 1:
                num -= len(LETTERS)
            encrypted_message += LETTERS[num]
        else:
            encrypted_message += symbol
    return encrypted_message


def load_dictionary():
    """Reads a file containing a bunch of words and returns a dictionary object
        dictionary used instead of list because it is faster for lookups?
        Note: dictionary text file must be in the cd
    """

    file_path = find_file('dictionary.txt')
    word_dictionary = {}
    with open(file_path) as f:
        for line in f:
            word = line.strip()
            word_dictionary[word] = None
    return word_dictionary


def remove_non_letters(stringy):
    """Remove any non letters or non spaces in a string"""
    cleaned_strings = []
    for symbol in stringy:
        if symbol in LETTERS_AND_SPACES:
            cleaned_strings.append(symbol)
    return ''.join(cleaned_strings)  # .strip('.')


def english_word_percentage(stringy):
    """Count the percentage of english words in a string"""
    english_words = load_dictionary()
    all_words = remove_non_letters(stringy).upper()
    all_words = all_words.split()

    if not all_words:
        return 0.0
    else:
        matches = 0
        for word in all_words:
            if word in english_words:
                matches += 1
    return matches / (len(all_words))


def is_english(text, word_percent_threshold=.50, letter_percent_threshold=.85):
    """Makes an educated guess on if the text provided is english or not
        based on the parameters you set for the percentage of words that should
        be english and the percentage of characters that are letters or spaces.
        I would like to find a better dictionary"""

    word_percent = english_word_percentage(text)
    letter_percent = len(remove_non_letters(text)) / len(text)

    if word_percent >= word_percent_threshold and letter_percent >= letter_percent_threshold:
        return True
    else:
        return False


def find_file(file_name):
    """searches for file name in cd and then back up path upwards. Returns absolute path
    I should make this better by deciding how many folders to go upward to make sure it can go
    upward first. If not found returning an empty string or None"""

    for root, directory, files in os.walk('../..'):
        # print(f'Files are: {files}')
        for file in files:
            # print(f'File is: {file}')
            if file == file_name:
                absolute_path = os.path.abspath(os.path.join(root, file))
                return absolute_path
