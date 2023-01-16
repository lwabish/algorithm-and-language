tc = [
    [4, 7, 1, 3, 2],
    [1],
    [],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
]


# 原地移动，没有使用切片
def main(nums):
    def to_right_1_digit(start, end):
        """
        将nums数组从start到end的值整体原地右移一位\n
        end+1的值将被覆盖
        """
        for i in range(end + 1, start, -1):
            nums[i] = nums[i - 1]
    sep_index = 1
    while sep_index < len(nums):
        this_val = nums[sep_index]
        for i in range(sep_index - 1, -1, -1):
            if nums[i] <= this_val:
                # 如果被比较的值并不比左边有序数组的最大值小，那么就直接sep_index+=1进行下一位的插入
                if i == sep_index - 1:
                    break
                # 找到的位置在中间
                to_right_1_digit(i+1, sep_index-1)
                nums[i + 1] = this_val
            # 如果到了有序数组的第一位还没找到，那么待插入的值应该插入到最左端。
            elif not i:
                to_right_1_digit(0, sep_index-1)
                nums[0] = this_val
        sep_index += 1
    return nums


if __name__ == '__main__':
    for i in tc:
        print(main(i))
