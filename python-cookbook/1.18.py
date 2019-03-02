# 通过名称索引序列的元素：命名元组
# 好处：代码易读。可以代替字典节省空间。
from collections import namedtuple


# 返回一个工厂函数
Sub = namedtuple('Sub', ['addr', 'joined'])
sub = Sub('10000', '1999')

print(sub.joined, sub.addr)
# 支持元组的操作

# 唯一和字典不同的：不可直接修改
# 间接修改：
sub = sub._replace(addr='42242')
print(sub)
# 可以先构造原型，再用_replace函数基于新的数据构造生成新的实例

proto = Sub('temp', 'temp')


def build(data: dict) -> int:
    return proto._replace(**data)


new_sub = build({'addr': 'hhaha', 'joined': 'jsdfjdskf'})
print(new_sub)
