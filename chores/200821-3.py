def judge(n):
    if not n & (n-1):
        result = "true"
    else:
        result = "false"
    return result


print(judge(1023))
