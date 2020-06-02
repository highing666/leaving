# -*- coding: utf-8 -*-


def exchange(nums: [int]) -> [int]:
    if len(nums) == 0:
        return nums

    p_begin = 0
    p_end = len(nums) - 1

    while p_begin < p_end:
        while p_begin < p_end and nums[p_begin] & 0x1 != 0:
            p_begin += 1

        while p_begin < p_end and nums[p_end] & 0x1 == 0:
            p_end -= 1

        if p_begin < p_end:
            temp = nums[p_begin]
            nums[p_begin] = nums[p_end]
            nums[p_end] = temp

    return nums


if __name__ == '__main__':
    print(exchange([1, 2, 3, 4, 5]))
    print(exchange([1, 3, 5, 7, 2, 4, 6, 8]))
    print(exchange([2, 4, 6, 8, 1, 3, 5, 7]))
    print(exchange([]))
