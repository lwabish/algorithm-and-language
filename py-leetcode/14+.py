from typing import List
tcs = [
    (["flower", "flow", "flight"],),
    (["dog", "racecar", "car"],),
]


class Solution:
    """
    最长公共前缀
    任取一个作为测试目标
    对于其他每一个词，都要对测试目标进行逐个字符的修剪
    直到遍历完，修剪最后留下的测试目标就是结果
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        test_target = strs[0]
        for str in strs:
            while not str.startswith(test_target):
                test_target = test_target[:len(test_target)-1]
        return test_target


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.longestCommonPrefix(*tc))
