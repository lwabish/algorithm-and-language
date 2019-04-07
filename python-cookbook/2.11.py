# strip
# strip只对字符串两端生效，对中间无效。
# 参数长度大于1的字符串时，是和的关系，不是且
a = '----hello===='
print(a.strip('-='))
