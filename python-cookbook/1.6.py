# 用defaultdict实现多值字典:只需要把default设置为list即可
from collections import defaultdict

multivalue_dict = defaultdict(list)

multivalue_dict[1].append(11)
multivalue_dict[1].append(21)


# 等价方法
d = {}
d.setdefault(1, []).append(11)
d.setdefault(1, []).append(21)
