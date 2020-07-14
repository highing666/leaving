# -*- coding: utf-8 -*-

from typing import List


class Solution:

    @staticmethod
    def single_number(nums: List[int]) -> int:
        counts = [0] * 32
        for num in nums:
            for j in range(32):
                counts[j] += num & 1
                num >>= 1

        result, m = 0, 3
        for i in range(32):
            result <<= 1
            result |= counts[31 - i] % m

        return result if counts[31] % m == 0 else -(result ^ 0xffffffff)


if __name__ == '__main__':
    test_solution = Solution()
    print(test_solution.single_number([2, 4, 2, 2]))
