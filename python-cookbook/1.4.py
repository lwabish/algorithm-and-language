# 查找topN个元素
# heapq的nlargest nsmallest方法适用于N>1且较小时
import heapq

nums = [1, 8, 2, 7, -4]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

# 当元素是复杂解构时，可以指定比较的key
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(heapq.nlargest(3, portfolio, key=lambda x: x['shares']))


# heapq原理：在底层实现里面，首先会先将集合数据进行堆排序后放入一个列表中。
# 堆数据结构最重要的特征是 heap[0] 永远是最小的元素
a_list = [8, 3, 4, 10, 2, -2]
print(type(a_list))
print(a_list)
# heapify将list变为堆list
heapq.heapify(a_list)
# type并没有变
print(type(a_list))
# 但是第一个已经是最小的了
print(a_list)

# 弹出第一个（最小的），并且再把最小的放到第一个（堆排序）
a, b = heapq.heappop(a_list), heapq.heappop(a_list)
print(a, b)
