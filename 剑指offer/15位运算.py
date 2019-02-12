"""
&
|
^
~
<< 
>>
"""
tc = 78


# 左移1，逐位做与运算，结果为1则计数加一
# 这种方法循环次数是n的位数
def main(n):
    count = 0
    flag = 1
    for _ in range(len(str(bin(n))[2:])):
        print(bin(flag), bin(n & flag))
        if n & flag:
            count += 1
        flag = flag << 1
    return count


# 巧妙的方法：依次把一个二进制数的最后一位反转成0，直到所有位都变成零。
# 反转操作的次数就是1的个数。
# 具体反转的方法是：将n-1，与原来的n做与操作
def main2(n):
    count = 0
    while (n):
        n = (n - 1) & n
        print(bin(n))
        count += 1
    return count


if __name__ == '__main__':
    print(main(tc))
    print(main2(tc))
