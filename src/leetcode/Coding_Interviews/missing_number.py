# -*- coding: utf-8 -*-

from typing import List


class Solution:

    @staticmethod
    def missing_number(nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1

        return left


if __name__ == '__main__':
    test_solution = Solution()
    print(test_solution.missing_number([0, 1, 2, 3, 5, 6, 7]))
