import os
print([file for file in os.listdir() if file.endswith(('py', 'exe'))])
# endswith及startswith可以接收元组作为参数，匹配多个开头或者结尾
