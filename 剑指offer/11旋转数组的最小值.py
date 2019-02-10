# 粗暴方法的复杂度是n，用二分查找的思想实现logn的复杂度

# 普通测试用例
tc = [7, 8, 9, 1, 2, 3, 4, 5, 6]
# 长度特殊，引起越界的测试用例
tc = [2, 1]
tc = [1]
# 特殊的旋转数组，即本身，是一个排序数组的旋转数组
tc = [1, 2, 3, 4]
# 包含重复数字的旋转数组
tc = [1, 0, 1, 1, 1]
# 其他特殊数组
tc = [2, 2]
tc = [1, 1, 1, 1, 1]
tc = [1, 2]
tc = [1, 1, 3]


def main(nums):
    # end指针没有减一，会使特殊情况的middle指针最终移到最后一位。如果end初始指针在len(nums)-1，则最终的middle指针会在倒数第二位
    start, end = 0, len(nums)
    while start < end:
        print(start, end)
        middle_index = int((start + end) / 2)
        if middle_index + 1 == len(nums):  # 中间指针到了最后一位，此时有三种情况：
            if middle_index == 0:  # 最后一位就是第一位，说明只有一个数字
                return nums[-1]
            elif nums[middle_index] < nums[middle_index - 1]:  # 最后一位比前一位小，这是有两个数字的普通旋转数组
                return nums[-1]
            else:   # 没旋转的旋转数组
                return nums[0]
        if nums[middle_index] > nums[middle_index + 1]:
            return nums[middle_index+1]
        if nums[middle_index] > nums[0]:
            start = middle_index
        elif nums[middle_index] < nums[0]:
            end = middle_index
        else:  # middle指向的数和后面相等，采用暴力查找
            smallest = nums[0]
            for i in nums:
                if i < smallest:
                    smallest = i
            return smallest


if __name__ == '__main__':
    print(main(tc))
