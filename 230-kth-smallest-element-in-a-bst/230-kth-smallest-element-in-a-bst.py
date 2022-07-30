# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #number of elements we've visisted from tree
        #approaching problem iteratively 
        n = 0
        stack = []
        cur = root
        
        while cur or stack:
            while cur:
                #when this loops stops it means cur is at null
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n +=1 
            if n ==k:
                return cur.val
            cur = cur.right