# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]):

        maxdiff=[0]
        def depth(node):
            if not node: return 0
            left=depth(node.left)
            right=depth(node.right)
            maxdiff[0]=max(maxdiff[0],abs(left-right))
            return 1+max(left,right)
        depth(root)
        return True if maxdiff[0]<=1 else False



        