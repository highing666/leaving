# -*- coding: utf-8 -*-

from typing import List


class Solution:

    def search_insert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = n
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if target <= nums[mid]:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
    
        return res
