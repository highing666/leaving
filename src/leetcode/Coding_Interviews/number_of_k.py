# -*- coding: utf-8 -*-

from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        return self.helper(nums, target) - self.helper(nums, target - 1)

    @staticmethod
    def helper(nums: List[int], n: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] <= n:
                i = m + 1
            else:
                j = m - 1
        return i


if __name__ == '__main__':
    test_solution = Solution()
    print(test_solution.search([5, 7, 7, 8, 8, 10], 8))
    print(test_solution.search([], 9))
