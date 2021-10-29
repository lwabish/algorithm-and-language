from typing import List
tcs = [
    ([2, 1, 1, 2],),
]


class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        """
        按照数组在坐标系上逆时针转，判断是否会相交
        枚举每一步的分类，归纳总结共有几种情况
        1和2比较容易
        3的条件归纳比较难：有几种情况看起来和3相似，但是其实可以归类到1、2中
                 i-2
    case 1 : i-1┌─┐
                └─┼─>i
                 i-3

                    i-2
    case 2 : i-1 ┌────┐
                 └─══>┘i-3
                 i  i-4      (i overlapped i-4)

    case 3 :    i-4
               ┌──┐ 
               │i<┼─┐
            i-3│ i-5│i-1
               └────┘
                i-2
        """
        if len(distance) < 4:
            return False
        for i, v in enumerate(distance):
            # case1
            if i >= 3 and distance[i-1] <= distance[i-3] and v >= distance[i-2]:
                return True
            # case2
            if i >= 4 and distance[i-1] == distance[i-3] and distance[i-4]+v == distance[i-2]:
                return True
            # case3
            if i >= 5 and v >= (distance[i-2]-distance[i-4]) and distance[i-1] >= (distance[i-3]-distance[i-5]) and distance[i-1] < distance[i-3] and distance[i-2] > distance[i-4] and distance[i-3] > distance[i-5]:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.isSelfCrossing(*tc))
