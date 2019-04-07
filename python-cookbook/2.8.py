# 问题：正则中.能匹配任意字符，但是不匹配换行符。所所以遇到多行字符串时就不能用了。

import re
text = """
hahah
/*aaaa
bbb
ccc
*/
"""
# 解决1：使用re.DOTALL标志
m = re.compile(
    r'/\*(.*?)\*/', re.DOTALL
)
res = m.findall(text)
print(res)
# 解决2：改写正则表达式,在.的基础上把\n考虑进来
m = re.compile(r'/\*((?:.|\n)*?)\*/')
res = m.findall(text)
print(res)
