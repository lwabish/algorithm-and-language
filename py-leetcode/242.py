from typing import List
from collections import Counter
tcs = [
    ("anagram", "nagaram",),
]


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.isAnagram(*tc))
