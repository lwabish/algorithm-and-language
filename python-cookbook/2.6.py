# 搜索时忽略大小写
import re
text = "UPPER PYTHON,lower python,Mixed Python"
res = re.findall('python', text, flags=re.IGNORECASE)
print(res)


# 替换时原样替换，不匹配原字符串的大小写。替换的结果是所有python都被替换成了小写的snake。
res = re.sub('python', 'snake', text, flags=re.IGNORECASE)
print(res)


# 替换时匹配大小写，原来是大写依然是大写，原来小写依然是小写.原来是首字母大写则依然首字母大写。
def match_case(word):
    def replace(m):
        # group()==group(0)匹配的完整文本
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace


res = re.sub('python', match_case('snake'), text, flags=re.IGNORECASE)
print(res)
