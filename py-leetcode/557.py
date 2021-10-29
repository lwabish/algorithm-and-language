from typing import List
tcs = [
    ("Let's take LeetCode contest",),
]


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        反转字符串中的单词
        """
        return " ".join(list(map(lambda s: s[::-1], s.split(" "))))


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.reverseWords(*tc))
