from typing import List
tcs = [
    # (28,),
    (-2147483648,),
    # (1,),
]


class Solution:
    def isUgly(self, num: int) -> bool:
        factors = list()

        def split_factor(num):
            num = abs(num)
            for n in range(2, num+1):
                if num % n == 0:
                    factors.append(n)
                    if n < num:
                        print(n)
                        split_factor(num//n)
                    break
        split_factor(num)
        print(factors)
        return not bool(set(factors) - set([2, 3, 5]))


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.isUgly(*tc))
