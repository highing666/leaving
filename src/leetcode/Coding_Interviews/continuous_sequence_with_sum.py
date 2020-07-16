# -*- coding: utf-8 -*-

from typing import List


class Solution:

    @staticmethod
    def find_continuous_sequence(target: int) -> List[List[int]]:
        result = []
        l, r = 1, 2
        while l < r:
            temp_sum = (l + r) * (r - l + 1) / 2
            if temp_sum == target:
                result.append([i for i in range(l, r + 1)])
                l += 1
            elif temp_sum < target:
                r += 1
            else:
                l += 1

        return result


if __name__ == '__main__':
    test_solution = Solution()
    print(test_solution.find_continuous_sequence(15))
