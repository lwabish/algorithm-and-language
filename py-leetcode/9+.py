from typing import List
tcs = [
    # 偶数位，反转结束
    (1234, ),
    (1221, ),
    (1201, ),

    (12134, ),
    (12121, ),
    (12101, ),

    (0,),
]


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        回文数字
        参考官方题解，反转原整数
        但是不能完全反转，因为完全反转有可能导致溢出
        只需要反转到新整数不比剩余的整数小时即可(官方题解的描述反转一半不够严谨，因为half和x的大小和位数还有关系)
        此时可以判断出结论
        """
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        half = 0
        while half < x:
            half = half*10+x % 10
            x //= 10

        # 偶数位   or  奇数位
        return half == x or half//10 == x


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.isPalindrome(*tc))
