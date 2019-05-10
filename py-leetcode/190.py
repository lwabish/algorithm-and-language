from typing import List
tcs = [
    (0b00000010100101000001111010011100,),
    (0b11111111111111111111111111111101,),
]


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary_str = bin(n)[2:]
        filled_str = binary_str.zfill(32)
        result_str = filled_str[::-1]
        return int(result_str, 2)


if __name__ == '__main__':
    solution = Solution()
    for tc in tcs:
        print(solution.reverseBits(*tc))
