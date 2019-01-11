# 解决有向无环图（权重非负）的最小权重问题
from copy import deepcopy
inf = float('inf')
# 用字典套字典的方式实现有向有权图：书上P108
graph = {
    'start': {
        'a': 6,
        'b': 2,
    },
    'a': {
        'end': 1
    },
    'b': {
        'end': 5,
        'a': 3
    },
    'end': {}
}

# 存储从起点到各节点的cost。算法的核心就是不断优化这个字典。
final_costs = {
    'a': 6,
    'b': 2,
    'end': inf
}

# 存储最短路径对应的父节点
parents = {
    'a': 'start',
    'b': 'start',
    'end': ''
}

# 记录已经优化过的节点
processed = ['start', 'end']


def get_next_node():
    # sorted的参数如果是字典，返回的是key；参数如果是items()，返回tuple
    unprocessed = sorted({key: value for key, value in final_costs.items() if key in list(
        final_costs.keys() - processed)}, key=lambda x: final_costs[x])
    if not unprocessed:
        return False
    return unprocessed[0]


def dikstla_search():
    while get_next_node():
        this_node = get_next_node()
        this_node_neighbor = graph[this_node].keys()
        for i in this_node_neighbor:    # i 是所有邻居节点中的一个比如a,b
            if graph[this_node][i] + final_costs[this_node] < final_costs[i]:
                final_costs[i] = graph[this_node][i] + final_costs[this_node]
                parents[i] = this_node
        processed.append(this_node)


def show_shortest_path():
    order_list = list(['end'])
    for t in range(len(parents)):
        order_list.append(parents[order_list[t]])
    order_list.reverse()
    print(order_list)


dikstla_search()
show_shortest_path()
