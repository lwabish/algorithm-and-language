import re
line = 'asdf fjdk; afed, fjek,asdf, foo'
# 不保留分隔字符
print(re.split(r'[;,\s]\s*', line))
# 保留分隔字符
print(re.split(r'(;|,|\s)\s*', line))
