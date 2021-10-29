from typing import List
tcs = [
    ([1, 2, 3, 4],),
]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        除自身以外数组的乘积
        遍历一遍，构造出遍历点左侧和右侧的累计乘积，左侧*右侧即为遍历点的结果
        """
        L, R = [1], [1]
        for i, v in enumerate(nums):
            if i > 0:
                L.append(L[i-1]*nums[i-1])
            if len(nums)-1-i < len(nums)-1:
                R.append(R[i-1]*nums[len(nums)-i])
        # [1,1,2,6] [1,4,12,24] 对称位相乘
        # [24,12,8,6]
        # print(L, R)
        return list(map(lambda x: x[1]*R[len(nums)-1-x[0]], enumerate(L)))


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.productExceptSelf(*tc))
