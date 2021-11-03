from typing import List
tcs = [
    (2334, ),
]


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        回文数字
        未考虑溢出，无效做法
        """
        ori_num = x   # 和列表的区别，列表赋值后动一个都会变，因为操作的是列表，指针没变；但是整数、字符串不会，因为改变了指针。
        if x < 0:
            # print('负数')
            return False
        if x % 10 == 0:
            # print('尾数为0')
            return False
        l = len(str(x))
        nums = list()
        for t in range(l, 0, -1):
            nums.append(x // (10 ** (t - 1)))
            x = x % (10 ** (t - 1))
        new_num = 0
        index = 0
        for t in nums:
            n = t * (10 ** index)
            new_num += n
            index += 1
        if ori_num == new_num:
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.isPalindrome(*tc))
