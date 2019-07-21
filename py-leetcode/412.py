from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = list()
        for i in range(1, n+1):
            three = i % 3
            five = i % 5
            if not three and not five:
                result.append("FizBuzz")
            elif not three and five:
                result.append('Fiz')
            elif not five and three:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
