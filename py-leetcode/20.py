from typing import List
tcs = [
    ("()[]{}",),
    ("([)]",),
    ("]",),
]


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        for brace in s:
            # 左括号，直接入栈
            if brace in mapping.values():
                stack.append(brace)
            elif stack and stack[-1] == mapping[brace]:
                # 注意[][-1]会越界，要加上判断条件限制
                # 右括号，且能和左括号配对
                stack.pop()
            else:
                # 右括号且出现不配对的左括号
                return False
        # 剩一种情况：左括号多于右括号
        return not stack


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.isValid(*tc))
