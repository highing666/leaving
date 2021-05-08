# -*- coding: utf-8 -*-

from collections import Counter
from heapq import heappush, heapreplace
from typing import List


class Solution:

    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for key, val in count.items():
            if len(heap) >= k:
                if val > heap[0][0]:
                    heapreplace(heap, (val, key))
            else:
                heappush(heap, (val, key))

        return [item[1] for item in heap]
