# 将空格替换成%20
# O(n)复杂度
tc = 'We Are Happy!'


def main(sentence):
    # 先查找空格个数
    c = sentence.count(' ')
    # 计算替换完成后字符串的新长度
    new_length = len(sentence) + c * 2
    # 按新长度申请字符串空间
    result = sentence + '*' * (new_length - len(sentence))
    # 设置指针，p1用来遍历原字符串，p2用来指示新字符串的改写位置
    p1 = len(sentence) - 1
    p2 = len(result) - 1
    # 将result转换成列表，string不能直接修改
    result = list(result)
    while p1 >= 0:
        if sentence[p1] != ' ':
            result[p2] = sentence[p1]
            p1 -= 1
            p2 -= 1
        else:
            result[p2] = '0'
            p2 -= 1
            result[p2] = '2'
            p2 -= 1
            result[p2] = '%'
            p2 -= 1
            p1 -= 1
        print(result)
    return ''.join(result)


if __name__ == '__main__':
    print(main(tc))
