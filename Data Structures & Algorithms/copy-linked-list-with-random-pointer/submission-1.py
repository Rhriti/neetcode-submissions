"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]'):
        if not head: return None

        dup={}
        def traverse(node,parent):
            newnode=Node(node.val)
            dup[node]=newnode
            if parent:dup[parent].next=newnode
            if node.next:traverse(node.next,node)
        traverse(head,None)
        
        itr=head
        while itr:
            if itr.random:dup[itr].random=dup[itr.random]
            itr=itr.next

        return dup[head]



        