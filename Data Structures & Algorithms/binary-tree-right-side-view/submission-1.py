# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) :
        if not root:return []
        #bfs level by level , right most print
        q=[root]
        rightside=[]
        while q:
            temp_q=[]
            for ele in q:
                if ele.left:temp_q.append(ele.left)
                if ele.right:temp_q.append(ele.right)
            rightside.append(q[-1].val)
            q=temp_q
        return rightside
            
        