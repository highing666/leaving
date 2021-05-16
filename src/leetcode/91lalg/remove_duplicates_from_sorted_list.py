# -*- coding: utf-8 -*-

from typing import List


class Solution:

    def remove_duplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        l = r = 1
        while r < n:
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
            r += 1
        
        return l
