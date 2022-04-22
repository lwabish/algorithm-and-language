import json
import os


def main():
    with open("零散/20220422.json", "r") as f:
        data = json.load(f)
        for k, v in data.items():
            # print(k, v)
            print()
            scores = sorted(v.items(), key=lambda x: x[1])
            score_list = list(map(lambda x: x[1], scores))
            for _, j in enumerate(scores):
                score = j[1]
                # list.index()可以优雅地实现并列排名
                print(k, j[0], score_list.index(score)+1)


if __name__ == "__main__":
    main()
