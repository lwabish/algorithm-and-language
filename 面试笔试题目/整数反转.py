def reverse(x):
    if x >= 0:
        r = int(str(x)[::-1])
    else:
        r = -int(str(x)[:0:-1])

    if -2 ** 31 < r < 2 ** 31 - 1:
        return r
    else:
        return 0


while True:
    s = input()
    if s != '':
        print(reverse(s))
    else:
        break
