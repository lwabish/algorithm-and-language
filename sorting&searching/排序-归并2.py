from typing import List
tcs = [
    ([-1, 2, 5, 0, 9, 4],),
]


# 先切分，再合并
class Solution:
    def mergeSort(self, nums: List):
        if len(nums) < 2:
            return nums
        # 负责切分
        priv = int(len(nums)/2)
        left = self.mergeSort(nums[:priv])
        right = self.mergeSort(nums[priv:])
        return self.merge(left, right)

    # 负责合并成有序数组
    # n1和n2都是内部有序的
    def merge(self, n1: List, n2: List):
        res = []
        while n1 or n2:
            c1 = c2 = float("inf")
            if n1:
                c1 = n1[0]
            if n2:
                c2 = n2[0]
            if c1 > c2:
                res.append(c2)
                n2.pop(0)
            else:
                res.append(c1)
                n1.pop(0)
        return res


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.mergeSort(*tc))
