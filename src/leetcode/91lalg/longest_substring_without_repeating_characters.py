# -*- coding: utf-8 -*-

class Solution:

    def length_of_longest_substring(self, s: str) -> int:
        occ = set()
        rk, res = -1, 0

        for i in range(n := len(s)):
            if i != 0:
                occ.remove(s[i - 1])
            
            while rk + 1 < n and s[rk + 1] not in occ:
                occ.add(s[rk + 1])
                rk += 1
            
            res = max(res, rk - i + 1)
        
        return res
