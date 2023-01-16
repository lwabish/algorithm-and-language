SINGLE_NUM = [str(x) for x in range(10)]
E = ('e', 'E')
SIGNS = ('-', '+')
POINT = ('.',)

# 正例
tc = '+456.7e89'
tc = '+100'
tc = '5e2'
tc = '-123'
tc = '3.4'
tc = '-1E-14'
tc = '.1e3'
tc = '2.'

# 负例
tc = '12e'
tc = '1a3.14'
tc = '+-5'
tc = '12e+4.5'
tc = 'e2'
tc = '3+3'
tc = '3.3.3'
tc = '.'  # 这个算数字0嘛？？？
tc = '.e3'
tc = ''


def main(string):
    if not string:
        return False
    index = 0
    e_left_point = False
    e_flag = False
    while index < len(string):
        this_char = string[index]
        if this_char in SIGNS:
            # 不在第一位的正负号,只有一种情况是合理的：左边有e。其他情况一律false
            if index and string[index - 1] not in E:
                return False
        elif this_char in POINT:
            if e_flag:  # e后面不能出现.
                return False
            if e_left_point:  # 不能出现两次.
                return False
            else:
                e_left_point = True
        elif this_char in E:
            if e_flag:
                return False
            else:
                e_flag = True
            if index == len(string)-1 or index == 0:   # 首尾的e
                return False
            if index:
                if string[index - 1] not in SINGLE_NUM:
                    return False
        elif this_char not in SINGLE_NUM:
            return False

        index += 1
    return True


if __name__ == '__main__':
    print(main(tc))
