tc = [0]


def main(digits):
    d = len(digits)
    number = 0
    for t in digits:
        number += t * 10 ** (d - 1)
        d -= 1
    number += 1
    return [int(i) for i in str(number)]


if __name__ == '__main__':
    print(main(tc))
