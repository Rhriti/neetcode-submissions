# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]):
        parent=None
        itr=head
        while itr:
            next=itr.next
            itr.next=parent
            parent=itr
            itr=next
        return parent
        