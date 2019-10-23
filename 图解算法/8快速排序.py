import random
import time


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    elif len(arr) == 2:
        return [arr[1], arr[0]] if arr[0] > arr[1] else [arr[0], arr[1]]
    else:
        # 方法2：书上的做法：每次以第一项为基准值
        piv_index = 0
        smaller = [i for i in arr[1:] if i <= arr[piv_index]]
        greater = [i for i in arr[1:] if i > arr[piv_index]]
        return quick_sort(smaller)+[arr[piv_index]]+quick_sort(greater)

        # 方法3：每次以中间索引值为基准值（注意在切片smaller和greater时需要保证每次的结果都要是上次的真子集，否则可能无限递归，类似于书上的arr[1:]的做法，而不是直接用arr。就是所谓的递归中确保问题的规模可以缩小）
        # piv_index = int(len(arr) / 2)
        # smaller = [i for i in arr[:piv_index] if i <= arr[piv_index]
        #            ]+[i for i in arr[piv_index+1:] if i <= arr[piv_index]]
        # greater = [i for i in arr[:piv_index] if i >
        #            arr[piv_index]]+[i for i in arr[piv_index+1:]]
        # return quick_sort(smaller)+[arr[piv_index]]+quick_sort(greater)

        # 方法1：我最开始的做法
        # piv_index = int(len(arr) / 2)           # 每次以中间索引值为基准值
        # smaller = [i for i in arr if i < arr[piv_index]]
        # greater = [i for i in arr if i > arr[piv_index]]
        # equal = [i for i in arr if i == arr[piv_index]]
        # if smaller == [] and greater == []:  # 此处如果不判断，会遇到[4,4,4]这样的arr，会导致无限递归
        #     return equal
        # return quick_sort(smaller)+quick_sort(equal)+quick_sort(greater)


# 测试速度
for t in range(1, 8):
    list_length = 10**t
    # list_length = random.randint(1, 100)
    a_list = [random.randint(0, list_length) for t in range(list_length)]
    start = time.time()
    result = quick_sort(a_list)
    end = time.time()-start
    print('list_length:', list_length, 'time_length:', end)

'''
方法1：基准值选择中间项(第一版)时的时间
list_length: 1 time_length: 1.3828277587890625e-05
list_length: 10 time_length: 0.00014591217041015625
list_length: 100 time_length: 0.0009179115295410156
list_length: 1000 time_length: 0.009429931640625
list_length: 10000 time_length: 0.1020059585571289
list_length: 100000 time_length: 0.95843505859375
list_length: 1000000 time_length: 12.558405876159668
list_length: 10000000 time_length: 158.15353107452393
'''
'''
方法2：书上基准值选择第一项
list_length: 1 time_length: 6.9141387939453125e-06
list_length: 10 time_length: 5.4836273193359375e-05
list_length: 100 time_length: 0.00045418739318847656
list_length: 1000 time_length: 0.007409811019897461
list_length: 10000 time_length: 0.0798337459564209
list_length: 100000 time_length: 0.7678031921386719
list_length: 1000000 time_length: 9.556749105453491
list_length: 10000000 time_length: 128.0651729106903
'''
'''
方法3：模仿书上的思路，基准项选择中间值
list_length: 10 time_length: 0.00026702880859375
list_length: 100 time_length: 0.008851051330566406
list_length: 1000 time_length: 0.78302001953125
list_length: 10000 time_length: 97.71110486984253
'''
