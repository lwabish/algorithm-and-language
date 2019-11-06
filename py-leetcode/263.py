from typing import List
import math
tcs = [
    (905391974,),
    (28,),
    (-2,),
    (1,),
    (0,),
]


class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        if num == 1:
            return True
        if num % 2 == 0:
            return self.isUgly(num//2)
        elif num % 3 == 0:
            return self.isUgly(num//3)
        elif num % 5 == 0:
            return self.isUgly(num//5)
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.isUgly(*tc))
