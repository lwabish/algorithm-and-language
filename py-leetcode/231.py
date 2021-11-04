from typing import List
tcs = [
    (),
]


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        是否是2的幂
        位运算
        n & (n-1) 可以消掉n二进制表示的最后一位1
        2的幂 在二进制表示时，形如 10 100 10000 100000 ....
        因此 10 & 01 = 00   100 & 011 = 000 .....
        """
        return n > 0 and (n & (n - 1)) == 0


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.isPowerOfTwo(*tc))
