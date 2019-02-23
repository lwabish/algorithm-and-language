tc = 1
tc = 2
tc = 4
tc = 0


def main(numRows: 'int') -> 'List[List[int]]':
    res = list([[1], [1, 1]])
    if numRows == 1:
        return res[:1]
    elif numRows == 2:
        return res
    elif numRows == 0:
        return []
    for i in range(1, numRows-1):
        new_line = [1] + [0] * i + [1]
        for j in range(1, i + 1):
            new_line[j] = res[-1][j - 1] + res[-1][j]
        res.append(new_line)
    return res


if __name__ == '__main__':
    print(main(tc))
