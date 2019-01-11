tc = '(])'
# tc = '{[[[[[[[]]]]}]]]'
# tc = '[{[}{}}]'


def main(s):
    left_braces = []
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    for t in s:
        if t in ('{', '[', '('):    # 此处可以改进，直接in pairs就可以，默认比对字典的key
            left_braces.append(t)
            continue
        try:
            if pairs[t] == left_braces[-1]:
                left_braces.pop()
            else:
                return False
        except IndexError:  # 没有左括号，先出现右括号
            if s != '':
                return False
            else:           # 空串
                return True
    if len(left_braces) > 0:
        return False
    else:
        return True


if __name__ == '__main__':
    print(main(tc))
