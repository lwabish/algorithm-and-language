stations = {
    'kone': set(['id', 'nv', 'ut']),
    'ktwo': set(['wa', 'id', 'mt']),
    'kthree': set(['or', 'nv', 'ca']),
    'kfour': set(['nv', 'ut']),
    'kfive': set(['ca', 'az'])
}

# 类似于列表生成式，集合生成式
all_states = {i for t in stations.values() for i in t}

final_station, covered_state = set(), set()
while covered_state != all_states:
    best_choice = None
    best_choice_new_count = 0
    for station, value in stations.items():
        new_covered_state = value - covered_state
        if len(new_covered_state) > best_choice_new_count:
            best_choice = station
            best_choice_new_count = len(new_covered_state)
            print(best_choice, new_covered_state)
    # 集合不能像列表用+，要用 |
    covered_state = covered_state | stations[best_choice]
    final_station.add(best_choice)

print(final_station)
# 结果是集合，无序
