# -*- coding: utf-8 -*-


class Solution:

    def __init__(self):
        self.result = []

    def print_1_to_max_of_n_digits(self, n: int) -> [int]:
        if n <= 0:
            return

        number = ['0'] * n

        for i in range(10):
            number[0] = chr(ord('0') + i)
            self.print_1_to_max_of_n_digits_recursively(number, n, 0)

        return self.result[1:]

    def print_1_to_max_of_n_digits_recursively(self, number, length, index):
        if index == length - 1:
            self.print_number(number)
            self.result.append(int(''.join(number)))
            return

        for i in range(10):
            number[index + 1] = chr(ord('0') + i)
            self.print_1_to_max_of_n_digits_recursively(number, length, index + 1)

    @staticmethod
    def print_number(number):
        number = int(''.join(number))
        if number != 0:
            print(number)


if __name__ == '__main__':
    test_solution = Solution()
    test_solution.print_1_to_max_of_n_digits(1)
    print(test_solution.result)
