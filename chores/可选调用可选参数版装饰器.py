import functools
import time
from inspect import isfunction


def print_used_time1(show_params=True):
    """
    这一版本的特点是，当不调用直接使用时，函数被传进来，当成了show_param参数，可以正常运行，但是show_param的默认值True被顶掉了。
    巧合之处在于这个装饰器内部对于show_param这个参数True False的判断逻辑并不会因此而发生错误，实属巧合。
    """
    def decorator(func, *args, **kwargs):
        @functools.wraps(func)
        def clocked(*args, **kwargs):
            t0 = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - t0
            name = func.__name__
            if show_params:
                arg_list = list()
                if args:
                    # obj==eval(repr(obj)),str()函数将对象转为字符串后不一定可逆
                    arg_list.append(','.join(repr(arg) for arg in args))
                if kwargs:
                    pairs = ['%s=%r' % (k, w)
                             for k, w in sorted(kwargs.items())]
                    arg_list.append(','.join(pairs))
                    # print(arg_list)
                arg_str = ','.join(arg_list)
                print('[%0.8fs] %s(%s) -> %r' %
                      (elapsed, name, arg_str, result))
            else:
                print('[%0.8fs] %s() -> %r' % (elapsed, name, result))
            # print(show_params)
            return result
        return clocked
    if type(show_params) == bool:
        return decorator
    elif isfunction(show_params):
        return decorator(show_params)


def print_used_time2(funcq=None, show_params=True):
    """
    该版本的特点是不会发生参数覆盖问题，但是在装饰器提供参数时，提供的是一个可选参数，所以提供时必须写参数名，不能直接提供值调用。
    """
    def decorator(func):
        @functools.wraps(func)
        def clocked(*args, **kwargs):
            t0 = time.time()
            print(funcq)
            result = func(*args, **kwargs)
            elapsed = time.time() - t0
            name = func.__name__
            if show_params:
                arg_list = list()
                if args:
                    # obj==eval(repr(obj)),str()函数将对象转为字符串后不一定可逆
                    arg_list.append(','.join(repr(arg) for arg in args))
                if kwargs:
                    pairs = ['%s=%r' % (k, w)
                             for k, w in sorted(kwargs.items())]
                    arg_list.append(','.join(pairs))
                    # print(arg_list)
                arg_str = ','.join(arg_list)
                print('[%0.8fs] %s(%s) -> %r' %
                      (elapsed, name, arg_str, result))
            else:
                print('[%0.8fs] %s() -> %r' % (elapsed, name, result))
            # print(show_params)
            return result
        return clocked
    if funcq:
        return decorator(funcq)
    else:
        return decorator


def log(text='nonename'):
    """
    方案3：最正常的逻辑：判断最外层的参数是你str还是函数。str说明提供了参数，否则说明没有提供参数，然后根据判断结果分别写两个装饰器即可。
    """
    if isinstance(text, str):
        # 三层带参数版装饰器
        def decortaor(func):
            @functools.wraps(func)
            def wrapper(args, **kw):
                print('%s %s():' % (text, func.name))
                return func(args, kw)
            return wrapper
        return decortaor
    else:
        # 普通无参数版装饰器
        @functools.wraps(text)
        def wrapper(*args, kw):
            print('call %s():' % text.name)
            return text(args, *kw)
        return wrapper


# 测试采用方法2，可选参数不给名字直接提供时，会被当成第一个可选参数
@print_used_time2(False)
def test1(a):
    pass


test1 = print_used_time2(True)()
# @print_used_time1()
# def test2(a):
#     pass


# @print_used_time1
# def test3(a, **kwargs):
#     pass


if __name__ == '__main__':
    test1(1)
    # test2(2)
    # test3(3, abc='def')
