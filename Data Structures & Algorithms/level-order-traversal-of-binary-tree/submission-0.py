# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]):
        if not root:return []

        stack=[root]
        arr=[]
        while stack:
            new_stack=[]
            new_arr=[]
            for node in stack:
                new_arr.append(node.val)
                if node.left and node.left is not None:new_stack.append(node.left)
                if node.right and node.right is not None:new_stack.append(node.right)
            arr.append(new_arr)
            stack=new_stack
        return arr
                

        