# -*- coding: utf-8 -*-

from functools import reduce
from typing import List


class Solution:

    @staticmethod
    def single_numbers(nums: List[int]) -> List[int]:
        result = reduce(lambda x, y: x ^ y, nums)
        div = 1
        while div & result == 0:
            div <<= 1
        a, b = 0, 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n

        return [a, b]


if __name__ == '__main__':
    test_solution = Solution()
    print(test_solution.single_numbers([1, 2, 10, 4, 1, 4, 3, 3]))
