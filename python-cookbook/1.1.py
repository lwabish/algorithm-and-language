# 结构赋值
# 变量数和元素数必须对应，否则抛出ValueError
p = (4, 5)
x, y = p

data = ['a', 'b', 4, 5, (1, 2, 3,)]
a, b, c, d, e = data
a, b, c, d, (e, f, g) = data

a, b, c, d, e = 'abcde'
_, _, a = 'abc'
