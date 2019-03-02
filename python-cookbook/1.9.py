# 字典异同
# 原理利用dict.keys dict.items返回的集合进行集合操作

a = {
    'x': 1,
    'y': 2,
    'z': 3}
b = {
    'w': 10,
    'x': 11,
    'y': 2}

print(a.keys() & b.keys())
# dict.values返回的不是集合
print(a.values())
print(a.items() & b.items())
