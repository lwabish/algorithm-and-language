# 合并字典

# 物理上合并字典update方法
from collections import ChainMap
a = {1: 2, 2: 3}
a.update({1: 10, 3: 4})  # 原地操作
print(a)

# 逻辑上合并

d1 = {1: 2, 2: 3}
d2 = {3: 4, 4: 5}
d_merge = ChainMap(d1, d2)
print(d_merge)

# 注意：重复键以第一个字典为准。更新和删除也总是对第一个字典操作。

# ChainMap的分层
values = ChainMap()
values[1] = 1
values = values.new_child()
values[1] = 2
print(values)
values = values.parents
print(values)
