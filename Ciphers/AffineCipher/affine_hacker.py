import affine_cipher
import ciphy


def main():
    encrypted_message = """U&'<3dJ^Gjx'-3^MS'Sj0jxuj'G3'%j'<mMMjS'g{GjMMg9j{G'g"'gG'<3^MS'Sj<jguj'm'P^dm{'g{G3'%jMgjug
    {9'GPmG'gG'-m0'P^dm{LU'5&Mm{'_^xg{9"""

    decrypted_message = hack_affine(encrypted_message)
    if decrypted_message:
        print(f'The decrypted message is:\n{decrypted_message}')
    else:
        print('Sorry, I was not able to decrypt the message.')


def hack_affine(encrypted_message):
    """Use brute force to hack"""
    print('Hacking!\n Press Control + C to quit')
    for key in range(len(affine_cipher.SYMBOLS) ** 2):
        if key % 100 == 0:
            print(f"Attmepting with Key: {key}")
        keyA = affine_cipher.get_key_parts(key)[0]
        if ciphy.gcd(keyA, len(affine_cipher.SYMBOLS)) != 1:
            # Only a keyA that is relatively prime with symbol length would have been used.
            continue

        decrypted_text = affine_cipher.decrypt_message(encrypted_message, key)

        if ciphy.is_english(decrypted_text):
            print(f"Hey This seems like it's English so it's probably the right message!")
            return decrypted_text

    return None


if __name__ == '__main__':
    main()
