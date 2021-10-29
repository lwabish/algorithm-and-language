from typing import List
tcs = [
    (["h", "e", "l", "l", "o"],),
    (["H", "a", "n", "n", "a", "h"],)
]


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        原地反转字符串数组
        利用python语法便利，比较容易
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        solution.reverseString(*tc)
        print(*tc)
