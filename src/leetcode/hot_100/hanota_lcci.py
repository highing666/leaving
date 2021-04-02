# -*- coding: utf-8 -*-

from typing import List

class Solution:

    def hanota(self, a: List[int], b: List[int], c: List[int]) -> None:
        n = len(a)
        self.move(n, a, b, c)

    def move(self, n: int, a: List[int], b: List[int], c: List[int]) -> None:
        if n == 1:
            c.append(a[-1])
            a.pop()
            return
        else:
            self.move(n - 1, a, c, b)
            c.append(a[-1])
            a.pop()
            self.move(n - 1, b, a, c)
    