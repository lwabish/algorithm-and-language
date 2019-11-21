import sys
from itertools import permutations
from luabish.common import print_used_time

n = sys.stdin.readline().strip()


@print_used_time
def F_value(x, A):
    res = ['', A[0]]
    for i in range(2, x+1):
        res.append(abs(res[i-1]-A[i-1]))
    return res[x]


@print_used_time
def F_wrapper(x):
    def F_value(A):
        if x == 1:
            return A[0]
        return abs(F_wrapper(x-1)(A)-A[x-1])
    return F_value


for i in range(int(n)):
    line = int(sys.stdin.readline().strip())
    min_res, max_res = float('inf'), float('-inf')

    for arr in permutations(list(range(1, line+1))):
        min_res = min(min_res, F_value(line, arr))
        max_res = max(max_res, F_value(line, arr))
    print(min_res, max_res)
    # print(min(list(map(F_wrapper(line), permutations(range(1, line+1))))),
    #   max(list(map(F_wrapper(line), permutations(range(1, line+1))))))
