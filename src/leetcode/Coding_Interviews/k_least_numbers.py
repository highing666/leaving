# -*- coding: utf-8 -*-


def get_least_numbers(arr: [int], k: int) -> [int]:
    nums = [0] * 10000
    for a in arr:
        nums[a] += 1
    
    output = []
    i = 0
    while len(output) < k:
        if nums[i] >= 1:
            for j in range(nums[i]):
                output.append(i)
        i += 1

    return output[:k]
