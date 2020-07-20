# -*- coding: utf-8 -*-

from typing import List


class Solution:

    @staticmethod
    def find_continuous_sequence(target: int) -> List[List[int]]:
        result = []
        left, right = 1, 2
        while left < right:
            temp_sum = (left + right) * (right - left + 1) / 2
            if temp_sum == target:
                result.append([i for i in range(left, right + 1)])
                left += 1
            elif temp_sum < target:
                right += 1
            else:
                left += 1

        return result


if __name__ == '__main__':
    test_solution = Solution()
    print(test_solution.find_continuous_sequence(15))
