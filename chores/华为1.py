import sys
import string

LEGAL_CHARS = string.ascii_letters+string.digits


def check_string(s):
    for t in s:
        if t not in LEGAL_CHARS:
            return False
    return True


def main():
    legal_words = list()
    ilegal_words = list()
    while True:
        s = sys.stdin.readline().strip()
        if not s:
            break
        if check_string(s):
            if s not in legal_words:
                legal_words.append(s)
        else:
            ilegal_words.append(s)
    print(' '.join(legal_words))
    print(' '.join(ilegal_words))


if __name__ == '__main__':
    main()
