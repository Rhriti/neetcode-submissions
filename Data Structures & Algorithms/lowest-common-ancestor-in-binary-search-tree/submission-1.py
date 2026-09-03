# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode):

        parent=set()
        def bs_parent(node):
            parent.add(node.val)
            if node.val==p.val:return 
            if p.val>node.val: bs_parent(node.right)
            else: bs_parent(node.left)
        bs_parent(root)
        print(parent,p.val)

        lca_arr=[0]
        def lca(node):
            if not node:return
            if  node.val in parent: lca_arr[0]=node
            print("lca_arr",lca_arr[0].val)
            if node.val==q.val:return 
            if q.val>node.val: lca(node.right)
            else: lca(node.left)
        lca(root)
        return lca_arr[0]



        