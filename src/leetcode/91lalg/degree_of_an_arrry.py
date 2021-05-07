# -*- coding: utf-8 -*-

from typing import List


class Solution:

    def find_shortest_sub_array(self, nums: List[int]) -> int:
        mp = dict()

        for i, num in enumerate(nums):
            if num in mp:
                mp[num][0] += 1
                mp[num][2] = i
            else:
                mp[num] = [1, i, i]
        
        max_num = min_len = 0
        for count, left, right in mp.values():
            if max_num < count:
                max_num = count
                min_len = right - left + 1
            elif max_num == count:
                if min_len > (span := right - left + 1):
                    min_len = span

        return min_len
