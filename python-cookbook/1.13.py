# 对装满字典的列表排序
from operator import itemgetter
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
# 1.用lambda表达式，速度稍慢于2
print(sorted(rows, key=lambda x: x['fname']))


# 2.用itemgetter。可以支持多关键字排序（原理还是用元组排序，即可以依次排序）
print(sorted(rows, key=itemgetter('fname', 'uid')))
