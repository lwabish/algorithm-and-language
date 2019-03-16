# python的单例


# 方法1：模块
# 直接把def或者data保存在模块中。
# 类：在模块中定义并且实例化即可。from xxx import s即可得到单例的对象
import threading
import time
from my_universal_operation import Singleton


class S:
    def foo(self):
        pass


s = S()
# 模块的最后删除类，防止被import生成别的实例化对象
del S

# 方法2：装饰器


@Singleton
class test:
    a = 0

    def __init__(self, x):
        self.a = x


t1 = test(1)
# print(t1.a)
# 单例模式下，得到的仍然是已经存在的类
t2 = test(2)
# print(t2 == t1)
# print(t2.a)


# 方法3：类的属性判断，注意多线程，需要加锁，且这种方式下必须使用get_instance获得对象，不能使用不同方法实例化


class Test3:
    # 设置一把锁
    _instance_lock = threading.Lock()

    def __init__(self):
        time.sleep(1)

    @classmethod
    def get_instance(cls, *args, **kwargs):
        # 只在还没有实例化的时候加锁
        if not hasattr(Test3, '_instance'):
            # 加锁
            with Test3._instance_lock:
                if not hasattr(Test3, '_instance'):
                    Test3._instance = Test3(*args, **kwargs)
        return Test3._instance


def test3(arg):
    obj = Test3.get_instance()
    print(obj, '\n')


for i in range(10):
    task = threading.Thread(target=test3, args=[i, ])
    task.start()
time.sleep(2)
obj = Test3.get_instance()
print(obj)


# 方法4：基于__new__方法，弥补方法3无法通过__init__实例化的问题
class Test4:
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Test4, '_instance'):
            with Test4._instance_lock:
                if not hasattr(Test4, '_instance'):
                    Test4._instance = object.__new__(cls)
        return Test4._instance


obj1 = Test4()
obj2 = Test4()
print(obj1, obj2)


def task4(arg):
    obj = Test4()
    print(obj)


for i in range(10):
    t = threading.Thread(target=task4, args=[i, ])
    t.start()


# 方法5：metaclass
class SingletonType(type):
    def __init__(self, *args, **kwargs):
        super(SingletonType, self).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):  # 这里的cls，即Foo类
        print('cls', cls)
        obj = cls.__new__(cls, *args, **kwargs)
        cls.__init__(obj, *args, **kwargs)  # Foo.__init__(obj)
        return obj


class Foo(metaclass=SingletonType):  # 指定创建Foo的type为SingletonType
    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)


obj = Foo('xx')
