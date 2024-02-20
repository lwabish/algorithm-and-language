from typing import List
tcs = [
    ([[1, 3], [2, 6], [8, 10], [15, 18]],),
]


# 排序的应用
# 实现很简单，思路不容易想到
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for i in intervals[1:]:
            tail = result[-1]
            if i[0] > tail[1]:
                result.append(i)
            else:
                result[-1][1] = max(tail[1], i[1])
        return result


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.merge(*tc))
