# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) :
        def check(root,subroot):
            if (root and not subroot) or (subroot and not root): return False
            if not root and not subroot: return True
            if root.val!=subroot.val: return False
     
            return check(root.left,subroot.left) and check(root.right,subroot.right)

            
        def traverse(root,subroot):
            t=check(root,subroot)
            if root.left:
                t=t or traverse(root.left,subroot)
            if root.right:
                t=t or traverse(root.right,subroot)        
            return t 
        return traverse(root,subRoot)


        