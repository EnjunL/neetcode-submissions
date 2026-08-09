# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #global var
        res = 0
        #returns height
        def dfs(cur):
            if not cur:
                return 0

            left=dfs(cur.left)
            right=dfs(cur.right)
            nonlocal res
            #maximize diamater
            res = max(res, left+right)
            #max of the height from cur
            return 1+max(left,right)
        dfs(root)
        return res

