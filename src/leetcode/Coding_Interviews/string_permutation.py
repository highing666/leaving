# -*- coding: utf-8 -*-


class Solution:

    @staticmethod
    def permutation(s: str) -> [str]:
        c, result = list(s), []

        def dfs(x):
            if x == len(c) - 1:
                result.append(''.join(c))
                return
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic:
                    continue
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]
                dfs(x + 1)
                c[i], c[x] = c[x], c[i]

        dfs(0)

        return result
