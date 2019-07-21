from typing import List
from string import digits
tcs = [
    (list(digits),),
]


class Solution:

    def __init__(self, nums: List[int]):
        self.ori_nums = nums
        self.to_shuffle = list(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.ori_nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        # 时间复杂度on2
        import random
        result = list()
        while self.to_shuffle:
            rd_index = random.randint(0, len(self.to_shuffle)-1)
            result.append(self.to_shuffle.pop(rd_index))
        return result
        # 时间复杂度on
        # 遍历一遍，从当前指针到尾巴中随机选一个交换位置即可


if __name__ == '__main__':
    for tc in tcs:
        s = Solution(*tc)
        print(s.reset())
        print(s.shuffle())
