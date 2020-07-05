# -*- coding: utf-8 -*-

from collections import OrderedDict

class Solution:

    def first_uniq_char(self, s: str) -> str:
        dic = OrderedDict()
        for ch in s:
            dic[ch] = not ch in dic
        for k, v in dic.items():
            if v:
                return k
        
        return ' '
