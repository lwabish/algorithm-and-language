# 我的方法
def my_max(max_, arr=[]):
    if arr == []:
        return max_
    elif max_ < arr[0]:
        max_ = arr[0]
        return my_max(max_, arr[1:])
    else:
        return my_max(max_, arr[1:])

# 书上方法


def my_max_2(arr=[]):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    else:
        sub_max = my_max_2(arr[1:])
        return arr[0] if arr[0] > sub_max else sub_max


print(my_max(-float('inf'), [1, 2, 3, 4]))
print(my_max_2([1, 2, 3, 4, 3]))
