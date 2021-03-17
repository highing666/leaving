# -*- coding: utf-8 -*-

from typing import List


class Solution:

    @staticmethod
    def count_bits(num: int) -> List[int]:
        bits = [0]
        for i in range(1, num + 1):
            bits.append(bits[i >> 1] + (i & 1))

        return bits
