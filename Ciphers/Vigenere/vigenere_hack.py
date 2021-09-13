import itertools
import re

import vigenere_cipher
import freq_analysis
import ciphy

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SILENT_MODE = False  # if set to True, program doesn't print attempts
NUM_MOST_FREQ_LETTERS = 4  # attempts this many letters per subkey
MAX_KEY_LENGTH = 16  # will not attempt keys longer than this
NONLETTERS_PATTERN = re.compile('[^A-Z]')


def main():
    ciphertext = """Adiz Avtzqeci Tmzubb wsa m Pmilqev halpqavtakuoi, lgouqdaf, kdmktsvmztsl, izr xoexghzr kkusitaaf. 
    Vz wsa twbhdg ubalmmzhdad qz hce vmhsgohuqbo ox kaakulmd gxiwvos, krgdurdny i rcmmstugvtawz ca tzm ocicwxfg jf 
    "stscmilpy" oid "uwydptsbuci" wabt hce Lcdwig eiovdnw. Bgfdny qe kddwtk qjnkqpsmev ba pz tzm roohwz at xoexghzr 
    kkusicw izr vrlqrwxist uboedtuuznum. Pimifo Icmlv Emf DI, Lcdwig owdyzd xwd hce Ywhsmnemzh Xovm mby Cqxtsm Supacg
     (GUKE) oo Bdmfqclwg Bomk, Tzuhvif'a ocyetzqofifo ositjm. Rcm a lqys ce oie vzav wr Vpt 8, lpq gzclqab mekxabnittq 
     tjr Ymdavn fihog cjgbhvnstkgds. Zm psqikmp o iuejqf jf lmoviiicqg aoj jdsvkavs Uzreiz qdpzmdg, dnutgrdny bts 
     helpar jf lpq pjmtm, mb zlwkffjmwktoiiuix avczqzs ohsb ocplv nuby swbfwigk naf ohw Mzwbms umqcifm. Mtoej bts 
     raj pq kjrcmp oo tzm Zooigvmz Khqauqvl Dincmalwdm, rhwzq vz cjmmhzd gvq ca tzm rwmsl lqgdgfa rcm a kbafzd-hzaumae 
     kaakulmd, hce SKQ. Wi 1948 Tmzubb jgqzsy Msf Zsrmsv'e Qjmhcfwig Dincmalwdm vt Eizqcekbqf Pnadqfnilg, ivzrw pq 
     onsaafsy if bts yenmxckmwvf ca tzm Yoiczmehzr uwydptwze oid tmoohe avfsmekbqr dn eifvzmsbuqvl tqazjgq. Pq kmolm 
     m dvpwz ab ohw ktshiuix pvsaa at hojxtcbefmewn, afl bfzdakfsy okkuzgalqzu xhwuuqvl jmmqoigve gpcz ie hce
      Tmxcpsgd-Lvvbgbubnkq zqoxtawz, kciup isme xqdgo otaqfqev qz hce 1960k. Bgfdny'a tchokmjivlabk fzsmtfsy if
       i ofdmavmz krgaqqptawz wi 1952, wzmz vjmgaqlpad iohn wwzq goidt uzgeyix wi tzm Gbdtwl Wwigvwy. Vz aukqdoev
        bdsvtemzh rilp rshadm tcmmgvqg (xhwuuqvl uiehmalqab) vs sv mzoejvmhdvw ba dmikwz. Hpravs rdev qz 1954,
         xpsl whsm tow iszkk jqtjrw pug 42id tqdhcdsg, rfjm ugmbddw xawnofqzu. Vn avcizsl lqhzreqzsy tzif vds
          vmmhc wsa eidcalq; vds ewfvzr svp gjmw wfvzrk jqzdenmp vds vmmhc wsa mqxivmzhvl. Gv 10 Esktwunsm 2009,
           fgtxcrifo mb Dnlmdbzt uiydviyv, Nfdtaat Dmiem Ywiikbqf Bojlab Wrgez avdw iz cafakuog pmjxwx ahwxcby gv 
           nscadn at ohw Jdwoikp scqejvysit xwd "hce sxboglavs kvy zm ion tjmmhzd." Sa at Haq 2012 i bfdvsbq azmtmd'g 
           widt ion bwnafz tzm Tcpsw wr Zjrva ivdcz eaigd yzmbo Tmzubb a kbmhptgzk dvrvwz wa efiohzd."""

    hacked_message = hack_vigenere(ciphertext)

    if hacked_message:
        print(f'The decrypted message is:\n{hacked_message}')
    else:
        print("LOL, you couldn't hack it!!")


def find_repeat_sequences_spacing(message):
    """Try to find any 3,4 or 5 letter sequences that are repeated. Return a dict with keys as the sequences
    and values as list of spacings (number of letters between the repeats)"""

    # Remove non-letters
    message = NONLETTERS_PATTERN.sub('', message.upper())

    seq_spacings = {}
    for seq_length in range(3, 6):
        for seq_start in range(len(message) - seq_length):
            seq = message[seq_start: seq_start + seq_length]

            for i in range(seq_start + seq_length, len(message) - seq_length):
                if message[i:i + seq_length] == seq:
                    if seq not in seq_spacings:
                        seq_spacings[seq] = []

                    seq_spacings[seq].append(i - seq_start)

    return seq_spacings


def get_useful_factors(number):
    """Returns a list of useful factors of number. "Useful" meaning factors less than MAX_KEY_LENGTH + 1. """

    factors = []

    if number < 2:
        return factors  # numbers less than 2 have no useful factors

    for i in range(2, MAX_KEY_LENGTH + 1):
        if number % i == 0:
            factors.append(i)
            factors.append(int(number / i))

    if 1 in factors:
        factors.remove(1)

    return list(set(factors))


def get_item_at_index_one(x):
    return x[1]


def get_most_common_factors(seq_factors):
    factor_counts = {}

    for seq in seq_factors:
        factor_list = seq_factors[seq]
        for factor in factor_list:
            if factor not in factor_counts:
                factor_counts[factor] = 0
            factor_counts[factor] += 1

    factors_by_count = []
    for factor in factor_counts:
        if factor <= MAX_KEY_LENGTH:
            factors_by_count.append((factor, factor_counts[factor]))

    factors_by_count.sort(key=get_item_at_index_one, reverse=True)

    return factors_by_count


def kasiski_examination(cipher_text):
    """Find sequences of factors that occur multiple times."""

    repeated_seq_spacings = find_repeat_sequences_spacing(cipher_text)

    seq_factors = {}
    for seq in repeated_seq_spacings:
        seq_factors[seq] = []
        for spacing in repeated_seq_spacings[seq]:
            seq_factors[seq].extend(get_useful_factors(spacing))

    factors_by_count = get_most_common_factors(seq_factors)

    all_likely_key_lengths = []
    for two_int_tuple in factors_by_count:
        all_likely_key_lengths.append(two_int_tuple[0])

    return all_likely_key_lengths


def get_nth_subkeys_letters(n, key_length, message):
    message = NONLETTERS_PATTERN.sub('', message)

    i = n - 1
    letters = []
    while i < len(message):
        letters.append(message[i])
        i += key_length
    return ''.join(letters)


def attempt_hack_with_key(cipher_text, most_likely_key_length):
    cipher_text_up = cipher_text.upper()

    all_freq_scores = []
    for nth in range(1, most_likely_key_length + 1):
        nth_letters = get_nth_subkeys_letters(nth, most_likely_key_length, cipher_text_up)

        freq_scores = []
        for possible_key in LETTERS:
            decrypted_text = vigenere_cipher.translate_message(nth_letters, possible_key, 'decrypt')
            key_and_freq_match_tuple = (possible_key, freq_analysis.english_freq_match_score(decrypted_text))
            freq_scores.append(key_and_freq_match_tuple)

        freq_scores.sort(key=get_item_at_index_one, reverse=True)
        all_freq_scores.append(freq_scores[:NUM_MOST_FREQ_LETTERS])

    for indexes in itertools.product(range(NUM_MOST_FREQ_LETTERS), repeat=most_likely_key_length):
        possible_key = ''
        for i in range(most_likely_key_length):
            possible_key += all_freq_scores[i][indexes[i]][0]

        decrypted_text = vigenere_cipher.translate_message(cipher_text_up, possible_key, 'decrypt')

        if ciphy.is_english(decrypted_text):
            original_case = []
            for i in range(len(cipher_text)):
                if cipher_text[i].isupper():
                    original_case.append(decrypted_text[i].upper())
                else:
                    original_case.append(decrypted_text[i].lower())

            decrypted_text = ''.join(original_case)

            print(f'Possible hack on key: {possible_key}')
            print(f'Text:\n{decrypted_text[:200]}')
            print(f'Enter D for done, or press Enter to keep trying:')
            response = input('>')
            if response.strip().upper().startswith('D'):
                return decrypted_text

    return None


def hack_vigenere(cipher_text):
    all_likely_key_lengthsis = kaski_examination(cipher_text)

    for key_length in all_likely_key_lengths:
        hacked_message = attempt_hack_with_key(cipher_text, key_length)
        if hacked_message is not None:
            break

    return hacked_message


if __name__ == '__main__':
    main()