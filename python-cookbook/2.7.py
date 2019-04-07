# 正则的贪婪与非匹配
# 使用.*匹配时会尽可能长地匹配
import re
text = 'aaaaa"bbbbb"ccccc"ddddd"'
print(re.findall(r'\"(.*)\"', text))

# 在*后加？可改成非贪婪匹配，会匹配到最短的符合模式的字符串
print(re.findall(r'\"(.*?)\"', text))
