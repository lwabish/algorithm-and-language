tc = '(])'
# tc = '{[[[[[[[]]]]}]]]'
# tc = '[{[}{}}]'


def main(s):
    count_left, count_right = 0, 0
    left_braces = []
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    for t in s:
        if t in ('{', '[', '('):    # 此处可以改进，直接in pairs就可以，默认比对字典的key
            count_left += 1
            left_braces.append(t)
            continue
        if t in (')', '}', ']'):
            count_right += 1
        try:
            if pairs[t] == left_braces[-1]:
                left_braces.pop()
        except IndexError:  # 没有左括号，先出现右括号
            if s != '':
                return False
            else:           # 空串
                return True
    if count_left != count_right:
        return False
    if len(left_braces) > 0:
        return False
    else:
        return True


if __name__ == '__main__':
    print(main(tc))
