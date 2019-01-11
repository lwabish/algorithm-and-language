num1 = 12345678123456781234567812345678
num2 = -1234567812345678123456781234567
num3 = 99999999999999999999999999999999


def rev(x):
    if x > 0:
        new_num = int(str(x)[::-1])
    else:
        new_num = -1 * int(str(x * (-1))[::-1])
    limit = 2**31
    if new_num > (limit - 1) or new_num < (-1 * limit):
        return 0
    else:
        return new_num


if __name__ == '__main__':
    print(rev(num1))
    print(rev(num2))
    print(rev(num3))
