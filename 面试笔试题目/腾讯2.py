import sys
from collections import Counter


def main(nums):
    res = Counter(nums)
    return abs(res['1']-res['0'])


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    nums = sys.stdin.readline().strip()
    print(main(nums))
