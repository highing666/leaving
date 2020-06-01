# -*- coding: utf-8 -*-


class Solution:

    def __init__(self, p):
        self.p = p

    def is_number(self, s: str) -> bool:
        s = s.strip()
        if s == '':
            return False

        numeric = self.scan_integer(s)

        if self.p > len(s) - 1:
            return numeric

        if self.p < len(s) and s[self.p] == '.':
            self.p += 1
            if self.p > len(s) - 1:
                return numeric
            numeric = self.scan_unsigned_integer(s) or numeric

        if self.p < len(s) and s[self.p] in ['e', 'E']:
            self.p += 1
            if self.p > len(s) - 1:
                return False
            numeric = numeric and self.scan_integer(s)

        if self.p < len(s):
            return False

        return numeric

    def scan_unsigned_integer(self, s):
        before = self.p
        while self.p < len(s) and '0' <= s[self.p] <= '9':
            self.p += 1

        return self.p > before

    def scan_integer(self, s):
        if s[self.p] in ['+', '-']:
            self.p += 1

        return self.scan_unsigned_integer(s)


if __name__ == '__main__':
    test_solution = Solution(0)
    print(test_solution.is_number('123.'))
