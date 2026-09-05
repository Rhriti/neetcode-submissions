# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) :
        parent=head_parent=ListNode()
        i=list1
        j=list2
        while i is not None and j is not None:
            if j.val<=i.val:
                curr=j
                j=j.next
            else:
                curr=i
                i=i.next
            
            parent.next=curr
            parent=curr
        if i is None and j is None:return head_parent.next
        if i is None: parent.next=j
        if j is None:parent.next=i
        return head_parent.next


