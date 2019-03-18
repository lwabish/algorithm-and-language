from typing import List

tcs = [
    ("leetcode",),
    ("loveleetcode",),
    ('',),
]


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        statics = dict()
        for i in range(len(s)):
            if s[i] not in statics:
                statics[s[i]] = i
            elif statics[s[i]] != len(s):
                statics[s[i]] = len(s)
        min_i = min(statics.values())
        return min_i if min_i < len(s) else -1


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.firstUniqChar(*tc))
