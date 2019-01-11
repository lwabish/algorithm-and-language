tc = 'MCMXCIV'


def main(s):
    sum = 0
    t = 0
    while t < len(s):
        # print(t)
        # print(s[t:t+2])
        if s[t:t + 2] == 'IV':
            sum += 4
            t += 2
            continue
        elif s[t:t + 2] == 'IX':
            sum += 9
            t += 2
            continue
        elif s[t:t + 2] == 'XL':
            sum += 40
            t += 2
            continue
        elif s[t:t + 2] == 'XC':
            sum += 90
            t += 2
            continue
        elif s[t:t + 2] == 'CD':
            sum += 400
            t += 2
            continue
        elif s[t:t + 2] == 'CM':
            sum += 900
            t += 2
            continue
        elif s[t:t + 1] == 'I':
            sum += 1
        elif s[t:t + 1] == 'V':
            sum += 5
        elif s[t:t + 1] == 'X':
            sum += 10
        elif s[t:t + 1] == 'L':
            sum += 50
        elif s[t:t + 1] == 'C':
            sum += 100
        elif s[t:t + 1] == 'D':
            sum += 500
        elif s[t:t + 1] == 'M':
            sum += 1000
        t += 1
    return sum


if __name__ == '__main__':
    print(main(tc))
