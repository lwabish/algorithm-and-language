# 字符串合并

# 1：+ (不宜多)
# 2：join
# 3：直接连写
a = 'a' 'b'
print(a)


# 小字符串的连续拼接,要考虑性能，且结合IO
def sample():
    yield 'a'
    yield 'b'
    yield 'c'
    yield 'd'


print(''.join(sample()))
