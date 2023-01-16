from typing import List
tcs = [
    # (1,),
    # (2,),
    # (3,),
    # (4,),
    # (5,),
    (6,),
    # (7,),
    # (8,),
    # (9,),
]


class Solution:
    def count_split(self, number):
        MEMO = {
            1: 0,
            2: 0,
            3: 1
        }
        if number < 4:
            return MEMO[number]
        for n in range(4, number+1):
            print('update ', n)
            result = 0
            for i in range(int(n/2)+1, n):
                print(i)
                result += 1
                result += MEMO[i]
                MEMO[n] = result
        print(MEMO)
        return MEMO[number]


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print('\tresult ', solution.count_split(*tc))
