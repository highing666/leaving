# -*- coding: utf-8 -*-

class Solution:

    def fib(self, n: int) -> int:
        a = 0
        b = 1

        for _ in range(n):
            a, b = b, a + b
        
        return a % 1000000007


if __name__ == "__main__":
    test1 = Solution()
    print(test1.fib(5))
