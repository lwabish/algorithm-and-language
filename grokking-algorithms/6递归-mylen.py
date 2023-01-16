# 我的思路，需要一个计数器
def my_len(counter=0, arr=[]):
    if arr == []:  # 两个空列表的比较是可行的
        return counter
    else:
        counter += 1
        arr.pop()
        return my_len(counter, arr)

# 书上的方法，巧妙地利用了递归参数的传递——在递归中使用list[1:]即可实现列表的逐渐缩减


def my_len_2(arr=[]):
    if arr == []:
        return 0
    else:
        return 1+my_len_2(arr[1:])


print(my_len(0, [1, 1, 1, 1, 1, 1]))
print(my_len_2([1, 1, 1, 1, 1, 1]))
