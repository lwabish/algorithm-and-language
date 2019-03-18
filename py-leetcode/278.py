from typing import List
tcs = [
    (5,),
]


# 假定4是第一个坏的版本
def isBadVersion(version):
    if version >= 1:
        return True
    else:
        return False


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def half_search(start, end):
            mid_i = int((start + end) / 2)
            if isBadVersion(mid_i):
                if not isBadVersion(mid_i - 1):
                    return mid_i
                else:
                    return half_search(start, mid_i - 1)
            else:
                if isBadVersion(mid_i + 1):
                    return mid_i + 1
                else:
                    return half_search(mid_i+1, end)
        return half_search(1, n)


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.firstBadVersion(*tc))
