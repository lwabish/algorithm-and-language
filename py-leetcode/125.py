# 字母数字是否已经是回文串
tc = [
    "A man, a plan, a canal: Panama",
    "race a car",
]


def main(s: str):
    s = ''.join(filter(lambda x: x.isalnum(), s)).lower()
    return s == s[::-1]


if __name__ == '__main__':
    for i in tc:
        print(main(i))
