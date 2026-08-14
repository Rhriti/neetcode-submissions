# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root):
        self.arr=[root]
        self.lefttraversal()

    def lefttraversal(self):
        #we append all the left nodes here
        itr=self.arr[-1]
        while itr.left:
            self.arr.append(itr.left)
            itr=itr.left


    def next(self):
        out=self.arr.pop()
        if out.right:
            self.arr.append(out.right)
            self.lefttraversal()
        return out.val

    def hasNext(self):
        if self.arr:
            return True
        else: return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()