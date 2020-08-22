import sys


def main():
    # 当前坐标
    C = 0
    # 已经走过的坐标
    F = set()
    # 结果，糖果数量
    R = 0

    _, k = sys.stdin.readline().strip().split()
    commands = sys.stdin.readline().strip()
    for _ in range(int(k)):
        for command in commands:
            if command == 'L':
                C -= 1
            elif command == "R":
                C += 1
            if C not in F:
                R += abs(C)
    print(R)


if __name__ == '__main__':
    main()
