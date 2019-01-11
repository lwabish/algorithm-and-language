# 递归（分而治之思想）的步骤：
# 1-确定基线条件
# 2-缩小问题规模
# 3-递归调用

# 简单的方法见6


def my_sum(total=0, arr=[]):
    if len(arr) == 1:
        return total+arr[0]
    else:
        last_num = arr.pop()
        total += last_num
        print(total, arr)
        return my_sum(total, arr)


print(my_sum(0, [1, 2, 3]))
