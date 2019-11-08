from typing import List
tcs = [
    ("abcabcbb",),
    ("abcabcbbcrstwvu",)
]


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 初始化
        # 窗口
        window_content = list()
        # 记录最大值
        max_length = 0

        for letter in s:
            # 处理已经存在的元素，一直向右移动窗口，直到该字母不存在
            while letter in window_content:
                window_content.pop(0)
            # 新字母
            window_content.append(letter)
            max_length = max(len(window_content), max_length)

        return max_length


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.lengthOfLongestSubstring(*tc))
