from typing import List
tcs = [
    ("42",),
    ('',),
    ("   -42",),
    ("4193 with words",),
    ("words and 987",),
    ("-91283472332",),
]


class Solution:
    def myAtoi(self, str: str) -> int:
        def get_all_nums(s: str):
            """
            从第一位开始，直到第一个不是数字的字符。返回中间的数字
            """
            index = -1
            while index < len(s) - 1:
                if not s[index + 1].isdigit():
                    break
                index += 1
            if index == -1:
                return ''
            else:
                return s[:index+1]
        str = str.lstrip()
        res = 0
        if str:
            if str[0] == '+'or str[0] == '-':
                nums = get_all_nums(str[1:])
                if nums:
                    res = int(str[0]+nums)
            elif str[0].isdigit():
                nums = get_all_nums(str)
                if nums:
                    res = int(nums)
        if res > 2 ** 31 - 1:
            res = 2 ** 31 - 1
        elif res < -2 ** 31:
            res = -2 ** 31
        return res


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.myAtoi(*tc))
