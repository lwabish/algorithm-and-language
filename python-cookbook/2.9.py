# 问题：一些字符用unicode表示可以有不同的方法。
import unicodedata
print('\u00f1o', 'n\u0303o')


# 虽然得到的结果是一样的，但是在底层不是一样的字符串，程序中判断会出现错误。所以需要在底层使用统一化的字符串
s1 = '\u00f1o'
s2 = 'n\u0303o'
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)
print(t1, ascii(t1))
