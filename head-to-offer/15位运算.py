# 该题在python中需要注意：python的负数表示与其他语音不一样。python中的负数二进制用负号加绝对值的二进制表示，所以用方法1会发现，正数负数的结果是一样的。用方法2会死循环，n = (n - 1) & n这种反转末位0的算法失效，负数的位数为无限扩张。
# 解决方法之一是：引入一个函数，将二进制转换回32位表示法
from my_data_structure import int_to_bin32
"""
&
|
^
~
<< 
>>
"""
tc = 78
tc = 1
tc = -1
tc = -78


# 左移1，逐位做与运算，结果为1则计数加一
# 这种方法循环次数是n的位数


def main(n):
    count = 0
    flag = 1
    n = int_to_bin32(n)
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
        n = int_to_bin32(n)
        n = (n - 1) & n
        print(bin(n))
        count += 1
    return count


if __name__ == '__main__':
    print(main(tc))
    print(main2(tc))
