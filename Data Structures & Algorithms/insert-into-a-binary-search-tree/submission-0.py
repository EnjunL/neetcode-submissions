# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #if value to insert is bigger than root, check right side, if right side is empty, add to it, else keep getting right side if not empty
        #same idea for left side

        #once we reach an empty spot, it would pop this node back up to update the tree (it would either be on the left or right of a node based on the conditions)
        if not root:
            return TreeNode(val)

        #insert on right side
        if val > root.val:
            root.right = self.insertIntoBST(root.right,val)

        #insert on left side
        else:
            root.left = self.insertIntoBST(root.left,val)

        return root

