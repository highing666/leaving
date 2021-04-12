# -*- coding: utf-8 -*-

from typing import Tuple


class Solution:

    def k_encoded_string(self, src_str: str) -> str:

        def dfs(s: str, i) -> Tuple[int, str]:
            res, multi = '', 0

            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(s, i + 1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                
                i += 1
            
            return i, res
        
        _, result = dfs(src_str, 0)
        
        return result


if __name__ == '__main__':
    solution = Solution()
    test_str = '3[a]2[bc]'
    print(solution.k_encoded_string(test_str))
