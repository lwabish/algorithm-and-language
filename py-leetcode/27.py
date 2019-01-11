val = 2
tc = [0, 1, 2, 2, 3, 0, 4, 2]
tc = [3, 2, 2, 3]


def main(nums, val):
    count = 0
    for num in nums:
        if num == val:
            count += 1
    index = len(nums) - 1
    while index >= len(nums) - count:
        if nums[index] != val:
            for t in range(len(nums) - count):
                if nums[t] == val:
                    nums[index], nums[t] = nums[t], nums[index]
                    break
        index -= 1

    print(nums)
    return len(nums)-count


if __name__ == '__main__':
    print(main(tc, val))
