tc = 4
tc = 0
tc = 1
tc = 2


def main(rowIndex: 'int'):
    def factorial(n):
        if n == 1 or n == 0:
            return 1
        return n*factorial(n-1)
    if rowIndex == 0:
        return [1]
    res = list()
    up = factorial(rowIndex)
    for t in range(rowIndex+1):
        down = factorial(t)*factorial(rowIndex-t)
        res.append(int(up / down))
    return res


if __name__ == '__main__':
    print(main(tc))
