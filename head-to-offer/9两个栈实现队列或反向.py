from my_data_structure import Stack
from queue import deque


class TwoStackQuene():
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def add(self, thing):
        self.s1.add(thing)

    def pop(self):
        if self.s2:
            return self.s2.pop()
        else:
            if not self.s1:
                return '空队列'
            else:
                while self.s1:
                    self.s2.add(self.s1.pop())
                return self.s2.pop()


class TwoQueneStack():
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def add(self, thing):
        self.q1.append(thing)

    def pop(self):
        if self.q1:
            while len(self.q1) > 1:
                self.q2.append(self.q1.popleft())
            return self.q1.popleft()
        else:
            if not self.q2:
                return 'empty stack'
            while len(self.q2) > 1:
                self.q1.append(self.q2.popleft())
            return self.q2.popleft()


if __name__ == '__main__':
    def test_quene():
        test_q = TwoStackQuene()
        # 空队列入队
        test_q.add(1)
        test_q.add(2)
        # 非空队列出队
        print(test_q.pop())
        # 非空队列入队
        test_q.add(3)
        test_q.add(4)
        # 连续出队，清空队列
        print(test_q.pop())
        print(test_q.pop())
        print(test_q.pop())
        # 空队列出队
        print(test_q.pop())

    def test_stack():
        test_s = TwoQueneStack()
        # 空栈压入
        test_s.add(1)
        test_s.add(2)
        # 非空栈弹出
        print(test_s.pop())
        # 非空栈压入
        test_s.add(3)
        # 中间压入后弹出
        print(test_s.pop())
        print(test_s.pop())
        # 空栈弹出
        print(test_s.pop())
    test_stack()
