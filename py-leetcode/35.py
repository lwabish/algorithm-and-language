nums = [1, 3, 5, 6]
target = 4
nums = [1, 3, 5, 6]
target = 5
target = 15


def main(nums, target):
    if target in nums:
        return nums.index(target)
    elif target < nums[0]:
        return 0
    elif target > nums[-1]:
        return len(nums)
    for t in range(len(nums)):
        if nums[t] < target and nums[t + 1] > target:
            return t+1


if __name__ == '__main__':
    print(main(nums, target))
