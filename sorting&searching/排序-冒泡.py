# 遍历，两两比较，不符合顺序的交换二者位置，每一轮找出一个最大值。
# 时间复杂度：On2
# 空间复杂度：O1
# 弊端：在最坏情况下（全部反序）需要大量挪动

tc = [3, 4, 2, 4, 5, 6, 1, 0, -4, 10, 4]
tc = []
tc = [1]
tc = [1, 2, 3]
tc = [3, 2, 1]
tc = [2, 2, 2]


# in_order标志实现已经排好序的部分不再扫描。
def main(numbers):
    for i in range(len(numbers)):  # 第几大
        in_order = True
        for j in range(len(numbers)-i-1):  # 左侧待扫描部分
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                in_order = False
        if in_order:
            break
    return numbers


if __name__ == '__main__':
    print(main(tc))
