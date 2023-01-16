tc = {
    1: 4,
    0: 2,
    3: 1,
    -4: 6
}
# sort by key


def sort_by_key(d):
    return {k: d[k] for k in sorted(d)}


def sort_by_value(d):
    return {k: d[k] for k in sorted(d, key=lambda x: d[x])}


if __name__ == '__main__':
    print(sort_by_key(tc))
    print(sort_by_value(tc))
