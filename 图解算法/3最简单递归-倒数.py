def count_down(x):
    print(x)
    if x == 1:  # 基线条件（停止递归的条件）
        return
    else:  # 递归条件
        count_down(x-1)


count_down(5)
