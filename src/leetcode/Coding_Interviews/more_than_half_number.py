# -*- coding: utf-8 -*-


class Solution:

    def majorityElement(self, nums: [int]) -> int:
        votes = 0
        for num in nums:
            if votes == 0:
                x = num
            if num == x:
                votes += 1
            else:
                votes -= 1
        
        return x


if __name__ == "__main__":
    test_nums = [1, 2, 3, 2, 3, 4, 2, 2, 4, 2]
    test_solution = Solution()
    print(test_solution.majorityElement(test_nums))
