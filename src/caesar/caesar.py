import sys

def get_letter(mode: str, alphabet: str, letter: str, shift: int) -> str:
    pos = alphabet.index(letter)
    if mode == 'encode':
        shifted = pos + shift
    else:
        shifted = pos - shift
    new_pos = shifted % len(alphabet)
    return alphabet[new_pos]

def cipher(mode: str, phrase: str, shift: int) -> None:
    lowercase_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    symbols = ' !@#$%^&*()_+-=[]\{\}|:;\'"<>,.?/~1234567890'

    new_phrase = ''
    for letter in phrase:
        if letter in lowercase_alphabet:
            new_phrase += get_letter(mode, lowercase_alphabet, letter, shift)
        elif letter in uppercase_alphabet:
            new_phrase += get_letter(mode, uppercase_alphabet, letter, shift)
        elif letter in symbols:
            new_phrase += letter
        else:
            raise ValueError("The script does not support your language yet.")

    print(new_phrase)

if __name__ == "__main__":
    if len(sys.argv) == 4:
        cipher(sys.argv[1], sys.argv[2], int(sys.argv[3]))
    else:
        raise Exception('Wrong number of arguments!')