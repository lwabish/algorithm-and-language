import sys
import math

n = sys.stdin.readline().strip()
nums = sys.stdin.readline().strip().split()

nums = set(nums)


def count_select(n, m):
    return math.factorial(n)/(math.factorial(m)*math.factorial(n-m))


total = 0
for i in range(2, len(nums)+1):
    total += count_select(len(nums), i)
print(int(total))
