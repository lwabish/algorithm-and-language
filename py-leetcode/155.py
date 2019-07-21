
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.helper = list()
        self.stack = list()

    def push(self, x: int) -> None:
        self.stack.append(x)
        # 特别注意这里的等号不能少
        if not self.helper or x <= self.helper[-1]:
            self.helper.append(x)

    def pop(self) -> None:
        if self.stack:
            if self.helper[-1] == self.stack[-1]:
                self.helper.pop()
            return self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.helper[-1]
