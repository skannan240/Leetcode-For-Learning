# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.same_tree(root, subRoot):
            return True
        elif (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)):
            return True
        
        
        
    def same_tree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return (self.same_tree(s.left, t.left) and
                    self.same_tree(s.right, t.right))
        return False
        