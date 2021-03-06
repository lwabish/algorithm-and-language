tc = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
]


# 矿泉水一元一瓶，两个矿泉水瓶可以换一瓶水。
# 给n元，可以喝多少瓶水
def main(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        # 偶数元钱很简单：喝完当前所有瓶数后，直接递归一半的瓶子数
        return n + main(int(n / 2))
    else:
        # 奇数元钱在比它小一的基础上，其实是多喝了多出来的一瓶以及和偶数情况下最后剩的一瓶又配对所以又多喝了一瓶。所以奇数元钱直接在上一个偶数元钱的基础上加2即可。
        return main(n-1)+2


if __name__ == '__main__':
    for i in tc:
        print(main(i))
