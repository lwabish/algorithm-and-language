# 命名切片
# 使得你的代码更加清晰可读
record = '12345abc32323434def233'
first_letters = slice(5, 8)
second_letters = slice(16, 19)
data = record[first_letters] + record[second_letters]
print(data)


# 按新长度缩放slice
test = slice(2, 20, 2)
some_text = 'afgsdfsdsdf'
new_test = test.indices(len(some_text))
print(new_test)
