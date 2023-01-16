# 规则：.代替任意字符，*代表前面的字符出现0-N次
def main(string, pattern):
    # print(string, pattern)
    if string == '' and pattern == '':
        return True
    if (string == '' and pattern != '') or (string != '' and pattern == ''):
        return False

    def get_next_patter(pattern):
        # 获取本次要匹配的正则
        if len(pattern) > 1:
            if pattern[1] == '*':
                this_pattern = pattern[0:2]
            else:
                this_pattern = pattern[0]
        else:
            this_pattern = pattern[0]
        return this_pattern
    this_pattern = get_next_patter(pattern)
    if len(this_pattern) == 1:
        if this_pattern == '.' or this_pattern == string[0]:
            return main(string[1:], pattern[1:])
        else:
            return False
    else:
        wildcard_string = this_pattern[0]
        # 待匹配的第一个字符和通配符字符一致
        if wildcard_string == string[0]:
            # 情况1：通配符匹配了第一个字符消耗掉
            result_1 = main(string[1:], pattern[2:])
            # 情况2：通配符匹配了第一个字符后继续匹配
            result_2 = main(string[1:], pattern)
            # 只要有一种情况匹配成功，就说明匹配成功
            if result_1 or result_2:
                return True
            else:
                return False
        # 待匹配的第一个字符和通配符字符不一样，则只能认为通配符字符没出现
        else:
            return main(string, pattern[2:])


if __name__ == '__main__':
    # 纯字符正例
    tc_str = 'aaa'
    tc_pattern = 'aaa'
    # 纯字符负例
    tc_str = 'aaa'
    tc_pattern = 'aba'
    tc_pattern = 'aaaa'
    # .正例
    tc_pattern = 'a.c.tq'
    tc_str = 'a7c3tq'
    # .负例
    tc_str = 'a77c9tq'
    # *正例
    tc_pattern = 'ab*c*defg'
    tc_str = 'abbbbbccdefg'
    # *负例
    tc_str = 'adcdefg'
    # .*混合正例
    tc_pattern = 'ab*.td*'
    tc_str = 'abbbqtddddd'
    # .*混合负例
    tc_str = 'abbbqqtddd'
    print(main(tc_str, tc_pattern))
    assert main(tc_str, tc_pattern) == False
