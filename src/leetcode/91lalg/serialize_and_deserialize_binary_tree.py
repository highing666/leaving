# -*- coding: utf-8 -*-

class TreeNode:

    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root: TreeNode) -> str:
        self.res = ''

        def dfs(root: TreeNode) -> None:
            if not root:
                self.res += 'None,'
            else:
                self.res += str(root.val)
                self.res += ','
                dfs(root.left)
                dfs(root.right)
        
        dfs(root)

        return self.res
                

    def deserialize(self, data: str) -> TreeNode:
        str_list = data.split(',')

        def dfs() -> None:
            s = str_list.pop(0)
            if s == 'None':
                return None
            else:
                root = TreeNode(int(s))
                root.left = dfs()
                root.right = dfs()
            
            return root
        
        return dfs()
    