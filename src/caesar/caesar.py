import sys

def get_letter(alphabet: str, letter: str, shift: int) -> str:
    pos = alphabet.index(letter)
    shifted = pos + shift
    new_pos = shifted % len(alphabet)
    return alphabet[new_pos]

def cipher(phrase: str, shift: int) -> None:
    lowercase_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #symbols = ' !@#$%^&*()_+-=[]\{\}|:;\'"<>,.?/~1234567890'

    new_phrase = ''
    for letter in phrase:
        if letter in lowercase_alphabet:
            new_phrase += get_letter(lowercase_alphabet, letter, shift)
        elif letter in uppercase_alphabet:
            new_phrase += get_letter(uppercase_alphabet, letter, shift)
        elif letter.isalpha() == False:
            new_phrase += letter
        else:
            raise ValueError("The script does not support your language yet.")

    return new_phrase

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