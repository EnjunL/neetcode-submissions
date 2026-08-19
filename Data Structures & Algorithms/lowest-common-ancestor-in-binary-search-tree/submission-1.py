# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # we are given a bst (left of node is smaller and right of node is bigger starting at root)

        # here is what we can deduce:
        # lca is on the left if p and q is < root
        # lca is on the right if p and q is > root
        # ow lca is the root since other options of p and q are exhausted and 
        # we know p and q can be descendants of itself

        if not root:
            return None

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root
        


