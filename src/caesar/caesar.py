import sys

LOWERCASE_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_letter(alphabet: str, letter: str, shift: int) -> str:
    pos = alphabet.index(letter)
    shifted = pos + shift
    new_pos = shifted % len(alphabet)
    return alphabet[new_pos]

def cipher(phrase: str, shift: int) -> str:

    new_phrase = list()
    for letter in phrase:
        if letter in LOWERCASE_ALPHABET:
            new_phrase.append(get_letter(LOWERCASE_ALPHABET, letter, shift))
        elif letter in UPPERCASE_ALPHABET:
            new_phrase.append(get_letter(UPPERCASE_ALPHABET, letter, shift))
        elif not letter.isalpha():
            new_phrase.append(letter)
        else:
            raise ValueError("The script does not support your language yet.")

    return ''.join(new_phrase)

if __name__ == "__main__":
    if len(sys.argv) == 4:
        mode = sys.argv[1]
        phrase = sys.argv[2]
        shift = int(sys.argv[3])

        if mode == 'decode':
            shift *= -1

        result = cipher(phrase, shift)
        print(result)
    else:
        raise IndexError('Wrong number of arguments!')