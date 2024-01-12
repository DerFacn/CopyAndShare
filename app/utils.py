from random import randint, choice

letters = "abcdefghijklmnopqrstuvwxyz"


def generate_code():
    code = ""
    for i in range(6):
        letter = choice(letters)
        if randint(0, 1) == 1:
            code += letter.upper()
        else:
            code += letter
    return code
