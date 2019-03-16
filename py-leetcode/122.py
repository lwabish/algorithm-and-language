tc = [
    [7, 1, 5, 3, 6, 4],
]


def main(prices: list):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += (prices[i]-prices[i-1])
    return profit


if __name__ == '__main__':
    for i in tc:
        print(main(i))
