# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        current = root
        #while there are nodes in stack or current node exists
        while current or stack:
            #go as far left as we can
            while current:
                stack.append(current)
                current = current.left
            #pop back upwards
            current = stack.pop()
            res.append(current.val)

            #after appending the parent node, traverse right
            current = current.right
        return res