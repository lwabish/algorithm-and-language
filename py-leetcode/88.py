nums1 = [1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0]
m = 3
nums2 = [1, 2, 3, 4, 5, 6, 7, 10]
n = 8

# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1

nums1 = [4, 0, 0]
m = 1
nums2 = [1, 2]
n = 2


# 要利用nums1和nums2都是排序数组这一特点，都从右侧开始比，两个最大中的最大就一定是最后的最大，所以就依次把最大往右侧塞
# 注意，当1全部比2里小时，可能只挪了1，没把2塞进去。所以需要判断，当m比n先到零时，说明没有全部塞进去
def main(nums1, m, nums2, n):
    l = len(nums1) - 1
    while m > 0 and n > 0:
        if nums1[m-1] > nums2[n-1]:
            nums1[l] = nums1[m-1]
            m -= 1
        else:
            nums1[l] = nums2[n-1]
            n -= 1
        l -= 1
    if m < n:
        for t in range(n):
            nums1[t] = nums2[t]

    return m, n


if __name__ == '__main__':
    print(main(nums1, m, nums2, n))
    print(nums1)
