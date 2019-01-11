# 书上案例，从所有朋友关系（这种关系以图的形式表现）中找到最近的橘子经销商
# 图用字典里存列表的方式实现

from collections import deque  # 队列
graph = {
    'you': ['alice', 'bob', 'claire'],
    'bob': ['anuj', 'peggy'],
    'alice': ['peggy'],
    'claire': ['jonny', 'thom'],
    'anuj': [],
    'peggy': [],
    'jonny': [],
    'thom': [],
}


def is_the_one(name):
    if int(str(hash(name))[-1]) % 9 == 0:
        return True
    else:
        return False


def search(name):
    target = deque()
    target += graph[name]  # 从一度关系开始搜索
    black_list = list()
    while target:
        print('the quene:', target)
        this_target = target.popleft()
        if is_the_one(this_target):
            return 'we\'ve got it: ' + this_target
        elif this_target in black_list:
            continue
        else:
            target += graph[this_target]
            black_list.append(this_target)
    return('no result')


print(search('you'))
