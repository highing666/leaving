# -*- coding: utf-8 -*-

from typing import List


class Solution:

    def max_chunks_to_sorted(self, arr: List[int]) -> int:
        stack = []
        for num in arr:
            if stack and num < stack[-1]:
                head = stack.pop()
                
                while stack and num < stack[-1]:
                    stack.pop()
                
                stack.append(head)
            else:
                stack.append(num)
        
        return len(stack)
