# 字符串替换
import re
# 1.
'abc'.replace('a', 'b')

# re.sub正则匹配替换,subn还可以返回替换次数
a = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', '11/23/1990')
print(a)


# re.sub正则匹配函数替换
pattern = re.compile(r'(\d+)/(\d+)/(\d+)')


def replace_func(pattern):
    from calendar import month_abbr
    month = month_abbr[int(pattern.group(1))]
    return '{} {} {}'.format(pattern.group(3), month, pattern.group(2))


b = pattern.sub(replace_func, '2/22/1997')
print(b)
