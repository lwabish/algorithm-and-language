tc = 8888


# 牛顿迭代法？
def main2(x):
    if x <= 1:
        return x
    r = x
    while r > x / r:
        r = (r + x / r) // 2
    return int(r)


# 二分法，int最大开根号也就46340.9，从0~46340之间找到n，n的平方小于x，n+1的平方大于x，就好
def main1(x):
    low, high = 0, 46340
    while low < high:
        mid_ = int((low + high) / 2)
        pow_ = mid_**2
        if pow_ < x and (mid_+1)**2 < x:
            low = mid_+1
        elif pow_ > x and (mid_+1)**2 > x:
            high = mid_-1
        elif pow_ < x and (mid_ + 1) ** 2 > x:
            return mid_


# 不要脸用math库的方法
def main(x):
    import math
    return int(math.sqrt(x))


if __name__ == '__main__':
    print(main(tc))
    print(main1(tc))
