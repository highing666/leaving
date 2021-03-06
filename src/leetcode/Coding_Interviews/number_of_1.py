# -*- coding: utf-8 -*-


class Solution:

    def countDigitOne(self, n: int) -> int:
        digit, result = 1, 0
        high, cur, low = n // 10, n % 10, 0
        while high != 0 or cur != 0:
            if cur == 0:
                result += high * digit
            elif cur == 1:
                result += high * digit + low + 1
            else:
                result += (high + 1) * digit
            
            low += cur * digit
            cur = high % 10
            high //= 10
            digit *= 10
        
        return result


if __name__ == "__main__":
    solution = Solution()
    test_num = 12344
    print(solution.countDigitOne(test_num))
        