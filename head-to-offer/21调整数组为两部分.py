# 按照某种标准，把一个数组中符合标准的和不符合标准的分到左右两部分。
tc = [3, 4, 5, 6, 7, 8, 9, 10, 11]
tc = [1]
tc = []
tc = [1, 3, 5, 2, 4, 6]
tc = [2, 4, 6, 1, 3, 5, 7]


# 思路跟二元选择排序类似
def main(nums):
    def seperate_number(n):
        """
        调整数组顺序的标准
        按照什么标准将数组分为两部分？
        目前的例子是按照奇数偶数
        这个函数可以根据需求灵活改动
        函数的主要部分将按照这个函数的处理结果来重排数组的顺序
        false在左，true在右
        """
        if n % 2:  # 奇数
            return False
        return True
    false_index = 0
    true_index = len(nums) - 1
    while false_index < true_index:
        left_num = nums[false_index]
        right_num = nums[true_index]
        # 最终实现的顺序是左false右true
        if seperate_number(left_num) and not seperate_number(right_num):
            nums[false_index], nums[true_index] = nums[true_index], nums[false_index]
            false_index += 1
            true_index -= 1
        elif seperate_number(left_num) and seperate_number(right_num):
            true_index -= 1
        elif not seperate_number(left_num) and not seperate_number(right_num):
            false_index += 1
        else:
            false_index += 1
            true_index -= 1
    return nums


if __name__ == '__main__':
    print(main(tc))
