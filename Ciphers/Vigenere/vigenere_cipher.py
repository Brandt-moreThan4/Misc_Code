from ciphy import LETTERS


def main():
    """Bulk"""

    myMessage = """Alan Mathison Turing was a British mathematician,
    logician, cryptanalyst, and computer scientist. He was highly influential in
    the development of computer science, providing a formalisation of the concepts
    of "algorithm" and "computation" with the Turing machine. Turing is widely
    considered to be the father of computer science and artificial intelligence.
    During World War II, Turing worked for the Government Code and Cypher School
    (GCCS) at Bletchley Park, Britain's codebreaking centre. For a time he was head
    of Hut 8, the section responsible for German naval cryptanalysis. He devised a
    number of techniques for breaking German ciphers, including the method of the
    bombe, an electromechanical machine that could find settings for the Enigma
    machine. After the war he worked at the National Physical Laboratory, where he
    created one of the first designs for a stored-program computer, the ACE. In
    1948 Turing joined Max Newman's Computing Laboratory at Manchester University,
    where he assisted in the development of the Manchester computers and became
    interested in mathematical biology. He wrote a paper on the chemical basis of
    morphogenesis, and predicted oscillating chemical reactions such as the
    Belousov-Zhabotinsky reaction, which were first observed in the 1960s. Turing's
    homosexuality resulted in a criminal prosecution in 1952, when homosexual acts
    were still illegal in the United Kingdom. He accepted treatment with female
    hormones (chemical castration) as an alternative to prison. Turing died in
    1954, just over two weeks before his 42nd birthday, from cyanide poisoning. An
    inquest determined that his death was suicide; his mother and some others
    believed his death was accidental. On 10 September 2009, following an Internet
    campaign, British Prime Minister Gordon Brown made an official public apology
    on behalf of the British government for "the appalling way he was treated." As
    of May 2012 a private member's bill was before the House of Lords which would
    grant Turing a statutory pardon if enacted."""

    encrypted_messaged = translate_message(myMessage, key='ASIMOV', method='encrypt')
    print(f'Encrypted = \n{encrypted_messaged}')
    decrypted_message = translate_message(encrypted_messaged, key='ASIMOV', method='decrypt')
    print(f'Decrypted = \n{decrypted_message}')


def translate_message(message, key, method):
    """Either Encrypt or decrypt message based on method selected"""

    translated = []
    key_index = 0
    key = key.upper()

    for symbol in message:
        letter_index = LETTERS.find(symbol.upper())
        if letter_index == -1:
            # Just append the mystery symbol if it is not found.
            translated.append(symbol)
        else:
            if method == 'encrypt':
                letter_index += LETTERS.find(key[key_index])
            elif method == 'decrypt':
                letter_index -= LETTERS.find(key[key_index])

            # ??? Don't know why the below works
            letter_index %= len(LETTERS)

            if symbol.isupper():
                translated.append(LETTERS[letter_index])
            else:
                translated.append(LETTERS[letter_index].lower())

            key_index += 1
            if key_index == len(key):
                key_index = 0

    return ''.join(translated)


if __name__ == '__main__':
    main()
