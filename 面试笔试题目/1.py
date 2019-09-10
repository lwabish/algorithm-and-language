import sys


def smaller_count(n):
    def do(x):
        if x <= n:
            return True
        else:
            return False
    return do


def get_percent(n):
    global scores
    smaller_n = len(list(filter(smaller_count(scores[n-1]), scores)))
    return (smaller_n-1)/len(scores)*100


if __name__ == "__main__":
    # n = int(sys.stdin.readline().strip())  # 总人数
    n = 3

    # line = sys.stdin.readline().strip()
    # scores = list(map(int, line.split()))   # 分数
    scores = [100, 98, 90]
    # q = int(sys.stdin.readline().strip())   #询问次数
    q = 3

    for i in range(q):
        result = get_percent(2)
        # print("{:%.6f}".format(result))
        print("%.6f" % result)
