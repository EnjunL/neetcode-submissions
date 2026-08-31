# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        if val > root.val:
            #"Fix/update my right subtree, then give me its root so I can reconnect it."
            root.right = self.insertIntoBST(root.right,val)
        else:
            #"Fix/update my left subtree, then give me its root so I can reconnect it."
            root.left = self.insertIntoBST(root.left,val)

        #"I'm done modifying my subtree. Its root is still this node, so give this node back to my parent."
        return root
