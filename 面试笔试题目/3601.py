line1 = input()
human_n, desk_n = [int(i) for i in line1.split()]
line2 = input()
nums = [int(i) for i in line2.split()]
# 升序排列
nums.sort()
desks = [[] for _ in range(desk_n)]


def main():
    if human_n <= desk_n:
        print(0)
        return
    for desk in desks:
        desk.append(nums.pop())

    for i in range(len(nums) - 1, -1, -1):
        desk_number = i-len(nums)
        desks[desk_number].append(nums[i])
    print(sum(desks[-len(nums)]))


main()
