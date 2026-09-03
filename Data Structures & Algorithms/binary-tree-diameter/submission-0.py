# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) :

        maxdia=[0]
        def depth(node):
            if not node: return -1
            left=depth(node.left)
            right=depth(node.right)
            maxdia[0]=max(maxdia[0],left+right+2)
            return 1+max(left,right)
        depth(root)
        return maxdia[0]

        