tc = 4
# 脑残了，一开始的思路是先算出所有三十个，然后根据n的值从这三十个里找，显然很慢，永远需要计算这三十个
# 高效的方法不就是要多少算到多少吗？-_-!

# 多层循环时，每层循环对应的题目里的状态容易乱，需要小心


def main(n):
    results = list(['1'])
    for t in range(1, n):
        last_str = results[t - 1]
        this_str = '#'
        counter = 1
        this_result = ''
        for s in range(len(last_str)):
            if last_str[s] != this_str:
                this_result += str(counter) + str(this_str)
                counter = 1
                this_str = last_str[s]
            else:
                counter += 1
            # 收尾：最后一个数字不需要判断，直接加入结果中。本来第一个数字也应该如此处理，但是前面用技巧省去了，因为初始值是#号，所以合并在了前面的判断里。
            if s == len(last_str) - 1:
                this_result += str(counter) + str(this_str)
        results.append(this_result[2:])
    return results[-1]


if __name__ == '__main__':
    print(main(tc))
