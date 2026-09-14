# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #essentially use BFS, if right exists, add rightmost to the result.

        if not root:
            return []
        res=[]
        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                #if we are at the end of q, it would be our rightmost element
                if i == qLen-1:
                    res.append(node.val)
        return res
        
