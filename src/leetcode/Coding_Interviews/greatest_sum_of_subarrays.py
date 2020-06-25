# -*- coding: utf-8 -*-

from typing import List


def max_sub_array(nums: List[int]) -> int:
    if not nums:
        return 0
    
    cur_sum = 0
    greatest_sum = int('-inf')
    for i in range(0, len(nums)):
        if cur_sum <= 0:
            cur_sum = nums[i]
        else:
            cur_sum += nums[i]

        if cur_sum > greatest_sum:
            greatest_sum = cur_sum
    
    return greatest_sum


if __name__ == "__main__":
    arr1 = [1, -2, 3, 10, -4, 7, 2, -5]
    print(max_sub_array(arr1))
