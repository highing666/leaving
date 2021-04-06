# -*- coding: utf-8 -*-

from typing import List

class Solution:

    def add_to_array_form(self, num: List[int], k: int) -> List[int]:
        total = 0
        dig = len(num) - 1

        for n in num:
            total += n * (10 ** dig)
            dig -= 1
        total += k

        result = []
        while total > 9:
            temp = total % 10
            result.insert(0, temp)
            total //= 10
        result.insert(0, total)
        
        return result


if __name__ == '__main__':
    solution = Solution()
    arr = [1, 2, 0, 0]
    test_k  = 34

    print(solution.add_to_array_form(arr, test_k))
