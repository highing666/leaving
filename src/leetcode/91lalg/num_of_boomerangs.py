# -*- coding: utf-8 -*-

from collections import defaultdict
from typing import List


class Solution:

    def num_of_boomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(length := len(points)):
            hmap = defaultdict(int)
            for j in range(length):
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                dis = dx * dx + dy * dy
                hmap[dis] += 1
            
            for val in hmap.values():
                res += val * (val - 1)

        return res
