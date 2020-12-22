import collections


class LRUCache:
    def __init__(self, size):
        self.cache = {}
        self.keys = []
        self.size = size

    def get(self, key):
        if key in self.cache:
            self.keys.remove(key)
            self.keys.insert(0, key)
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        if key in self.cache:
            self.keys.remove(key)
            self.keys.insert(0, key)
            self.cache[key] = value
        elif len(self.keys) == self.size:
            old = self.keys.pop()
            self.cache.pop(old)
            self.keys.insert(0, key)
            self.cache[key] = value
        else:
            self.keys.insert(0, key)
            self.cache[key] = value


c = int(input())
l_c = LRUCache(c)
while True:
    s = input()
    s_list = s.split()
    if s != '' and len(s_list) == 2:
        l_c.put(s_list[0], s_list[1])
    elif s != '' and len(s_list) == 1:
        l_c.get(s_list[0])
    else:
        for k in list(l_c.cache.keys())[:: -1]:
            print(k, l_c.cache[k])
        break
