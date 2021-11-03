from typing import List
tcs = [
    (12345678123456781234567812345678,),
    (-1234567812345678123456781234567,),
    (99999999999999999999999999999999,),

]


class Solution:
    def reverse(self, x: int) -> int:
        """
        整数反转
        字符串反转，没有意义的解法
        由于python没有整数溢出的问题，用其他有严格限制数据类型长度的语言做比较方便理解
        """
        if x > 0:
            new_num = int(str(x)[::-1])
        else:
            new_num = -1 * int(str(x * (-1))[::-1])
        limit = 2**31
        if new_num > (limit - 1) or new_num < (-1 * limit):
            return 0
        else:
            return new_num


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.reverse(*tc))
