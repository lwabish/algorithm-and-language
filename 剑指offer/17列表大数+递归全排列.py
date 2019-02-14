tc = 3
tc = -1
tc = 0


def main(n):
    # 将列表中的数字打印出来，但是不打印前面的补位0
    def print_list(l):
        first_non_0_index = 0
        for i in range(len(l)):
            if l[i] != '0':
                first_non_0_index = i
                break
            # 如果已经到了最后一位依然是0，说明这个数是0，不打印
            if i == len(l) - 1:
                return
        real_num = ''.join(l[first_non_0_index:])
        print(real_num)

    def generate_int(num_list, index):
        if index == len(num_list):
            print_list(num_list)
            return
        for i in range(10):
            num_list[index] = str(i)
            generate_int(num_list, index+1)
    if n <= 0:
        print('非法输入')
        return
    generate_int([0]*n, 0)


if __name__ == '__main__':
    main(tc)
