from typing import List
tcs = [
    (["eat", "tea", "tan", "ate", "nat", "bat"],),
]


# 哈希
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in m:
                m[key] += [s]
            else:
                m[key] = [s]
        return [v for v in m.values()]


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.groupAnagrams(*tc))
