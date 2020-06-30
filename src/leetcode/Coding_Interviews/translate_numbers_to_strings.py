# -*- coding: utf-8 -*-


class Solution:

    def translate_num(self, num: int) -> int:
        a = 1
        b = 1
        y = num % 10
        while num != 0:
            num //= 10
            x = num % 10
            if 10 <= 10 * x + y <= 25:
                c = a + b
            else:
                c = a
            a, b = c, a
            y = x
            
        return a


if __name__ == "__main__":
    test_solution = Solution()
    print(test_solution.translate_num(12258))
