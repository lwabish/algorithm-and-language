import sys
from datetime import datetime, timedelta


def parse_log(log):
    log_s = list(map(lambda x: x.strip(), log.split('|')))
    t = log_s[0].split()[0].split(
        '-')+log_s[0].split()[1].split(',')[0].split(':')+[log_s[0].split()[1].split(',')[1]]
    t = list(map(lambda x: int(x), t))
    t[6] *= 1000
    return datetime(*t), log_s[3], log_s[4], log_s[6]


def show_result(result):
    if not result:
        print('none')
    ordered_class_name = sorted(list(result.keys()))
    for c in ordered_class_name:
        print(c+':')
        defs = result[c]
        ordered_def_name = sorted(list(defs.keys()))
        for d in ordered_def_name:
            time_spent = defs[d][-1]-defs[d][0]
            print(d+','+str(int(time_spent.microseconds/1000)))
        print()


def main():
    result = dict()
    while True:
        l = sys.stdin.readline().strip()
        if not l:
            break
        t, class_name, def_name, event = parse_log(l)
        # print(t, class_name, def_name, event)
        if '[ENTER]' in event:
            if class_name not in result:
                result[class_name] = dict()
                result[class_name][def_name] = [t]
            elif def_name not in result[class_name]:
                result[class_name][def_name] = [t]
            else:
                continue
        elif '[EXIT]' in event:
            result[class_name][def_name].append(t)
    show_result(result)


if __name__ == '__main__':
    main()
