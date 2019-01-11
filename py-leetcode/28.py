# tc = ''
haystack = "hello"
needle = "ll"


def main2(haystack, needle):
    if needle not in haystack:
        return - 1
    return haystack.index(needle)


def main(haystack, needle):
    if needle == '':
        return 0
    length = len(needle)
    for i in range(len(haystack)):
        # print(haystack[i:i+length])
        if haystack[i:i + length] == needle:
            return i
    return -1


if __name__ == '__main__':
    print(main(haystack, needle))
    print(main2(haystack, needle))
