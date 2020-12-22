m = 21
coins = [1, 2, 5, 10]
# coins = [2, 4]
coins.sort()


def find_combination(n):
    res = list()

    def check(n):
        for i in range(len(coins) - 1, -1, -1):
            if coins[i] <= n:
                res.append(coins[i])
                delta = n - coins[i]
                check(delta)
                return
    check(n)
    if sum(res) != n:
        return -1
    return len(res)
    # return res


def main(m):
    counts = list()
    for i in range(1, m + 1):
        res = find_combination(i)
        if res != -1:
            counts.append(res)
        else:
            return -1
    return max(counts)


if __name__ == '__main__':
    print(main(m))
