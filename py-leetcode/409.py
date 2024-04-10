from typing import List
tcs = [
    ("aaabbbcccd",),
]


# 最长回文字符串（不要求连续子串）
# 本质上就是凑对儿
# 最后考虑中间如果有单蹦的就加1，否则就不加
class Solution:
    def longestPalindrome(self, s: str) -> int:
        tmp = set()
        ans = 0
        for t in s:
            if t in tmp:
                ans += 2
                tmp.remove(t)
                continue
            tmp.add(t)
        return ans if len(tmp) == 0 else ans + 1


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.longestPalindrome(*tc))
