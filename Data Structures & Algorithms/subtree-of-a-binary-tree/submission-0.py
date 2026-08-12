# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #edge cases
        if not subRoot:
            return True
        if not root:
            return False
        
        def sameTree(p,q):
            #both reached end at same time
            if not p and not q:
                return True
            #one has ended while the other still has place to go
            if not p or not q:
                return False
            #valeus are diff
            if p.val != q.val:
                return False
            #returning the traversal of both the left and right side at the same time, if any side hits
            #a false case, we are able to stop and return false(not same tree)
            return sameTree(p.left,q.left) and sameTree(p.right,q.right)

        if sameTree(root,subRoot):
            return True
        #If the subtree doesn’t start at the current node, check whether it starts somewhere in the left subtree 
        #OR somewhere in the right subtree.
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
