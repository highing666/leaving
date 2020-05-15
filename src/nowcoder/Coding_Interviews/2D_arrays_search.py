# -*- coding: utf-8 -*-

class Solution:

    def find(self, target, array):
        if len(array) == 0 or len(array[0]) == 0:
            return False

        for i in range(1, len(array) + 1):
            for j in range(len(array[0])):
                if array[-i][j] < target:
                    continue
                elif array[-i][j] > target:
                    break
                else:
                    return True
        
        return False


if __name__ == "__main__":
    test_l = [
        [1, 2, 3, 4, 5],
        [4, 5, 6, 7, 8],
        [5, 7, 8, 9, 10],
        [7, 8, 9, 10, 11]
    ]
    solution1 = Solution()
    print(solution1.find(1, test_l))
    