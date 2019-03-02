prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 对字典的值进行数据操作
# 默认对字典的操作会对应到key上
# 使用zip函数将字典的键值反过来,变成一个值在前键在后的tuple，对数据进行操作的时候就基于值了。
# 主要：zip返回的是一个类似生成器的对象，只能用一次

min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
