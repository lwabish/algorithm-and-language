from typing import List
tcs = [
    (3,),
    (4,),
    (76,),
    (0,),
]


class Solution:
    def ten_2_three(self, n):
        init = n
        res = list()
        while init > 0:
            res.append(str(init % 3))
            init = init // 3
        return ''.join(res[::-1])

    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        three = self.ten_2_three(n)
        if three[0] != '1':
            return False
        if three[1:] != '0'*(len(three)-1):
            return False
        return True


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.isPowerOfThree(*tc))
