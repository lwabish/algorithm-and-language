# 复杂度：logn
# 实现关键：把控住起始点和结束点；每次修改起始点或结束点时，要加一或者减一使区间永远在缩小，避免区间出现不变的情况陷入死循环

import random


def binary_search(element, arr=[]):
    arr.sort()
    low, high = 0, len(arr)-1
    while low <= high:
        this_guess_index = int((low + high) / 2)
        this_guess = arr[this_guess_index]
        print('[{}-{}]'.format(low, high),
              '[{}]'.format(this_guess_index), '[{}]'.format(this_guess))
        if this_guess < element:
            low = this_guess_index+1
        elif this_guess > element:
            high = this_guess_index-1
        elif this_guess == element:
            return this_guess_index
        else:
            return None


print(binary_search(44, [random.randint(0, 100) for i in range(100)]))
