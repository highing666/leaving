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

        products = list(range(n + 1))
        products[0] = 0
        products[1] = 1
        products[2] = 2
        products[3] = 3

        for i in range(4, n + 1):
            max_v = 0
            for j in range(1, i // 2 + 1):
                product = products[j] * products[i - j]
                if max_v < product:
                    max_v = product
                products[i] = max_v

        max_v = products[n]

        return max_v


if __name__ == '__main__':
    test_solution = Solution
    print(test_solution.cutting_rope(8))
