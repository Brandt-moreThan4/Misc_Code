import random as rd
import sys
import transpositionCipher as tc


def test_bunch():
    """Use this to test the encrypt and decrypt functions"""
    rd.seed(42)

    for i in range(20):
        # Random list of letters to test
        message = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ" * rd.randint(3, 20))
        rd.shuffle(message)
        message = ''.join(message)
        print(f'Test #{i + 1}: {message}')

        # Test with all the possible keys
        for key in range(1, len(message)):
            encrypted = tc.encrypt_message(message, key)
            decrypted = tc.decrypt_message(encrypted, key)

            if message != decrypted:
                print(f'Problem with test number {i} key: {key}')
                sys.exit()

    print('Done with testing')


if __name__ == '__main__':
    test_bunch()
