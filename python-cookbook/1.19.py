# 数据的中间处理
# 使用生成式即可
# 生成器作为别的函数的参数时可以不加[]

# 例1
import os
nums = [1, 2, 3]
total = sum(n*n for n in nums)
print(total)

# 2
files = os.listdir(os.getcwd())
if any(file.endswith('py') for file in files):
    print(True)
else:
    print(False)

# 3
s = ('a', 'b', 'c')
print(','.join(t for t in s))

# 4
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]

least = min(item['shares'] for item in portfolio)
print(least)
