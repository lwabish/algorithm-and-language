# 字符串对齐
# 1.str.ljust(),rjust(),center()

print('hello'.ljust(20))
print('hello'.rjust(20, '='))
print('hello'.center(20))

# 2.format
print('{:=>20}'.format('hello'))
