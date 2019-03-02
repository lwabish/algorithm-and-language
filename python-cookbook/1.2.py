# *号解构
# 尤其适用于变长数据结构


def count_middle_avg(grades: list):
    _first, *mid, _last = grades
    return sum(mid) / len(mid)


record = ('a', 'b', 1, 2)
a, b, *nums = record
# *结构出的变量永远是list
type(nums)

sales_record = (1, 2, 1, 2, 3, 4, 2)
*past_data, now_data = sales_record
past_avg = sum(past_data) / len(past_data)
# do something with past_avg and now data
