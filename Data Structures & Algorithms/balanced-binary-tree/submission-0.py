# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.left,self.right =0,0

        def dfs(node):
            if not node:
                return [True, 0] #returns isBalanced flag and height

            left, right = dfs(node.left), dfs(node.right)
            balanced = left[0] and right[0] and abs(left[1]-right[1]) <= 1
            return [balanced, 1+max([left[1],right[1]])]

        return dfs(root)[0]

            
            


        
        

        

        


        