import sys
n = sys.stdin.readline().strip()


def count(nums):
    res = min(nums)
    nums = list(map(lambda x: x-res, nums))
    if nums[0] > 2*nums[1]:
        res += nums[1]
    elif nums[1] > 2*nums[0]:
        res += nums[0]
    else:
        res += int((nums[0]+nums[1])/3)
    return res


for i in range(int(n)):
    line = list(map(lambda x: int(x), sys.stdin.readline().strip().split()))
    print(count(line))
