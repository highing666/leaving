# -*- coding: utf-8 -*-


class Solution:

    @staticmethod
    def cutting_rope(n: int) -> int:
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2

        times_of_3 = n // 3
        if n - times_of_3 * 3 == 1:
            times_of_3 -= 1

        times_of_2 = (n - times_of_3 * 3) / 2

        return int(3 ** times_of_3) * int(2 ** times_of_2) % 1000000007


if __name__ == '__main__':
    test_solution = Solution
    print(type(test_solution.cutting_rope(120)))
    print(test_solution.cutting_rope(120))
