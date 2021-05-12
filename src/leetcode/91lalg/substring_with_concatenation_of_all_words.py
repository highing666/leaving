# -*- coding: utf-8 -*-

from collections import Counter
from typing import List


class Solution:

    def find_substring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        one_word = len(words[0])
        all_words_len = one_word * len(words)
        n = len(s)
        words_dic = Counter(words)
        res = list()

        for i in range(0, n - all_words_len + 1):
            temp = s[i:i + all_words_len]
            c_temp = list()
            for j in range(0, all_words_len, one_word):
                c_temp.append(temp[j:j + one_word])
            if Counter(c_temp) == words_dic:
                res.append(i)
        
        return res
