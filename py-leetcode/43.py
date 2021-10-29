from typing import List
tcs = [
    ("123", "456"),
]


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        字符串相乘
        和字符串相加同样的思路，按位分别乘最后加总
        """
        result = 0
        for i, v in enumerate(num2):
            for j, w in enumerate(num1):
                result += int(v)*pow(10, len(num2)-1-i) * \
                    int(w)*pow(10, len(num1)-j-1)
        return str(result)


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.multiply(*tc))
