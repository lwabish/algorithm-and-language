class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = -1
        for t in range(1, len(nums)):
            if index == -1:
                if nums[t] == nums[t-1]:
                    index = t
            else:
                if nums[t] != nums[t-1]:
                    nums[index] = nums[t]
                    index += 1
        if index == -1:
            return len(nums)
        return index
