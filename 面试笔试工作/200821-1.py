# 输入：5 1 2 3 4 5 输出：0 3.0

def count(args):
    args = list(map(lambda x: int(x), args.split(' ')))
    minus_number = list(filter(lambda x: x < 0, args[1:]))
    non_minus_number = list(filter(lambda x: x >= 0, args[1:]))
    result1 = len(minus_number)
    result2 = round(sum(non_minus_number)/len(non_minus_number),
                    1) if non_minus_number else 0
    return result1, result2


print(count('5 -1 -2 -3 -4 -5'))
