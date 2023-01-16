class Car:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def add_oil(self):
        pass


class Battery:
    def __init__(self, b=100):
        pass


class Ecar(Car):
    # 子类的init函数
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        self.d = d
        self.battery = Battery()

    def add_oil(self):
        # 重写，覆盖父类的方法
        pass


my_ecar = Ecar(1, 2, 3, 4)
print(my_ecar.d, my_ecar.c)
