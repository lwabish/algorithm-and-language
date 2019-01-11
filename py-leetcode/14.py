tc = ["flower", "flow", "flight"]
tc = []
tc = ['abc']
tc = ["dog", "racecar", "car"]
tc = ['c', 'c']
tc = ["aa", "a"]
# tc = ['a', 'aa']


def main(strs):
    t = 0   # 位数指针
    tmp = list()  # 判断是否有相异字符串的临时列表
    end = False
    # 我的这个sb算法对['a','aa']这样的输入的顺序有要求，必须是短字符串在前，所以先排序
    strs.sort(key=lambda x: len(x))
    while not end:
        if len(strs) > 1:  # 多于一个元素
            for word in strs:
                try:                  # 测试指针是否已经到了某个单词的末尾，是则停止循环
                    if word[t] == '1':
                        pass
                except IndexError:
                    end = True
                    break
                try:
                    if tmp[t] != word[t]:  # 对比当前单词的当前指针字符串和tmp中上一个是否一样，不一样则停止
                        end = True
                        tmp.pop()
                        break
                except IndexError:  # 如果是第一个单词，直接把第一个词的当前字母作为被比较目标放进tmp
                    tmp.append(word[t])
            t += 1
            result = ''.join(tmp)  # join方法用于粘合序列
        elif len(strs) == 0:
            result = ''
            break
        else:
            result = strs[0]
            break
    return result


if __name__ == '__main__':
    print(main(tc))
