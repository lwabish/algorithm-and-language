# n>1,切成的段数>1
tc_n = 10


# 动态规划
def main(n):
    # f2=1+1,f3=2+1。加1是因为f2 f3作为子问题时，可以一刀不剪。
    sub_max = list([0, 1, 2, 3])
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2

    def count_sub_max(x):
        max_product = 0
        for i in range(1, int(x / 2)+1):
            if sub_max[i] * sub_max[x - i] > max_product:
                max_product = sub_max[i] * sub_max[x - i]
        return max_product

    for t in range(4, n+1):
        sub_max.append(count_sub_max(t))
    print(sub_max)
    return sub_max[-1]


# 贪心算法:3米的子长度是最佳长度，多剪。剩下的小段，多剪2
def main2(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2

    if n % 3 == 0:
        return 3**(n//3)
    elif n % 3 == 1:
        return 4*3**(n//3-1)
    else:
        return 2*3**(n//3)


if __name__ == '__main__':
    print(main(tc_n))
    print(main2(tc_n))
