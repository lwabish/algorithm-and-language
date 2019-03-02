# 用heapq实现优先级队列
import heapq


class PriorityQuene(object):
    def __init__(self):
        self._quene = list()
        self._index = 0

    def push(self, item, priority):
        """
        内部存储不是直接存Item
        存储一个三元组
        -priority实现按优先级从高到低弹出
        _index实现同优先级比较时按照加入顺序排序,且可以避免加入的东西不能排序，用heap的时候就会出错
        原理：heap在比较时，比较的是元组。元组比较时，是惰性比较。
        """
        heapq.heappush(self._quene, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._quene)[-1]

# 使用


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQuene()
q.push(Item('1'), 2)
q.push(Item('2'), 1)
q.push(Item('3'), 5)
q.push(Item('4'), 5)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
