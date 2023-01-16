tc = [3, 4]
tc = [0, -2]
tc = [0, 0]
tc = [0, 3]
tc = [3, 0]
tc = [3, -2]
tc = [-3, -2]
tc = [3, 10]
tc = [2, 1]
tc = [2, -1]
tc = [2, 2]


# 功能性：如何高效实现乘方？在之前斐波那契数列实现过，用二分的思想做乘方。
def main(a, x):
    # 特殊值判断：a=0
    if a == 0:
        if x < 0:
            raise ZeroDivisionError('0的负幂非法')
        return 0  # 0的0次幂没意义，可以随意返回0或1，所以也合并在这种情况

    # 特殊值判断：x为0或负数
    if x == 0:
        return 1
    elif x > 0:
        abs_x = x
    elif x < 0:
        abs_x = -x
    # 递归的基线条件
    if x == 1:
        return a
    elif x == 2:
        return a * a

    #  递归调用
    result = main(main(a, int(abs_x/2)), 2)

    # 奇数次幂多乘一次a
    if x % 2 == 1:
        result *= a

    # 负数次幂返回倒数
    if x < 0:
        result = 1 / result

    return result


if __name__ == '__main__':
    print(main(tc[0], tc[1]))
