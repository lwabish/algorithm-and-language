tc1 = '1111'
tc2 = '1111'


'''
python内置函数实现,bin()将十进制转2进制，返回字符串。int(111,2)也可以实现
'''


def main1(a, b):
    return bin(int(a, 2)+int(b, 2))[2:]


# 不用python内置函数实现


def main(a, b):
    shorter = b if len(a) > len(b) else a
    longer = a[::-1] if shorter == b else b[::-1]
    d = abs(len(a) - len(b))
    c = '0' * d + shorter
    c = c[::-1]
    plus_list = list([''] * len(c))+['']
    result = list()
    for index in range(len(c)):
        plus = 1 if plus_list[index] != '' else 0
        total = int(c[index])+int(longer[index])+plus
        if total in [0, 1]:
            result.append(str(total))
        elif total == 2:
            plus_list[index+1] = '1'
            result.append('0')
        elif total == 3:
            plus_list[index+1] = '1'
            result.append('1')
    if plus_list[-1] != '':
        result.append('1')
    result.reverse()
    # print(c, longer, plus_list, result)
    return ''.join(result)


if __name__ == '__main__':
    print(main(tc1, tc2))
    print(main1(tc1, tc2))
