# -*- coding: utf-8 -*-

class Solution1:

    def min_array(self, numbers: list) -> int:
        index1 = 0
        index2 = len(numbers) - 1
        index_mid = index1
        while numbers[index1] >= numbers[index2]:
            if index2 - index1 == 1:
                index_mid = index2
                break

            index_mid = int((index1 + index2) / 2)
            if numbers[index1] == numbers[index2] == numbers[index_mid]:
                return self.min_in_order(numbers)
            if numbers[index_mid] >= numbers[index1]:
                index1 = index_mid
            elif numbers[index_mid] <= numbers[index2]:
                index2 = index_mid
        
        return numbers[index_mid]
    
    def min_in_order(self, numbers):
        result = numbers[0]
        for item in numbers:
            if result > item:
                result = item
        
        return result


class Solution2:

    def min_array(self, numbers: [int]) -> int:
        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]:
                i = m + 1
            elif numbers[m] < numbers[j]:
                j = m
            else:
                j -= 1
        return numbers[i]


if __name__ == "__main__":
    test_list1 = [3, 4, 5, 6, 7, 1, 2]
    test_list2 = [1, 0, 1, 1, 1]
    solution_test = Solution2()
    print(solution_test.min_array(test_list1))
    print(solution_test.min_array(test_list2))
