from typing import List
from my_universal_operation import print_used_time


class Solution1:
    @print_used_time
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        def move_once(direction='right'):
            if direction == 'right':
                last_didit = nums[-1]
                for i in range(len(nums) - 1, 0, -1):
                    nums[i] = nums[i-1]
                nums[0] = last_didit
            elif direction == 'left':
                first_digit = nums[0]
                for i in range(len(nums) - 1):
                    nums[i] = nums[i + 1]
                nums[-1] = first_digit
        if k < int(len(nums) / 2):
            k = len(nums) - k
            for _ in range(k):
                move_once('left')
        else:
            for _ in range(k):
                move_once()


class Solution2:
    @print_used_time
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        while k > 0:
            a = nums.pop()
            nums.insert(0, a)
            k -= 1


class Solution3:
    @print_used_time
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        reverse(0, len(nums) - 1)
        reverse(0, k-1)
        reverse(k, len(nums) - 1)


if __name__ == '__main__':
    tc = [0]*10000+[1]*10000
    Solution1().rotate(tc, 5)

    tc = [0] * 10000 + [1] * 10000
    Solution2().rotate(tc, 5)

    tc = [0] * 10000 + [1] * 10000
    Solution3().rotate(tc, 5)
