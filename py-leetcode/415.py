from typing import List
tcs = [
    ("456", "77"),
    ("0", "0"),
    ("", ""),
]


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """
        字符串相加
        按位做乘法，最后累加即可
        """
        result = 0
        n = len(num1) if len(num1) > len(num2)else len(num2)
        for i in range(n):
            if i < len(num1):
                result += int(num1[i])*pow(10, len(num1)-1-i)
            if i < len(num2):
                result += int(num2[i])*pow(10, len(num2)-1-i)
        return str(result)


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.addStrings(*tc))
