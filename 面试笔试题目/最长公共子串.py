def LCstring(string1, string2):
    len1 = len(string1)
    len2 = len(string2)
    res = [[0 for i in range(len1+1)] for j in range(len2+1)]
    result = 0
    results = []
    for i in range(1, len2+1):
        for j in range(1, len1+1):
            if string2[i-1] == string1[j-1]:
                res[i][j] = res[i-1][j-1]+1
                if res[i][j] > result:
                    results = [(j-1, i-1)]
                    result = res[i][j]
                elif res[i][j] == result:
                    results.append((j-1, i-1))
    result_strings = []
    for point in results:
        result_str = ''
        for t in range(result):
            result_str = string1[point[0]-t]+result_str
        result_strings.append(result_str)
    result_strings.sort()
    for r in result_strings:
        print(r)


LCstring('zeqrbe', 'zeearbb')
