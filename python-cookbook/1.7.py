# 有序字典
# 对于一个已经存在的键的重复赋值不会 改变键的顺序。
# 需要注意的是，一个 OrderedDict 的大小是一个普通字典的两倍，因为它内部维 护着另外一个链表。
import json
from collections import OrderedDict

d = OrderedDict()
d['a'] = 4
d['b'] = 3
d['c'] = 2

# 尤其适合需要序列化的对象
print(json.dumps(d))
