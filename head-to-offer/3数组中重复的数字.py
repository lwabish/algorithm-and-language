# 判断长度为n，由0-(n-1)构成的数组中是否存在重复的数字
from collections import Counter
from time import sleep
tc = [2, 3, 1, 0, 2, 5, 3]  # 负例
tc = [3, 2, 1, 0]   # 正例
tc = [0]  # 边界
# tc = [10, 11]  # 不符合题意的输入是否需要测试？


# 方法1：排序、遍历数组比较
# 方法2：遍历数组，尝试查找并移动元素到另一个数组，如果另一个数组中已经存在结果，则有重复，否则移动。
# 方法3：重排法。空间复杂度1，时间复杂度n（每个数字最多两次就能移动到位）
def m3(nums):
    for t in range(len(nums)):
        while nums[t] != t:  # 索引=值
            if nums[t] == nums[nums[t]]:
                return True
            else:
                nums[nums[t]], nums[t] = nums[t], nums[nums[t]]
                print(nums)
    return False

# 长度为n+1的数组中，所有数字的范围都在1-n，找出任意一个重复的数字


tc1 = [1, 3, 5, 4, 6, 2, 6, 7]
tc1 = [2, 3, 5, 4, 3, 2, 6, 7]
tc1 = [1, 1]  # 边界

# 方法0：排序后查找
# 方法1：用辅助数组，空间复杂度高
# 方法2：原地找，二分查找。空间复杂度1，时间复杂度nlogn，属于用时间换空间的算法


def main(nums):
    def get_count(start, end):
        sum = 0
        tmp = Counter(nums)
        for i in range(start, end + 1):
            sum += tmp[i]
        return sum
    # print(get_count(1, 4))
    start = 1
    end = len(nums) - 1
    while start != end:
        sleep(1)
        mid_value = int((start + end) / 2)  # 注意里面的括号
        # print(start, end, mid_value, get_count(start, end), mid_value-start)
        if get_count(start, mid_value) != mid_value-start+1:
            end = mid_value
            continue
        if get_count(mid_value + 1, end) != end - mid_value:
            start = mid_value + 1
            continue
    return start


if __name__ == '__main__':
    print(m3(tc))
    print(main(tc1))
