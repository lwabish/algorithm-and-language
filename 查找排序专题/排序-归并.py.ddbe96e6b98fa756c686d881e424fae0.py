tc = [
    [4, 7, 1, 3, 2, 8],
    [1],
    [],
    [1, 2, 3,4,5],
    [5,4,3,2,1],
]


def main(nums):

    def merge(nums1, nums2):
        res = list()
        while nums1 or nums2:
            c1 = c2 = float('inf')
            if nums1:
                c1 = nums1[0]
            if nums2:
                c2 = nums2[0]
            if c1 < c2:
                res.append(c1)
                nums1.pop(0)
            else:
                res.append(c2)
                nums2.pop(0)
        return res

    def cut(nums):
        if len(nums) < 2:
            return nums
        mid_index = int(len(nums)/2)
        left = cut(nums[:mid_index])
        right = cut(nums[mid_index:])
        return merge(left, right)
    return cut(nums)


if __name__ == '__main__':
    for i in tc:
        print(main(i))
