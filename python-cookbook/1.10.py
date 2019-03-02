# 元素去重

# 1.简单去重，不要求顺序
a = [1, 1, 2, 3, 3]
a = set(a)
print(a)


# 2.hashable，不乱序去重
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


# 3.unhashable,不乱序去重
def dedupe_better(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
