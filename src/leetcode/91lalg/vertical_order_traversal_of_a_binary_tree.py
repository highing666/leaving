# -*- coding: utf-8 -*-

from collections import defaultdict
from typing import Collection, List


class TreeNode:

    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def vertical_traversal(self, root: TreeNode) -> List[List[int]]:
        seen = defaultdict(lambda: defaultdict(list))

        def dfs(node, x=0, y=0):
            if node:
                seen[x][y].append(node)
                dfs(node.left, x - 1, y + 1)
                dfs(node.right, x + 1, y + 1)
        
        dfs(root)

        ans = []

        for x in sorted(seen):
            report = []
            for y in sorted(seen[x]):
                report.extend(sorted(node.val for node in seen[x][y]))
            ans.append(report)
    
        return ans
