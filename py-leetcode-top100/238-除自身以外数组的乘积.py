from typing import List
tcs = [
    ([1, 2, 3, 4],),
]


# 有点像42接雨水 53最大子数组和
# 问题转化：除自身的乘积=左边乘积*右边乘积
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProduct, rightProduct = [1], [1]
        n = len(nums)
        for k, e in enumerate(nums[:n-1]):
            leftProduct.append(leftProduct[k]*e)
        for k, e in enumerate(nums[::-1][:n-1]):
            rightProduct.append(rightProduct[k]*e)
        rightProduct.reverse()
        return [leftProduct[i]*rightProduct[i] for i in range(n)]


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.productExceptSelf(*tc))
