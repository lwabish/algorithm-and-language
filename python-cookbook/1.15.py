# 字典数据分组

from itertools import groupby
from operator import itemgetter
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

# groupby
# 先按照要分组的数据排序
rows.sort(key=itemgetter('date'))
for date, item in groupby(rows, key=itemgetter('date')):
    print(date)
    print('    ', item)
    for i in item:
        print('    ', i)


# 如果只是为了分组存储，可以结合defaultdict构建多值字典，然后分组存储
