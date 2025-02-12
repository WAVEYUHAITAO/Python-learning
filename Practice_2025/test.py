import random

def generate_code(len = 4):
    all_chars='01234567abcdefgABCDEFG'
    for i in range(len):
        yield random.choice(all_chars)
if __name__ == '__main__':
    for code in generate_code():
        print(code, end='')