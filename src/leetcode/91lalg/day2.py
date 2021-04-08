# -*- coding: utf-8 -*-

from typing import List


class Solution:

    def shortest(self, s: str, ch: str) -> List[int]:
        result = []
        length = len(s)

        for i in range(length):
            a = 99999
            for j in range(i, length):
                if s[j] == ch:
                    a = j - i
                    break
            
            b = 99999
            for k in range(i, 0, -1):
                if s[k] == ch:
                    b = i - k
                    break
            result.append(min(a, b))
        
        return result


if __name__ == '__main__':
    solution = Solution()
    test_string = 'loveleetcode'
    test_ch = 'e'
    print(solution.shortest(test_string, test_ch))
