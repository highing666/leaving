# -*- coding: utf-8 -*-

from typing import List


class Solution:

    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        combine = []

        def dfs(target: int, idx: int) -> None:
            if idx == len(candidates):
                return
            if target == 0:
                ans.append(combine[:])
                return

            dfs(target, idx + 1)

            if target - candidates[idx] >= 0:
                combine.append(candidates[idx])
                dfs(target - candidates[idx], idx)
                combine.pop()

        dfs(target, 0)

        return ans


if __name__ == '__main__':
    test_candidates = [2, 3, 6, 7]
    test_target = 7

    solution = Solution()
    result = solution.combination_sum(test_candidates, test_target)
    print(result)
