import sys


def fetch_water(x, y, z):
    if x == z or y == z:
        return 'true'
    elif x+y == z:
        return 'true'
    elif max([x, y])-min([x, y]) == z:
        return 'true'
    else:
        return 'false'


for line in sys.stdin:
    a = map(lambda x: int(x), line.split())
    print(fetch_water(*a))
