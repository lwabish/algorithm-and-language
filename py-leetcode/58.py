tc = 'Hello World'
tc = ''
tc = ' '
# tc = 'a  '


def main(s):
    words = s.split(' ')
    word = ''
    index = -1
    while not word:
        try:
            word = words[index]
        except IndexError:
            return 0
        index -= 1
    return len(word)


if __name__ == '__main__':
    print(main(tc))
