from typing import List
tcs = [
    (["flower", "flow", "flight"],),
    (["dog", "racecar", "car"],),
    (['abcde', 'a'],),
    ([],),
    (['aa', 'ab'],),
    (['ca', 'a'],),
]


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        def is_common(s):
            for str in strs:
                if str[:len(s)] != s:
                    return False
            return True

        def get_shortest(l):
            least_index = -1
            least_len = float('inf')
            for i, string in enumerate(l):
                if len(string) < least_len:
                    least_len = len(string)
                    least_index = i
            return l[least_index]
        shortest_str = get_shortest(strs)

        def half_try(s, lcp):
            if is_common(lcp+s):
                lcp += s
                return lcp
            elif len(s) == 1:
                return lcp
            mid_index = int(len(s) / 2)
            left_str = s[:mid_index]
            l_lcp = half_try(left_str, lcp)
            right_str = s[mid_index:]
            r_lcp = half_try(right_str, l_lcp)
            return r_lcp

        return half_try(shortest_str, '')


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.longestCommonPrefix(*tc))
