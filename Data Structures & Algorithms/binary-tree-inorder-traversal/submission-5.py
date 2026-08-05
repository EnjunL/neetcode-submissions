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
        cur = root
        #Keep going while there is either a current node to explore
        #or a saved node waiting in the stack.
        while cur or stack:
            #go left as long as we can
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            #shift to right node after popping from our stack 
            cur=cur.right
        return res
