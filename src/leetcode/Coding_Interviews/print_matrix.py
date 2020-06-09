# -*- coding: utf-8 -*-


class Solution:

    def spiral_order(self, matrix):
        if not matrix:
            return []

        start = 0
        rows = len(matrix)
        columns = len(matrix[0])
        results = list()

        while columns > start * 2 and rows > start * 2:
            results += self.print_matrix_in_circle(matrix, columns, rows, start)
            start += 1

        return results

    @staticmethod
    def print_matrix_in_circle(matrix, columns, rows, start):
        end_x = columns - 1 - start
        end_y = rows - 1 - start

        results = list()

        for i in range(start, end_x + 1):
            results.append(matrix[start][i])
            print(matrix[start][i])

        if start < end_y:
            for i in range(start + 1, end_y + 1):
                results.append(matrix[i][end_x])
                print(matrix[i][end_x])

        if start < end_x and start < end_y:
            for i in range(end_x - 1, start - 1, -1):
                results.append(matrix[end_y][i])
                print(matrix[end_y][i])

        if start < end_x and start < end_y - 1:
            for i in range(end_y - 1, start, -1):
                results.append(matrix[i][start])
                print(matrix[i][start])

        return results


if __name__ == '__main__':
    test_numbers = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    test_solution = Solution()
    test_solution.spiral_order(test_numbers)
