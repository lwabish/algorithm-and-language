tc = 2


def main(n):
    results = list([1, 2])
    if n < 3:
        return results[n-1]
    while len(results) < n:
        results.append(results[-1]+results[-2])
    return results[-1]


if __name__ == '__main__':
    print(main(tc))
