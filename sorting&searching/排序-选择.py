# 遍历，在一批数中找出最大值（或同时找出最大值最小值），并摆放就位，直到所有数字都摆放好。
# 时间复杂度On2
# 空间复杂度O1
# 性能略好于冒泡排序，不需要太频繁的挪移
tc = [5, 4, 8, 2, 0, 6]
tc = []
tc = [1]
tc = [1, 2, 3, 4]
tc = [4, 3, 2, 1]
tc = [2, 2, 2, 2]


# 一元选择排序，依次挑出最大的值往左侧放
def main(nums):
    head = 0
    while head < len(nums):
        max_index = head
        for t in range(head, len(nums)):
            if nums[t] > nums[max_index]:
                max_index = t
        if max_index != head:
            nums[max_index], nums[head] = nums[head], nums[max_index]
        head += 1
    return nums


# 二元选择排序，每一轮在挑出最大值的同时，挑出最小值往另一端放
def main2(nums):
    # 初始化头尾两个指针，head是放最大值的指针，tail是放最小值的指针
    head, tail = 0, len(nums) - 1
    while tail - head > 1:
        max_i, min_i = head, tail
        for i in range(head, tail + 1):
            if nums[i] > nums[max_i]:
                max_i = i
            if nums[i] < nums[min_i]:
                min_i = i

        # 优化点：如果一次里找到的极大值和极小值是相等的，说明以后的所有循环都会是相等的，就不需要再移动了。
        if nums[max_i] == nums[min_i]:
            break

        if max_i != head:

            # 非常关键的一个细节：第一次移动最大值的时候，会改变nums的下标索引，从而可能影响后一步移动最小值时的判断。所以需要检查移动最大值的时候是否影响到min_i
            if min_i == head:   # 如果min_i正好在要移动的位置上，那么就把移动后的值给min_i
                min_i = max_i
            elif min_i == max_i:  # 如果min_i正好在要移动的位置上，那么就把移动后的值给min_i
                min_i = head

            # 移动最大值
            nums[max_i], nums[head] = nums[head], nums[max_i]

        # 轻微优化：额外判断一下值是否相等，避免相等时依然挪动
        if min_i != tail and nums[min_i] != nums[tail]:
            # 移动最小值
            nums[min_i], nums[tail] = nums[tail], nums[min_i]
        head += 1
        tail -= 1
    return nums


if __name__ == '__main__':
    print(main(tc))
    print(main2(tc))
