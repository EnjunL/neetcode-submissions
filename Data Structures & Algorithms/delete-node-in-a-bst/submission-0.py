# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        if key < root.val:
            root.left = self.deleteNode(root.left,key)
        elif key > root.val:
            root.right = self.deleteNode(root.right,key)
        # we have found the key
        else:
            #no left child
            if not root.left:
                return root.right
            #no right child
            elif not root.right:
                return root.left
            #have both child, we can pick the right side or the left side
            #i choose right side, find smallest of the right tree so that when I replace
            #the deleted node with it, the BST still holds.
            else:
                #picking the right side
                successor = root.right

                #finding the smallest value of the right side
                while successor.left:
                    successor=successor.left
                
                #replace value of 'deleted'(old) node with successor node
                root.val = successor.val

                #delete the node we originally copied from starting from the head of the
                #right subtree
                root.right = self.deleteNode(root.right,successor.val)

        return root