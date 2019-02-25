# 算法原理：埃氏筛法(用自然数序列的第一项作除数去筛掉后面的数，每筛选一轮，序列头部的数就是下一个质数)。练习生成器和filter函数。

tc = 5


def prime_generator():

    # (3,5,7……)从3开始往后筛
    def _odd_iterator():
        n = 1
        while True:
            n += 2
            yield n

    # 第一个质数
    yield 2
    # 初始化序列
    numbers = _odd_iterator()
    while True:
        # 返回这一轮的质数
        this_prime = next(numbers)
        yield this_prime
        # 用这个质数去筛选后面所有的数
        numbers = filter(lambda x: x % this_prime != 0, numbers)


if __name__ == '__main__':
    # 注意：函数里有yield后变成了生成器的生成器，需要执行一次，才会返回一个generator。之后对返回值调用next。
    g = prime_generator()
    # print(type(g))
    for t in range(tc):
        print(next(g))
