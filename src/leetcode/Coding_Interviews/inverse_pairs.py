# -*- coding: utf-8 -*-

from typing import List


class Solution:
    
    def reverse_pairs(self, nums: List[int]) -> int:
        size = len(nums)
        if not nums:
            return 0

        temp = [0] * size

        return self.count_reverse_pairs(nums, 0, size - 1, temp)

    def count_reverse_pairs(self, nums: List[int], left: int, right: int, temp: List[int]):
        if left == right:
            return 0
        mid = (left + right) >> 1
        left_pairs = self.count_reverse_pairs(nums, left, mid, temp)
        right_pairs = self.count_reverse_pairs(nums, mid + 1, right, temp)

        reverse_pairs = left_pairs + right_pairs

        if nums[mid] <= nums[mid + 1]:
            return reverse_pairs
        
        reverse_cross_pairs = self.merge_and_count(nums, left, mid, right, temp)

        return reverse_pairs + reverse_cross_pairs
    
    def merge_and_count(self, nums: List[int], left: int, mid: int, right: int, temp: List[int]):
        for i in range(left, right + 1):
            temp[i] = nums[i]

        i = left
        j = mid + 1
        result = 0
        for k in range(left, right + 1):
            if i > mid:
                nums[k] = temp[j]
                j += 1
            elif j > right:
                nums[k] = temp[i]
                i += 1
            elif temp[i] <= temp[j]:
                nums[k] = temp[i]
                i += 1
            else:
                nums[k] = temp[j]
                j += 1
                result += (mid - i + 1)
        
        return result


if __name__ == "__main__":
    
    test_solution = Solution()
    print(test_solution.reverse_pairs([7, 5, 6, 4]))
    print(test_solution.reverse_pairs([]))
