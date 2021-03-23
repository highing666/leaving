# -*- coding: utf-8 -*-

from typing import List


class Solution:

    @staticmethod
    def move_zeroes(nums: List[int]) -> None:
        if not nums:
            return 0

        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        print(nums)


if __name__ == '__main__':
    test_l = [0, 1, 0, 3, 12]
    test_solution = Solution()
    test_solution.move_zeroes(test_l)
