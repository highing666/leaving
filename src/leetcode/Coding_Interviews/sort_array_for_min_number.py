# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def min_number(self, nums: List[int]) -> str:
        str_nums = [str(num) for num in nums]
        sorted_nums = self.quick_sort(str_nums)

        return ''.join(sorted_nums)

    def quick_sort(self, collection: List[str]) -> List[str]:
        length = len(collection)
        if length <= 1:
            return collection
        else:
            pivot = collection.pop()
            greater, lesser = [], []
            for element in collection:
                if element + pivot > pivot + element:
                    greater.append(element)
                else:
                    lesser.append(element)
            return self.quick_sort(lesser) + [pivot] + self.quick_sort(greater)


if __name__ == '__main__':
    test_solution = Solution()
    test_arr = [3, 30, 34, 5, 9]
    print(test_solution.min_number(test_arr))
