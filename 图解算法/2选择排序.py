# 复杂度n**2
# append+pop的方法简单易懂易操作


def select_sort(arr=[]):
    # 从列表中找出最小元素
    def find_smallest(arr=[]):
        smallest = arr[0]
        for i in arr:
            if i < smallest:
                smallest = i
        return arr.index(smallest)
    # 每次都找出最小数的索引，从旧的pop掉，放进新的
    sorted_arr = list()
    while arr:
        smallest_index = find_smallest(arr)
        print(arr, '\t', smallest_index, '\t', sorted_arr)
        sorted_arr.append(arr.pop(smallest_index))
    return sorted_arr


print(select_sort([4, 2, 5, 1]))
