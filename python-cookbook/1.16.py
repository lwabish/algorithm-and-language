# 序列元素过滤

# 1.生成式内判断
from itertools import compress
nums = [1, 2, 3, 4]
# 列表生成式占内存大
print([n for n in nums if n % 2 == 0])
# 生成器推导占内存小
print((n for n in nums if n % 2 == 0))


# 2.filter函数加自定义的def
# 返回值类似生成器
print(filter(None, [1, 2, 0]))


# 3 将数据与同维度的bool值对比，true的留下
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]
bools = [n > 5 for n in counts]
print(compress(addresses, bools))
